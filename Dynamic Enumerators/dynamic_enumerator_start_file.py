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
from bpy.props import EnumProperty




class TestSettings(bpy.types.PropertyGroup):
    
    material : EnumProperty(
        name = "Material",
        description = "Material",
        default = "Red",
        items=[ 
            ('Red', "Red", "Red"),
            ('Green', "Green", "Green"),
            ('Blue', "Blue", "Blue"),],
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
        mat = bpy.data.materials[tt.material]
        
        layout.prop(tt, "material",)
        layout.prop(mat, "diffuse_color", text="Color")


classes = (
    TestSettings,
    TEST_PT_panel,
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
