# Properties docs page:
# https://docs.blender.org/api/current/bpy.props.html

import bpy
from bpy.props import BoolProperty, BoolVectorProperty, CollectionProperty, EnumProperty, FloatProperty, FloatVectorProperty, IntProperty, IntVectorProperty, StringProperty

# Options, subtype and unit settings should be an enumerator in the given lists, e.g. options={"ANIMATABLE"}

# The soft_min, soft_max, min and max settings default and maximum vaules are actually 3.402823e+38

bpy.props.BoolProperty(
    name="",
    description="",
    default=False,
    options=["HIDDEN", "SKIP_SAVE", "ANIMATABLE",
             "LIBRARY_EDITABLE", "PROPORTIONAL", "TEXTEDIT_UPDATE"],
    tags={},
    subtype=["PIXEL", "UNSIGNED", "PERCENTAGE",
             "FACTOR", "ANGLE", "TIME", "DISTANCE", "NONE"],
    update=None,
    get=None,
    set=None
)

# https://docs.blender.org/api/current/bpy.props.html#bpy.props.BoolProperty

bpy.props.BoolVectorProperty(
    name="",
    description="",
    default=(False, False, False),
    options=["HIDDEN", "SKIP_SAVE", "ANIMATABLE",
             "LIBRARY_EDITABLE", "PROPORTIONAL", "TEXTEDIT_UPDATE"],
    tags={},
    subtype=["COLOR", "TRANSLATION", "DIRECTION", "VELOCITY", "ACCELERATION", "MATRIX", "EULER",
             "QUATERNION", "AXISANGLE", "XYZ", "COLOR_GAMMA", "LAYER", "LAYER_MEMBER", "POWER", "NONE"],
    size=3,
    update=None,
    get=None,
    set=None
)

# https://docs.blender.org/api/current/bpy.props.html#bpy.props.BoolVectorProperty

bpy.props.CollectionProperty(
    type=None,
    name="",
    description="",
    options=["HIDDEN", "SKIP_SAVE", "ANIMATABLE",
             "LIBRARY_EDITABLE", "PROPORTIONAL", "TEXTEDIT_UPDATE"],
    tags={}
)

# https://docs.blender.org/api/current/bpy.props.html#bpy.props.CollectionProperty

bpy.props.EnumProperty(
    items=[("identifier", "name", "description", "icon", "number"), ],
    name="",
    description="",
    default=None,
    options=["HIDDEN", "SKIP_SAVE", "ANIMATABLE",
             "LIBRARY_EDITABLE", "PROPORTIONAL", "TEXTEDIT_UPDATE"],
    tags={},
    update=None,
    get=None,
    set=None
)

# https://docs.blender.org/api/current/bpy.props.html#bpy.props.EnumProperty

bpy.props.FloatProperty(
    name="",
    description="",
    default=0.0,
    min=-1000,
    max=1000,
    soft_min=-1000,
    soft_max=,
    step=3, precision=2,
    options=["HIDDEN", "SKIP_SAVE", "ANIMATABLE",
             "LIBRARY_EDITABLE", "PROPORTIONAL", "TEXTEDIT_UPDATE"],
    tags={},
    subtype=["PIXEL", "UNSIGNED", "PERCENTAGE",
             "FACTOR", "ANGLE", "TIME", "DISTANCE", "NONE"],
    unit=["NONE", "LENGTH", "AREA", "VOLUME", "ROTATION", "TIME",
          "VELOCITY", "ACCELERATION", "MASS", "CAMERA", "POWER"],
    update=None,
    get=None,
    set=None
)

# https://docs.blender.org/api/current/bpy.props.html#bpy.props.FloatProperty

bpy.props.FloatVectorProperty(
    name="",
    description="",
    default=(0.0, 0.0, 0.0),
    min=-1000,
    max=1000,
    soft_min=-1000,
    soft_max=1000,
    step=3,
    precision=2,
    options=["HIDDEN", "SKIP_SAVE", "ANIMATABLE",
             "LIBRARY_EDITABLE", "PROPORTIONAL", "TEXTEDIT_UPDATE"],
    tags={},
    subtype=["COLOR", "TRANSLATION", "DIRECTION", "VELOCITY", "ACCELERATION", "MATRIX", "EULER",
             "QUATERNION", "AXISANGLE", "XYZ", "COLOR_GAMMA", "LAYER", "LAYER_MEMBER", "POWER", "NONE"],
    unit=["NONE", "LENGTH", "AREA", "VOLUME", "ROTATION", "TIME",
          "VELOCITY", "ACCELERATION", "MASS", "CAMERA", "POWER"],
    size=3,
    update=None,
    get=None,
    set=None
)

# https://docs.blender.org/api/current/bpy.props.html#bpy.props.FloatVectorProperty

bpy.props.IntProperty(
    name="",
    description="",
    default=0,
    min=-1000,
    max=1000,
    soft_min=-1000,
    soft_max=1000,
    step=1,
    options=["HIDDEN", "SKIP_SAVE", "ANIMATABLE",
             "LIBRARY_EDITABLE", "PROPORTIONAL", "TEXTEDIT_UPDATE"],
    tags={},
    subtype=["PIXEL", "UNSIGNED", "PERCENTAGE",
             "FACTOR", "ANGLE", "TIME", "DISTANCE", "NONE"],
    update=None,
    get=None,
    set=None
)

# https://docs.blender.org/api/current/bpy.props.html#bpy.props.IntProperty

bpy.props.IntVectorProperty(
    name="",
    description="",
    default=(0, 0, 0),
    min=-1000,
    max=1000,
    soft_min=-1000,
    soft_max=1000,
    step=1,
    options=["HIDDEN", "SKIP_SAVE", "ANIMATABLE",
             "LIBRARY_EDITABLE", "PROPORTIONAL", "TEXTEDIT_UPDATE"],
    tags={},
    subtype=["COLOR", "TRANSLATION", "DIRECTION", "VELOCITY", "ACCELERATION", "MATRIX", "EULER",
             "QUATERNION", "AXISANGLE", "XYZ", "COLOR_GAMMA", "LAYER", "LAYER_MEMBER", "POWER", "NONE"],
    size=3,
    update=None,
    get=None,
    set=None
)

# https://docs.blender.org/api/current/bpy.props.html#bpy.props.IntVectorProperty

bpy.props.StringProperty(
    name="",
    description="",
    default="",
    maxlen=0,
    options=["HIDDEN", "SKIP_SAVE", "ANIMATABLE",
             "LIBRARY_EDITABLE", "PROPORTIONAL", "TEXTEDIT_UPDATE"],
    tags={},
    subtype=["FILE_PATH", "DIR_PATH", "FILE_NAME",
             "BYTE_STRING", "PASSWORD", "NONE"],
    update=None,
    get=None,
    set=None
)

# https://docs.blender.org/api/current/bpy.props.html#bpy.props.StringProperty
