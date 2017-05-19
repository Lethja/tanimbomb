#!/usr/bin/env python

import argparse
import struct
import copy
import sys

# http://stackoverflow.com/questions/442188/readint-readbyte-readstring-etc-in-python
#
class BinaryStream:
    def __init__(self, base_stream):
        self.base_stream = base_stream

    def readBytes(self, length):
        return self.base_stream.read(length)

    def writeBytes(self, value):
        self.base_stream.write(value)

    def unpack(self, fmt):
        return struct.unpack(fmt, self.readBytes(struct.calcsize(fmt)))

    def pack(self, fmt, *data):
        return self.writeBytes(struct.pack(fmt, *data))

    # http://stackoverflow.com/questions/32774910/clean-way-to-read-a-null-terminated-c-style-string-from-a-file
    def readCString(self):
        buf = bytearray()
        while True:
            b = self.base_stream.read(1)
            if b is None or b == '\0':
                return str(buf)
            else:
                buf.append(b)

    def writeCString(self, string):
        self.writeBytes(string)
        self.writeBytes("\0")

class JointMotion(object):
    KEY_SIZE = 8

    @property
    def rotKeyCount(self):
        return len(self.rotKeys) / JointMotion.KEY_SIZE

    @property
    def locKeyCount(self):
        return len(self.locKeys) / JointMotion.KEY_SIZE


class JointConstraintSharedData(object):
    pass

class KeyframeMotion(object):
    def deserialize(self, file):
        stream = BinaryStream(file)
        (self.version, self.subVersion, self.priority, self.duration) = stream.unpack("HHif")
        self.emote = stream.readCString()
        (self.loopIn, self.loopOut, self.loop, self.easeIn, self.easeOut, self.handPosture, jointCount) = stream.unpack("ffiffii")
        self.joints = list()
        for jointNum in range(jointCount):
            joint = JointMotion()
            self.joints.append(joint)
            joint.name = stream.readCString()
            (joint.priority, rotKeyCount) = stream.unpack("ii")
            joint.rotKeys = stream.readBytes(rotKeyCount * JointMotion.KEY_SIZE)
            (locKeyCount,) = stream.unpack("i")
            joint.locKeys = stream.readBytes(locKeyCount * JointMotion.KEY_SIZE)
        (constraintCount,) = stream.unpack("i")
        self.constraints = list()
        for constraintNum in range(constraintCount):
            constraint = JointConstraintSharedData()
            self.constraints.append(constraint)
            (constraint.chainLength, constraint.type) = stream.unpack("BB")
            (constraint.sourceVolume, constraint.sourceOffsetX, constraint.sourceOffsetY, constraint.sourceOffsetZ,
                constraint.targetVolume, constraint.targetOffsetX, constraint.targetOffsetY, constraint.targetOffsetZ,
                constraint.targetDirX, constraint.targetDirY, constraint.targetDirZ,
                constraint.easeInStart, constraint.easeInStop, constraint.easeOutStart, constraint.easeOutStop) = stream.unpack("16s3f16s3f3f4f")

    def serialize(self, file):
        stream = BinaryStream(file)
        stream.pack("HHif", self.version, self.subVersion, self.priority, self.duration)
        stream.writeCString(self.emote)
        stream.pack("ffiffii", self.loopIn, self.loopOut, self.loop, self.easeIn, self.easeOut, self.handPosture, len(self.joints))
        for joint in self.joints:
            stream.writeCString(joint.name)
            stream.pack("ii", joint.priority, joint.rotKeyCount)
            stream.writeBytes(joint.rotKeys)
            stream.pack("i", joint.locKeyCount)
            stream.writeBytes(joint.locKeys)
        stream.pack("i", len(self.constraints))
        for constraint in self.constraints:
            stream.pack("BB", constraint.chainLength, constraint.type)
            stream.pack("16s3f16s3f3f4f",
                constraint.sourceVolume, constraint.sourceOffsetX, constraint.sourceOffsetY, constraint.sourceOffsetZ,
                constraint.targetVolume, constraint.targetOffsetX, constraint.targetOffsetY, constraint.targetOffsetZ,
                constraint.targetDirX, constraint.targetDirY, constraint.targetDirZ,
                constraint.easeInStart, constraint.easeInStop, constraint.easeOutStart, constraint.easeOutStop)

    def dump(self):
        print "version: %d.%d" % (self.version, self.subVersion)
        print "priority: %d" % (self.priority,)
        print "duration: %f" % (self.duration,)
        print 'emote: "%s"' % (self.emote,)
        print 'loop: %d (%f - %f)' % (self.loop, self.loopIn, self.loopOut)
        print 'ease: %f - %f' % (self.easeIn, self.easeOut)
        print 'joints: %d' % (len(self.joints),)
        for joint in self.joints:
            print '\tP%d %dR %dL: %s' % (joint.priority, joint.rotKeyCount, joint.locKeyCount, joint.name)
        print 'constraints: %d' % (len(self.constraints),)
        for constraint in self.constraints:
            print "\tchain: %d type: %d\n\t\t%s + <%f, %f, %f> ->\n\t\t%s + <%f, %f, %f> at <%f, %f, %f>\n\t\tease: %f, %f - %f, %f" % (constraint.chainLength, constraint.type,
                constraint.sourceVolume, constraint.sourceOffsetX, constraint.sourceOffsetY, constraint.sourceOffsetZ,
                constraint.targetVolume, constraint.targetOffsetX, constraint.targetOffsetY, constraint.targetOffsetZ,
                constraint.targetDirX, constraint.targetDirY, constraint.targetDirZ,
                constraint.easeInStart, constraint.easeInStop, constraint.easeOutStart, constraint.easeOutStop)

    def summarize(self, name):
        rotJointCount = 0
        locJointCount = 0
        for joint in self.joints:
            if (joint.rotKeyCount > 0): rotJointCount += 1
            if (joint.locKeyCount > 0): locJointCount += 1
        print '%s: %dR %dL' % (name, rotJointCount, locJointCount)

class AnimTransform(object):
    def __init__(self):
        pass

    def __call__(self, anim):
        pass

class TransformJointsMatching(AnimTransform):
    def __init__(self, dropGlobs, keepGlobs, jointTransform):
        self.dropGlobs = dropGlobs
        self.keepGlobs = keepGlobs
        self.jointTransform = jointTransform

    def __repr__(self):
        return "TransformJointsMatching(%r, %r, %r)" % (self.dropGlobs,
                self.keepGlobs, self.jointTransform)

    def __call__(self, anim):
        pass


class AddConstraint(AnimTransform):
    def __init__(self, sourceVolume, targetVolume, chainLength):
        self.constraint = JointConstraintSharedData()
        self.constraint.chainLength = int(chainLength)
        self.constraint.type = 0 # 0: point, 1: plane
        self.constraint.sourceVolume = sourceVolume

        self.constraint.sourceOffsetX = 0
        self.constraint.sourceOffsetY = 0
        self.constraint.sourceOffsetZ = 0

        self.constraint.targetVolume = targetVolume
        self.constraint.targetOffsetX = 0
        self.constraint.targetOffsetY = 0
        self.constraint.targetOffsetZ = 0

        self.constraint.targetDirX = 0
        self.constraint.targetDirY = 0
        self.constraint.targetDirZ = 0

        self.constraint.easeInStart = 0
        self.constraint.easeInStop = 0
        self.constraint.easeOutStart = 10
        self.constraint.easeOutStop = 10

    def __call__(self, anim):
        anim.constraints.append(self.constraint)

class DropConstraints(AnimTransform):
    def __call__(self, anim):
        anim.constraints = list()

class JointTransform(object):
    def __call__(self, anim, joint):
        pass

class DropLocationKeyframes(JointTransform):
    def __call__(self, anim, joint):
        pass

class DropRotationKeyframes(JointTransform):
    def __call__(self, anim, joint):
        pass

class DropPriority(JointTransform):
    def __call__(self, anim, joint):
        pass


def _ensure_value(namespace, name, value):
    if getattr(namespace, name, None) is None:
        setattr(namespace, name, value)
    return getattr(namespace, name)

class AppendObjectAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=0, **kwargs):
        super(AppendObjectAction, self).__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        #print '%r %r %r' % (namespace, values, option_string)
        item = self.const(*values)
        items = copy.copy(_ensure_value(namespace, self.dest, []))
        items.append(item)
        setattr(namespace, self.dest, items)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description='Manipulate Secondlife .anim files')
    parser.add_argument('files', type=argparse.FileType('r'), nargs='+',
                        help='anim files to dump or process')
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--outputfiles', '-o', type=argparse.FileType('w'),
            nargs='*')

    parser.add_argument('--keep-loc', action='append')
    parser.add_argument('--drop-loc', action='append')
    parser.add_argument('--keep-rot', action='append')
    parser.add_argument('--drop-rot', action='append')
    parser.add_argument('--keep-pri', action='append')
    parser.add_argument('--drop-pri', action='append')

    parser.add_argument('--add-constraint', action=AppendObjectAction,
            dest='actions', const=AddConstraint, nargs=3)
    parser.add_argument('--drop-constraints', action=AppendObjectAction,
            dest='actions', const=DropConstraints)

    args = parser.parse_args()
    _ensure_value(args, 'actions', [])
    if (args.drop_loc):
        args.actions.append(TransformJointsMatching(args.drop_loc,
                args.keep_loc, DropLocationKeyframes()))
    if (args.drop_rot):
        args.actions.append(TransformJointsMatching(args.drop_rot,
                args.keep_rot, DropRotationKeyframes()))
    if (args.drop_pri):
        args.actions.append(TransformJointsMatching(args.drop_pri,
                args.keep_pri, DropPriority()))

    if (args.verbose >= 2):
        print args

    if args.outputfiles is None:
        # summarize all files
        for file in args.files:
            anim = KeyframeMotion()
            anim.deserialize(file)
            anim.summarize(file.name)
            if (args.verbose > 0):
                anim.dump()

    else:
        # convert files
        if (len(args.files) != len(args.outputfiles)):
            print "different number of input and output files"
            sys.exit();
        for inputFile,outputFile in zip(args.files, args.outputfiles):
            anim = KeyframeMotion()
            anim.deserialize(inputFile)
            for action in args.actions:
                action(anim)
            anim.serialize(outputFile)








