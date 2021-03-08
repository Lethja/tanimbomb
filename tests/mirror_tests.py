from unittest import TestCase
import animDump

JOINTS = [
{"name": "mPelvis"                 , "pos": [ 0    ,  0    ,  1.067], "rot": [ 0,   0   ,   0]},
{"name": "mSpine1"                 , "pos": [ 0    ,  0    ,  0.084], "rot": [ 0,   0   ,   0]},
{"name": "mSpine2"                 , "pos": [ 0    ,  0    , -0.084], "rot": [ 0,   0   ,   0]},
{"name": "mTorso"                  , "pos": [ 0    ,  0    ,  0.084], "rot": [ 0,   0   ,   0]},
{"name": "mSpine3"                 , "pos": [-0.015,  0    ,  0.205], "rot": [ 0,   0   ,   0]},
{"name": "mSpine4"                 , "pos": [ 0.015,  0    , -0.205], "rot": [ 0,   0   ,   0]},
{"name": "mChest"                  , "pos": [-0.015,  0    ,  0.205], "rot": [ 0,   0   ,   0]},
{"name": "mNeck"                   , "pos": [-0.01 ,  0    ,  0.251], "rot": [ 0,   0   ,   0]},
{"name": "mHead"                   , "pos": [ 0    , -0    ,  0.076], "rot": [ 0,   0   ,   0]},
{"name": "mSkull"                  , "pos": [ 0    ,  0    ,  0.079], "rot": [ 0,   0   ,   0]},
{"name": "mEyeLeft"                , "pos": [ 0.098,  0.036,  0.079], "rot": [ 0,  -0   ,   0]},
{"name": "mEyeRight"               , "pos": [ 0.098, -0.036,  0.079], "rot": [ 0,   0   ,  -0]},

{"name": "mCollarLeft"             , "pos": [-0.021,  0.085,  0.165], "rot": [ 0,   0   ,   0]},
{"name": "mCollarRight"            , "pos": [-0.021, -0.085,  0.165], "rot": [ 0,   0   ,   0]},
{"name": "mShoulderLeft"           , "pos": [ 0    ,  0.079, -0    ], "rot": [ 0,   0   ,   0]},
{"name": "mShoulderRight"          , "pos": [ 0    , -0.079, -0    ], "rot": [ 0,   0   ,   0]},
{"name": "mElbowLeft"              , "pos": [ 0    ,  0.248,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mElbowRight"             , "pos": [ 0    , -0.248, -0    ], "rot": [ 0,   0   ,   0]},
{"name": "mWristLeft"              , "pos": [-0    ,  0.205,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mWristRight"             , "pos": [ 0    , -0.205, -0    ], "rot": [ 0,   0   ,   0]},

{"name": "mWingsRoot"              , "pos": [-0.014,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mWing1Left"              , "pos": [-0.099,  0.105,  0.181], "rot": [ 0,   0   ,   0]},
{"name": "mWing1Right"             , "pos": [-0.099, -0.105,  0.181], "rot": [ 0,   0   ,   0]},
{"name": "mWing2Left"              , "pos": [-0.168,  0.169,  0.067], "rot": [ 0,   0   ,   0]},
{"name": "mWing2Right"             , "pos": [-0.168, -0.169,  0.067], "rot": [ 0,   0   ,   0]},
{"name": "mWing3Left"              , "pos": [-0.181,  0.183,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mWing3Right"             , "pos": [-0.181, -0.183,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mWing4Left"              , "pos": [-0.171,  0.173,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mWing4Right"             , "pos": [-0.171, -0.173,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mWing4FanLeft"           , "pos": [-0.171,  0.173,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mWing4FanRight"          , "pos": [-0.171, -0.173,  0    ], "rot": [ 0,   0   ,   0]},

{"name": "mHipLeft"                , "pos": [ 0.034,  0.127, -0.041], "rot": [ 0,   0   ,   0]},
{"name": "mHipRight"               , "pos": [ 0.034, -0.129, -0.041], "rot": [ 0,   0   ,   0]},
{"name": "mKneeLeft"               , "pos": [-0.001, -0.046, -0.491], "rot": [ 0,   0   ,   0]},
{"name": "mKneeRight"              , "pos": [-0.001,  0.049, -0.491], "rot": [ 0,   0   ,   0]},
{"name": "mAnkleLeft"              , "pos": [-0.029,  0.001, -0.468], "rot": [ 0,   0   ,   0]},
{"name": "mAnkleRight"             , "pos": [-0.029,  0    , -0.468], "rot": [ 0,   0   ,   0]},
{"name": "mFootLeft"               , "pos": [ 0.112, -0    , -0.061], "rot": [ 0,   0   ,   0]},
{"name": "mFootRight"              , "pos": [ 0.112, -0    , -0.061], "rot": [ 0,   0   ,   0]},
{"name": "mToeLeft"                , "pos": [ 0.109,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mToeRight"               , "pos": [ 0.109,  0    ,  0    ], "rot": [ 0,   0   ,   0]},

{"name": "mTail1"                  , "pos": [-0.116,  0    ,  0.047], "rot": [ 0,   0   ,   0]},
{"name": "mTail2"                  , "pos": [-0.197,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mTail3"                  , "pos": [-0.168,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mTail4"                  , "pos": [-0.142,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mTail5"                  , "pos": [-0.112,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mTail6"                  , "pos": [-0.094,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mGroin"                  , "pos": [ 0.064,  0    , -0.097], "rot": [ 0,   0   ,   0]},

{"name": "mHindLimbsRoot"          , "pos": [-0.2  ,  0    ,  0.084], "rot": [ 0,   0   ,   0]},
{"name": "mHindLimb1Left"          , "pos": [-0.204,  0.129, -0.125], "rot": [ 0,   0   ,   0]},
{"name": "mHindLimb1Right"         , "pos": [-0.204, -0.129, -0.125], "rot": [ 0,   0   ,   0]},
{"name": "mHindLimb2Left"          , "pos": [ 0.002, -0.046, -0.491], "rot": [ 0,   0   ,   0]},
{"name": "mHindLimb2Right"         , "pos": [ 0.002,  0.046, -0.491], "rot": [ 0,   0   ,   0]},
{"name": "mHindLimb3Left"          , "pos": [-0.03 , -0.003, -0.468], "rot": [ 0,   0   ,   0]},
{"name": "mHindLimb3Right"         , "pos": [-0.03 ,  0.003, -0.468], "rot": [ 0,   0   ,   0]},
{"name": "mHindLimb4Left"          , "pos": [ 0.112,  0    , -0.061], "rot": [ 0,   0   ,   0]},
{"name": "mHindLimb4Right"         , "pos": [ 0.112,  0    , -0.061], "rot": [ 0,   0   ,   0]},

{"name": "mHandThumb1Left"         , "pos": [ 0.031,  0.026,  0.004], "rot": [ 0,   0   ,   0]},
{"name": "mHandThumb1Right"        , "pos": [ 0.031, -0.026,  0.004], "rot": [ 0,   0   ,   0]},
{"name": "mHandThumb2Left"         , "pos": [ 0.028,  0.032, -0.001], "rot": [ 0,   0   ,   0]},
{"name": "mHandThumb2Right"        , "pos": [ 0.028, -0.032, -0.001], "rot": [ 0,   0   ,   0]},
{"name": "mHandThumb3Left"         , "pos": [ 0.023,  0.031, -0.001], "rot": [ 0,   0   ,   0]},
{"name": "mHandThumb3Right"        , "pos": [ 0.023, -0.031, -0.001], "rot": [ 0,   0   ,   0]},
{"name": "mHandIndex1Left"         , "pos": [ 0.038,  0.097,  0.015], "rot": [ 0,   0   ,   0]},
{"name": "mHandIndex1Right"        , "pos": [ 0.038, -0.097,  0.015], "rot": [ 0,   0   ,   0]},
{"name": "mHandIndex2Left"         , "pos": [ 0.017,  0.036, -0.006], "rot": [ 0,   0   ,   0]},
{"name": "mHandIndex2Right"        , "pos": [ 0.017, -0.036, -0.006], "rot": [ 0,   0   ,   0]},
{"name": "mHandIndex3Left"         , "pos": [ 0.014,  0.032, -0.006], "rot": [ 0,   0   ,   0]},
{"name": "mHandIndex3Right"        , "pos": [ 0.014, -0.032, -0.006], "rot": [ 0,   0   ,   0]},
{"name": "mHandMiddle1Left"        , "pos": [ 0.013,  0.101,  0.015], "rot": [ 0,   0   ,   0]},
{"name": "mHandMiddle1Right"       , "pos": [ 0.013, -0.101,  0.015], "rot": [ 0,   0   ,   0]},
{"name": "mHandMiddle2Left"        , "pos": [-0.001,  0.04 , -0.006], "rot": [ 0,   0   ,   0]},
{"name": "mHandMiddle2Right"       , "pos": [-0.001, -0.04 , -0.006], "rot": [ 0,   0   ,   0]},
{"name": "mHandMiddle3Left"        , "pos": [-0.001,  0.049, -0.008], "rot": [ 0,   0   ,   0]},
{"name": "mHandMiddle3Right"       , "pos": [-0.001, -0.049, -0.008], "rot": [ 0,   0   ,   0]},
{"name": "mHandRing1Left"          , "pos": [-0.01 ,  0.099,  0.009], "rot": [ 0,   0   ,   0]},
{"name": "mHandRing1Right"         , "pos": [-0.01 , -0.099,  0.009], "rot": [ 0,   0   ,   0]},
{"name": "mHandRing2Left"          , "pos": [-0.013,  0.038, -0.008], "rot": [ 0,   0   ,   0]},
{"name": "mHandRing2Right"         , "pos": [-0.013, -0.038, -0.008], "rot": [ 0,   0   ,   0]},
{"name": "mHandRing3Left"          , "pos": [-0.013,  0.04 , -0.009], "rot": [ 0,   0   ,   0]},
{"name": "mHandRing3Right"         , "pos": [-0.013, -0.04 , -0.009], "rot": [ 0,   0   ,   0]},
{"name": "mHandPinky1Left"         , "pos": [-0.031,  0.095,  0.003], "rot": [ 0,   0   ,   0]},
{"name": "mHandPinky1Right"        , "pos": [-0.031, -0.095,  0.003], "rot": [ 0,   0   ,   0]},
{"name": "mHandPinky2Left"         , "pos": [-0.024,  0.025, -0.006], "rot": [ 0,   0   ,   0]},
{"name": "mHandPinky2Right"        , "pos": [-0.024, -0.025, -0.006], "rot": [ 0,   0   ,   0]},
{"name": "mHandPinky3Left"         , "pos": [-0.015,  0.018, -0.004], "rot": [ 0,   0   ,   0]},
{"name": "mHandPinky3Right"        , "pos": [-0.015, -0.018, -0.004], "rot": [ 0,   0   ,   0]},

{"name": "mFaceRoot"               , "pos": [ 0.025,  0    ,  0.045], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyeAltLeft"         , "pos": [ 0.073,  0.036,  0.034], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyeAltRight"        , "pos": [ 0.073, -0.036,  0.034], "rot": [ 0,   0   ,   0]},
{"name": "mFaceForeheadLeft"       , "pos": [ 0.061,  0.035,  0.083], "rot": [ 0,   0   ,   0]},
{"name": "mFaceForeheadRight"      , "pos": [ 0.061, -0.035,  0.083], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyebrowOuterLeft"   , "pos": [ 0.064,  0.051,  0.048], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyebrowOuterRight"  , "pos": [ 0.064, -0.051,  0.048], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyebrowCenterLeft"  , "pos": [ 0.07 ,  0.043,  0.056], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyebrowCenterRight" , "pos": [ 0.07 , -0.043,  0.056], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyebrowInnerLeft"   , "pos": [ 0.075,  0.022,  0.051], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyebrowInnerRight"  , "pos": [ 0.075, -0.022,  0.051], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyeLidUpperLeft"    , "pos": [ 0.073,  0.036,  0.034], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyeLidUpperRight"   , "pos": [ 0.073, -0.036,  0.034], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyeLidLowerLeft"    , "pos": [ 0.073,  0.036,  0.034], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyeLidLowerRight"   , "pos": [ 0.073, -0.036,  0.034], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEar1Left"           , "pos": [ 0    ,  0.08 ,  0.002], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEar1Right"          , "pos": [ 0    , -0.08 ,  0.002], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEar2Left"           , "pos": [-0.019,  0.018,  0.025], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEar2Right"          , "pos": [-0.019, -0.018,  0.025], "rot": [ 0,   0   ,   0]},
{"name": "mFaceNoseCenter"         , "pos": [ 0.102,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mFaceNoseLeft"           , "pos": [ 0.086,  0.015, -0.004], "rot": [ 0,   0   ,   0]},
{"name": "mFaceNoseRight"          , "pos": [ 0.086, -0.015, -0.004], "rot": [ 0,   0   ,   0]},
{"name": "mFaceCheekLowerLeft"     , "pos": [ 0.05 ,  0.034, -0.031], "rot": [ 0,   0   ,   0]},
{"name": "mFaceCheekLowerRight"    , "pos": [ 0.05 , -0.034, -0.031], "rot": [ 0,   0   ,   0]},
{"name": "mFaceCheekUpperLeft"     , "pos": [ 0.07 ,  0.034, -0.005], "rot": [ 0,   0   ,   0]},
{"name": "mFaceCheekUpperRight"    , "pos": [ 0.07 , -0.034, -0.005], "rot": [ 0,   0   ,   0]},
{"name": "mFaceJaw"                , "pos": [-0.001,  0    , -0.015], "rot": [ 0,   0   ,   0]},
{"name": "mFaceChin"               , "pos": [ 0.074,  0    , -0.054], "rot": [ 0,   0   ,   0]},
{"name": "mFaceTeethLower"         , "pos": [ 0.021,  0    , -0.039], "rot": [ 0,   0   ,   0]},
{"name": "mFaceLipLowerCenter"     , "pos": [ 0.045,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mFaceLipLowerLeft"       , "pos": [ 0.045,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mFaceLipLowerRight"      , "pos": [ 0.045,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mFaceTongueBase"         , "pos": [ 0.039,  0    ,  0.005], "rot": [ 0,   0   ,   0]},
{"name": "mFaceTongueTip"          , "pos": [ 0.022,  0    ,  0.007], "rot": [ 0,   0   ,   0]},
{"name": "mFaceJawShaper"          , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "mFaceForeheadCenter"     , "pos": [ 0.069,  0    ,  0.065], "rot": [ 0,   0   ,   0]},
{"name": "mFaceNoseBase"           , "pos": [ 0.094,  0    , -0.016], "rot": [ 0,   0   ,   0]},
{"name": "mFaceTeethUpper"         , "pos": [ 0.02 ,  0    , -0.03 ], "rot": [ 0,   0   ,   0]},
{"name": "mFaceLipUpperLeft"       , "pos": [ 0.045,  0    , -0.003], "rot": [ 0,   0   ,   0]},
{"name": "mFaceLipUpperRight"      , "pos": [ 0.045,  0    , -0.003], "rot": [ 0,   0   ,   0]},
{"name": "mFaceLipCornerLeft"      , "pos": [ 0.028, -0.019, -0.01 ], "rot": [ 0,   0   ,   0]},
{"name": "mFaceLipCornerRight"     , "pos": [ 0.028,  0.019, -0.01 ], "rot": [ 0,   0   ,   0]},
{"name": "mFaceLipUpperCenter"     , "pos": [ 0.045,  0    , -0.003], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyecornerInnerLeft" , "pos": [ 0.075,  0.017,  0.032], "rot": [ 0,   0   ,   0]},
{"name": "mFaceEyecornerInnerRight", "pos": [ 0.075, -0.017,  0.032], "rot": [ 0,   0   ,   0]},
{"name": "mFaceNoseBridge"         , "pos": [ 0.091,  0    ,  0.02 ], "rot": [ 0,   0   ,   0]},

{"name": "PELVIS"                  , "pos": [-0.01 ,  0    , -0.02 ], "rot": [ 0,   8   ,   0]},
{"name": "BUTT"                    , "pos": [-0.06 ,  0    , -0.1  ], "rot": [ 0,   0   ,   0]},
{"name": "BELLY"                   , "pos": [ 0.028,  0    ,  0.04 ], "rot": [ 0,   8   ,   0]},
{"name": "LEFT_HANDLE"             , "pos": [ 0    ,  0.1  ,  0.058], "rot": [ 0,   0   ,   0]},
{"name": "RIGHT_HANDLE"            , "pos": [ 0    , -0.1  ,  0.058], "rot": [ 0,   0   ,   0]},
{"name": "LOWER_BACK"              , "pos": [ 0    ,  0    ,  0.023], "rot": [ 0,   0   ,   0]},
{"name": "CHEST"                   , "pos": [ 0.028,  0    ,  0.07 ], "rot": [ 0, -10   ,   0]},
{"name": "LEFT_PEC"                , "pos": [ 0.119,  0.082,  0.042], "rot": [ 0,   4.29,   0]},
{"name": "RIGHT_PEC"               , "pos": [ 0.119, -0.082,  0.042], "rot": [ 0,   4.29,   0]},
{"name": "UPPER_BACK"              , "pos": [ 0    ,  0    ,  0.017], "rot": [ 0,   0   ,   0]},
{"name": "NECK"                    , "pos": [ 0    ,  0    ,  0.02 ], "rot": [ 0,   0   ,   0]},
{"name": "HEAD"                    , "pos": [ 0.02 ,  0    ,  0.07 ], "rot": [ 0,   0   ,   0]},
{"name": "L_CLAVICLE"              , "pos": [ 0.02 ,  0    ,  0.02 ], "rot": [ 0,   0   ,   0]},
{"name": "R_CLAVICLE"              , "pos": [ 0.02 ,  0    ,  0.02 ], "rot": [ 0,   0   ,   0]},
{"name": "L_UPPER_ARM"             , "pos": [ 0    ,  0.12 ,  0.01 ], "rot": [-5,   0   ,   0]},
{"name": "R_UPPER_ARM"             , "pos": [ 0    , -0.12 ,  0.01 ], "rot": [ 5,   0   ,   0]},
{"name": "L_LOWER_ARM"             , "pos": [ 0    ,  0.1  ,  0    ], "rot": [-3,   0   ,   0]},
{"name": "R_LOWER_ARM"             , "pos": [ 0    , -0.1  ,  0    ], "rot": [ 3,   0   ,   0]},
{"name": "L_HAND"                  , "pos": [ 0.01 ,  0.05 ,  0    ], "rot": [-3,   0   , -10]},
{"name": "R_HAND"                  , "pos": [ 0.01 , -0.05 ,  0    ], "rot": [ 3,   0   ,  10]},
{"name": "L_UPPER_LEG"             , "pos": [-0.02 , -0.05 , -0.22 ], "rot": [ 0,   0   ,   0]},
{"name": "R_UPPER_LEG"             , "pos": [-0.02 ,  0.05 , -0.22 ], "rot": [ 0,   0   ,   0]},
{"name": "L_LOWER_LEG"             , "pos": [-0.02 ,  0    , -0.2  ], "rot": [ 0,   0   ,   0]},
{"name": "R_LOWER_LEG"             , "pos": [-0.02 ,  0    , -0.2  ], "rot": [ 0,   0   ,   0]},
{"name": "L_FOOT"                  , "pos": [ 0.077,  0    , -0.041], "rot": [ 0,  10   ,   0]},
{"name": "R_FOOT"                  , "pos": [ 0.077,  0    , -0.041], "rot": [ 0,  10   ,   0]},

{"name": "Pelvis"                  , "pos": [ 0    ,  0    , -0.15 ], "rot": [ 0,   0   ,   0]},
{"name": "Stomach"                 , "pos": [ 0.092,  0    ,  0.088], "rot": [ 0,   0   ,   0]},
{"name": "Left Pec"                , "pos": [ 0.104,  0.082,  0.247], "rot": [ 0,   0   ,   0]},
{"name": "Right Pec"               , "pos": [ 0.104, -0.082,  0.247], "rot": [ 0,   0   ,   0]},
{"name": "Chest"                   , "pos": [ 0.15 ,  0    , -0.1  ], "rot": [ 0,  90   ,  90]},
{"name": "Spine"                   , "pos": [-0.15 ,  0    , -0.1  ], "rot": [ 0, -90   ,  90]},
{"name": "Neck"                    , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Mouth"                   , "pos": [ 0.12 ,  0    ,  0.001], "rot": [ 0,   0   ,   0]},
{"name": "Chin"                    , "pos": [ 0.12 ,  0    , -0.04 ], "rot": [ 0,   0   ,   0]},
{"name": "Nose"                    , "pos": [ 0.1  ,  0    ,  0.05 ], "rot": [ 0,   0   ,   0]},
{"name": "Skull"                   , "pos": [ 0    ,  0    ,  0.15 ], "rot": [ 0,   0   ,  90]},
{"name": "Left Ear"                , "pos": [ 0.015,  0.08 ,  0.017], "rot": [ 0,   0   ,   0]},
{"name": "Right Ear"               , "pos": [ 0.015, -0.08 ,  0.017], "rot": [ 0,   0   ,   0]},
{"name": "Left Eyeball"            , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Right Eyeball"           , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Alt Left Ear"            , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Alt Right Ear"           , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Alt Left Eye"            , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Alt Right Eye"           , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Jaw"                     , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Tongue"                  , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},

{"name": "Tail Base"               , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Tail Tip"                , "pos": [-0.025,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Left Wing"               , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Right Wing"              , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Groin"                   , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Left Hind Foot"          , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Right Hind Foot"         , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},

{"name": "Left Shoulder"           , "pos": [ 0    ,  0    ,  0.08 ], "rot": [ 0,   0   ,   0]},
{"name": "Right Shoulder"          , "pos": [ 0    ,  0    ,  0.08 ], "rot": [ 0,   0   ,   0]},
{"name": "L Upper Arm"             , "pos": [ 0.01 ,  0.15 , -0.01 ], "rot": [ 0,   0   ,   0]},
{"name": "R Upper Arm"             , "pos": [ 0.01 , -0.13 ,  0.01 ], "rot": [ 0,   0   ,   0]},
{"name": "L Forearm"               , "pos": [ 0    ,  0.113,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "R Forearm"               , "pos": [ 0    , -0.12 ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Left Hand"               , "pos": [ 0    ,  0.08 , -0.02 ], "rot": [ 0,   0   ,   0]},
{"name": "Right Hand"              , "pos": [ 0    , -0.08 , -0.02 ], "rot": [ 0,   0   ,   0]},
{"name": "Left Ring Finger"        , "pos": [-0.006,  0.019, -0.002], "rot": [ 0,   0   ,   0]},
{"name": "Right Ring Finger"       , "pos": [-0.006, -0.019, -0.002], "rot": [ 0,   0   ,   0]},

{"name": "Left Hip"                , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Right Hip"               , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "L Upper Leg"             , "pos": [-0.019, -0.034, -0.31 ], "rot": [ 0,   0   ,   0]},
{"name": "R Upper Leg"             , "pos": [-0.017,  0.041, -0.31 ], "rot": [ 0,   0   ,   0]},
{"name": "L Lower Leg"             , "pos": [-0.044, -0.007, -0.261], "rot": [ 0,   0   ,   0]},
{"name": "R Lower Leg"             , "pos": [-0.044, -0.007, -0.262], "rot": [ 0,   0   ,   0]},
{"name": "Left Foot"               , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Right Foot"              , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},

{"name": "Center 2"                , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Top Right"               , "pos": [ 0    , -0.5  ,  0.5  ], "rot": [ 0,   0   ,   0]},
{"name": "Top"                     , "pos": [ 0    ,  0    ,  0.5  ], "rot": [ 0,   0   ,   0]},
{"name": "Top Left"                , "pos": [ 0    ,  0.5  ,  0.5  ], "rot": [ 0,   0   ,   0]},
{"name": "Center"                  , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},
{"name": "Bottom Left"             , "pos": [ 0    ,  0.5  , -0.5  ], "rot": [ 0,   0   ,   0]},
{"name": "Bottom"                  , "pos": [ 0    ,  0    , -0.5  ], "rot": [ 0,   0   ,   0]},
{"name": "Bottom Right"            , "pos": [ 0    , -0.5  , -0.5  ], "rot": [ 0,   0   ,   0]},
{"name": "Avatar Center"           , "pos": [ 0    ,  0    ,  0    ], "rot": [ 0,   0   ,   0]},

]


JOINT_PAIRS = [
    ("mPelvis", "mPelvis",),
    ("mSpine1", "mSpine1",),
    ("mSpine2", "mSpine2",),
    ("mTorso", "mTorso",),
    ("mSpine3", "mSpine3",),
    ("mSpine4", "mSpine4",),
    ("mChest", "mChest",),
    ("mNeck", "mNeck",),
    ("mHead", "mHead",),
    ("mSkull", "mSkull",),
    ("mEyeLeft", "mEyeRight",),

    ("mCollarLeft", "mCollarRight",),
    ("mShoulderLeft", "mShoulderRight",),
    ("mElbowLeft", "mElbowRight",),
    ("mWristLeft", "mWristRight",),

    ("mWingsRoot", "mWingsRoot",),
    ("mWing1Left", "mWing1Right",),
    ("mWing2Left", "mWing2Right",),
    ("mWing3Left", "mWing3Right",),
    ("mWing4Left", "mWing4Right",),
    ("mWing4FanLeft", "mWing4FanRight",),

    ("mHipLeft", "mHipRight",),
    ("mKneeLeft", "mKneeRight",),
    ("mAnkleLeft", "mAnkleRight",),
    ("mFootLeft", "mFootRight",),
    ("mToeLeft", "mToeRight",),

    ("mTail1", "mTail1",),
    ("mTail2", "mTail2",),
    ("mTail3", "mTail3",),
    ("mTail4", "mTail4",),
    ("mTail5", "mTail5",),
    ("mTail6", "mTail6",),
    ("mGroin", "mGroin",),

    ("mHindLimbsRoot", "mHindLimbsRoot",),
    ("mHindLimb1Left", "mHindLimb1Right",),
    ("mHindLimb2Left", "mHindLimb2Right",),
    ("mHindLimb3Left", "mHindLimb3Right",),
    ("mHindLimb4Left", "mHindLimb4Right",),

    ("mHandThumb1Left", "mHandThumb1Right",),
    ("mHandThumb2Left", "mHandThumb2Right",),
    ("mHandThumb3Left", "mHandThumb3Right",),
    ("mHandIndex1Left", "mHandIndex1Right",),
    ("mHandIndex2Left", "mHandIndex2Right",),
    ("mHandIndex3Left", "mHandIndex3Right",),
    ("mHandMiddle1Left", "mHandMiddle1Right",),
    ("mHandMiddle2Left", "mHandMiddle2Right",),
    ("mHandMiddle3Left", "mHandMiddle3Right",),
    ("mHandRing1Left", "mHandRing1Right",),
    ("mHandRing2Left", "mHandRing2Right",),
    ("mHandRing3Left", "mHandRing3Right",),
    ("mHandPinky1Left", "mHandPinky1Right",),
    ("mHandPinky2Left", "mHandPinky2Right",),
    ("mHandPinky3Left", "mHandPinky3Right",),

    ("mFaceRoot", "mFaceRoot",),
    ("mFaceEyeAltLeft", "mFaceEyeAltRight",),
    ("mFaceForeheadLeft", "mFaceForeheadRight",),
    ("mFaceEyebrowOuterLeft", "mFaceEyebrowOuterRight",),
    ("mFaceEyebrowCenterLeft", "mFaceEyebrowCenterRight",),
    ("mFaceEyebrowInnerLeft", "mFaceEyebrowInnerRight",),
    ("mFaceEyeLidUpperLeft", "mFaceEyeLidUpperRight",),
    ("mFaceEyeLidLowerLeft", "mFaceEyeLidLowerRight",),
    ("mFaceEar1Left", "mFaceEar1Right",),
    ("mFaceEar2Left", "mFaceEar2Right",),
    ("mFaceNoseCenter", "mFaceNoseCenter",),
    ("mFaceNoseLeft", "mFaceNoseRight",),
    ("mFaceCheekLowerLeft", "mFaceCheekLowerRight",),
    ("mFaceCheekUpperLeft", "mFaceCheekUpperRight",),
    ("mFaceJaw", "mFaceJaw",),
    ("mFaceChin", "mFaceChin",),
    ("mFaceTeethLower", "mFaceTeethLower",),
    ("mFaceLipLowerCenter", "mFaceLipLowerCenter",),
    ("mFaceLipLowerLeft", "mFaceLipLowerRight",),
    ("mFaceTongueBase", "mFaceTongueBase",),
    ("mFaceTongueTip", "mFaceTongueTip",),
    ("mFaceJawShaper", "mFaceJawShaper",),
    ("mFaceForeheadCenter", "mFaceForeheadCenter",),
    ("mFaceNoseBase", "mFaceNoseBase",),
    ("mFaceTeethUpper", "mFaceTeethUpper",),
    ("mFaceLipUpperLeft", "mFaceLipUpperRight",),
    ("mFaceLipCornerLeft", "mFaceLipCornerRight",),
    ("mFaceLipUpperCenter", "mFaceLipUpperCenter",),
    ("mFaceEyecornerInnerLeft", "mFaceEyecornerInnerRight",),
    ("mFaceNoseBridge", "mFaceNoseBridge",),

    ("PELVIS", "PELVIS",),
    ("BUTT", "BUTT",),
    ("BELLY", "BELLY",),
    ("LEFT_HANDLE", "RIGHT_HANDLE",),
    ("LOWER_BACK", "LOWER_BACK",),
    ("CHEST", "CHEST",),
    ("LEFT_PEC", "RIGHT_PEC",),
    ("UPPER_BACK", "UPPER_BACK",),
    ("NECK", "NECK",),
    ("HEAD", "HEAD",),
    ("L_CLAVICLE", "R_CLAVICLE",),
    ("L_UPPER_ARM", "R_UPPER_ARM",),
    ("L_LOWER_ARM", "R_LOWER_ARM",),
    ("L_HAND", "R_HAND",),
    ("L_UPPER_LEG", "R_UPPER_LEG",),
    ("L_LOWER_LEG", "R_LOWER_LEG",),
    ("L_FOOT", "R_FOOT",),

    ("Pelvis", "Pelvis",),
    ("Stomach", "Stomach",),
    ("Left Pec", "Right Pec",),
    ("Chest", "Chest",),
    ("Spine", "Spine",),
    ("Neck", "Neck",),
    ("Mouth", "Mouth",),
    ("Chin", "Chin",),
    ("Nose", "Nose",),
    ("Skull", "Skull",),
    ("Left Ear", "Right Ear",),
    ("Left Eyeball", "Right Eyeball",),
    ("Alt Left Ear", "Alt Right Ear",),
    ("Alt Left Eye", "Alt Right Eye",),
    ("Jaw", "Jaw",),
    ("Tongue", "Tongue",),

    ("Tail Base", "Tail Base",),
    ("Tail Tip", "Tail Tip",),
    ("Left Wing", "Right Wing",),
    ("Groin", "Groin",),
    ("Left Hind Foot", "Right Hind Foot",),

    ("Left Shoulder", "Right Shoulder",),
    ("L Upper Arm", "R Upper Arm",),
    ("L Forearm", "R Forearm",),
    ("Left Hand", "Right Hand",),
    ("Left Ring Finger", "Right Ring Finger",),

    ("Left Hip", "Right Hip",),
    ("L Upper Leg", "R Upper Leg",),
    ("L Lower Leg", "R Lower Leg",),
    ("Left Foot", "Right Foot",),

    ("Center 2", "Center 2",),
    ("Top", "Top",),
    ("Top Left", "Top Right",),
    ("Center", "Center",),
    ("Bottom", "Bottom",),
    ("Bottom Left", "Bottom Right",),
    ("Avatar Center", "Avatar Center",),
]


class MirrorTest(TestCase):
    def test_mirror_name(self):
        for a, b in JOINT_PAIRS:
            self.assertEqual(animDump.MirrorJoints.mirror_joint_name(a), b)
            self.assertEqual(animDump.MirrorJoints.mirror_joint_name(b), a)
