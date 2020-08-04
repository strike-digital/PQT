bl_info = {
    "name": "Dynamic enumerator example",
    "author": "Andrew Stevenson",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N-Panel",
    "description": "Dynamic enumerator example",
    "warning": "",
    "doc_url": "",
    "category": "Python",
}


import bpy
from bpy.props import EnumProperty

def enum_items(self,context):
    items = []
    material_slots = bpy.context.active_object.material_slots
    i = 0
    
    for material_slot in material_slots:
        material_name = material_slot.material.name
        items.append(
        (material_name,material_name,material_name)
        )
    
    return(items)

class TestSettings(bpy.types.PropertyGroup):
    
    material : EnumProperty(
            name = "",
            description = "material to display",
            items = enum_items,
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
