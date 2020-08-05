bl_info = {
    "name": "Test",
    "author": "Andrew Stevenson",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Test addon",
    "warning": "",
    "doc_url": "",
    "category": "Test",
}


import bpy
from bpy.props import BoolProperty, FloatProperty, StringProperty, IntProperty, FloatVectorProperty, EnumProperty


class TestSettings(bpy.types.PropertyGroup):
    
    show_test : BoolProperty(
        name = "show test operator",
        description = "show test operator",
        default = False,
        )

class TEST_PT_panel(bpy.types.Panel):
    """Creates a Panel"""
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Test panel"
    bl_category = "Test panel"
    
    def draw(self, context):
        layout = self.layout
        tt = bpy.context.scene.test_tool
        
        layout.prop(tt, "show_test",)
        if tt.show_test:
            layout.operator("object.test")


class TEST_OT_operator(bpy.types.Operator):
    """Tests"""
    bl_idname = "object.test"
    bl_label = "Test operator"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        print("Test Operator")
        return {'FINISHED'}


classes = (
    TestSettings,
    TEST_PT_panel,
    TEST_OT_operator,
    )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.test_tool = bpy.props.PointerProperty(type=TestSettings)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.test_tool

if __name__ == "__main__":
    register()
