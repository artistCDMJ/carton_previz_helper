# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {"name": "Carton Helper Panel",
           "author": "CDMJ",
           "version": (2, 00, 0),
           "blender": (2, 80, 0),
           "location": "Toolbar > Misc Tab > Carton Panel",
           "description": "Carton Previs Studio Tool",
           "warning": "",
           "category": "Object"}

import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector



class OBJECT_OT_front_mapping(bpy.types.Operator):
    """Unwrap Front"""
    bl_idname = "object.unwrap_front"


    bl_label = "Unwrap Project Front"
    bl_options = { 'REGISTER', 'UNDO' }
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        scene = context.scene
        #new code
        bpy.ops.view3d.view_persportho() 
        bpy.ops.view3d.view_axis(type='FRONT')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True, correct_aspect=True, scale_to_bounds=False)       
                
        return {'FINISHED'}

class OBJECT_OT_back_mapping(bpy.types.Operator):
    """Unwrap Back"""
    bl_idname = "object.unwrap_back"


    bl_label = "Unwrap Project Back"
    bl_options = { 'REGISTER', 'UNDO' }
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        scene = context.scene
        #new code
        bpy.ops.view3d.view_persportho() 
        bpy.ops.view3d.view_axis(type='BACK')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True, correct_aspect=True, scale_to_bounds=False)       
                
        return {'FINISHED'}

class OBJECT_OT_top_mapping(bpy.types.Operator):
    """Unwrap Top"""
    bl_idname = "object.unwrap_top"


    bl_label = "Unwrap Project Top"
    bl_options = { 'REGISTER', 'UNDO' }
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        scene = context.scene
        #new code

        bpy.ops.view3d.view_persportho() 
        bpy.ops.view3d.view_axis(type='TOP')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True, correct_aspect=True, scale_to_bounds=False)       
                
        return {'FINISHED'}

class OBJECT_OT_bottom_mapping(bpy.types.Operator):
    """Unwrap Bottom"""
    bl_idname = "object.unwrap_bottom"


    bl_label = "Unwrap Project Bottom"
    bl_options = { 'REGISTER', 'UNDO' }
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        scene = context.scene


        #new code

        bpy.ops.view3d.view_persportho() 
        bpy.ops.view3d.view_axis(type='BOTTOM')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True, correct_aspect=True, scale_to_bounds=False)       
                
        return {'FINISHED'}

class OBJECT_OT_left_mapping(bpy.types.Operator):
    """Unwrap Left"""
    bl_idname = "object.unwrap_left"


    bl_label = "Unwrap Project Left"
    bl_options = { 'REGISTER', 'UNDO' }
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        scene = context.scene


        #new code

        bpy.ops.view3d.view_persportho() 
        bpy.ops.view3d.view_axis(type='LEFT')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True, correct_aspect=True, scale_to_bounds=False)       
                
        return {'FINISHED'}

class OBJECT_OT_right_mapping(bpy.types.Operator):
    """Unwrap Right"""
    bl_idname = "object.unwrap_right"


    bl_label = "Unwrap Project Right"
    bl_options = { 'REGISTER', 'UNDO' }
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        scene = context.scene


        #new code

        bpy.ops.view3d.view_persportho() 
        bpy.ops.view3d.view_axis(type='RIGHT')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True, correct_aspect=True, scale_to_bounds=False)       
                
        return {'FINISHED'}


class VIEW3D_OT_imperial_measurement(bpy.types.Operator):
    """Imperial"""
    bl_idname = "object.imperial_measure"


    bl_label = "Imperial Measurement"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene


        #new code

        bpy.context.scene.unit_settings.system = 'IMPERIAL'

        return {'FINISHED'}

class VIEW3D_OT_metric_measurement(bpy.types.Operator):
    """Metric"""
    bl_idname = "object.metric_measure"


    bl_label = "Metric Measurement"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene


        #new code

        bpy.context.scene.unit_settings.system = 'METRIC'

        return {'FINISHED'}

###################***************************experimental feature for carton :D robbed from templates
def add_object(self, context):
    scale_x = self.scale.x
    scale_y = self.scale.y
    scale_z = self.scale.z

    verts = [
        (+1.0, +1.0, -1.0),
        (+1.0, -1.0, -1.0),
        (-1.0, -1.0, -1.0),
        (-1.0, +1.0, -1.0),
        (+1.0, +1.0, +1.0),
        (+1.0, -1.0, +1.0),
        (-1.0, -1.0, +1.0),
        (-1.0, +1.0, +1.0),
    ]
    edges = []
    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (4, 0, 3, 7),
    ]

    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * scale_x, v[1] * scale_y, v[2] * scale_z

    #return verts, faces

    mesh = bpy.data.meshes.new(name="New Carton Base")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)



class OBJECT_OT_carton_base(bpy.types.Operator, AddObjectHelper):
    """Add Carton Base at Cursor Position - adjust Dimensions in Item Panel"""
    bl_idname = "object.carton_base"
    bl_label = "Carton Base"
    bl_options = { 'REGISTER', 'UNDO' }


    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):

        add_object(self, context)

        return {'FINISHED'}
    
class OBJECT_OT_cartonflat_base(bpy.types.Operator):
    """Add Plane for Construct of Carton Flat"""
    bl_idname = "object.cartonflat_base"
    bl_label = "Carton Flat Base"
    bl_options = { 'REGISTER', 'UNDO' }


    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):

        bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))


        return {'FINISHED'}

class OBJECT_OT_add_bevel(bpy.types.Operator):
    """Add Mod"""
    bl_idname = "object.add_bevel"


    bl_label = "Add Bevel"
    bl_options = { 'REGISTER', 'UNDO' }
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        scene = context.scene
        #add bevel mod to carton base
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].width = 0.0019752
        bpy.context.object.modifiers["Bevel"].show_in_editmode = True

        return {'FINISHED'}
    
class OBJECT_OT_wire_draw(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.wire_draw"
    bl_label = "Object to Wire"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if bpy.context.object.display_type == 'TEXTURED':
            bpy.context.object.display_type = 'WIRE'
        elif bpy.context.object.display_type == 'WIRE':
            bpy.context.object.display_type = 'TEXTURED'
        else:
            bpy.context.object.display_type = 'WIRE'
        return {'FINISHED'}
    
class OBJECT_OT_apply_xmirror(bpy.types.Operator):
    """Enable XMirror and Apply Mods"""
    bl_idname = "object.apply_xmirror"
    bl_label = "Xmirror ApplyMods"
    bl_options = { 'REGISTER', 'UNDO' }
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        bpy.ops.object.convert(target='MESH')
        #bpy.ops.object.editmode_toggle()
        bpy.context.object.data.use_mirror_x = True
        bpy.context.object.data.use_mirror_topology = True




        return {'FINISHED'}

class PANEL_PT_carton_panel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_idname = "ch.settings"
    bl_space_type = 'VIEW_3D'
    bl_label = "Settings"
    bl_region_type = "UI"
    bl_category = "Carton Helper"

    #OBJECT_OT_cartonflat_base,
    #OBJECT_OT_wire_draw
    
    def draw(self, context):
        layout = self.layout

        box = layout.box()                             #MACRO
        col = box.column(align = True)
        col.label(text="Carton Units")

        row = col.row(align=True)
        #row.scale_y = 2.0
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.5
        row1.operator("object.imperial_measure", text = "Imperial", icon = 'MOD_DECIM')

        row2 = row.split(align=True)

        row2.scale_x=0.50
        row2.scale_y=1.5
        row2.operator("object.metric_measure", text = "Metric", icon = 'MOD_BUILD')

        #col.separator()
        # Big render button
        #layout.label(text=":")
        box = layout.box()                             #MACRO
        col = box.column(align = True)
        col.label(text="Carton Primitives and Features")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("object.carton_base", text = "Carton Base", icon = 'VIEW3D')
        row.operator("object.wire_draw", text = "Wire Toggle", icon = 'MOD_SOLIDIFY')
        row = layout.row()
        row.scale_y = 1.5
        row.operator("object.cartonflat_base", text = "Carton Flat", icon = 'MOD_MESHDEFORM')
        row.operator("object.add_bevel", text = "Add Bevel", icon = 'MESH_ICOSPHERE')
        #object.apply_xmirror
        row.operator("object.apply_xmirror", text = "XMirror", icon = 'MOD_MIRROR')
        

        box = layout.box()                        #big buttons aligned
        col = box.column(align = True)
        col.label(text='Carton Sides')

        row = col.row(align=True)
        #row.scale_y = 2.0
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.5
        row1.operator("object.unwrap_front", text = "Front")
        row2 = row.split(align=True)

        row2.scale_x=0.50
        row2.scale_y=1.5
        row2.operator("object.unwrap_back", text = "Back")

        #col.separator()

        #box = layout.box()                        #big buttons aligned
        col = box.column(align = True)
        

        #row = col.row(align=True)
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.5
        row1.operator("object.unwrap_top", text = "Top")

        row2 = row.split(align=True)
        row2.scale_x=0.50
        row2.scale_y=1.5
        row2.operator("object.unwrap_bottom", text = "Bottom")

        #col.separator()

        row = col.row(align=True)
        #row.scale_y = 2.0
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.5
        row1.operator("object.unwrap_left", text = "Left", icon = 'PREV_KEYFRAME')

        row2 = row.split(align=True)
        row2.scale_x=0.50
        row2.scale_y=1.5
        row2.operator("object.unwrap_right", text = "Right", icon = 'NEXT_KEYFRAME')

        #col.separator()
        # Big render button
        #layout.label(text=":")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("render.render")


classes = (
    OBJECT_OT_front_mapping,
    OBJECT_OT_back_mapping,
    OBJECT_OT_top_mapping,
    OBJECT_OT_bottom_mapping,
    OBJECT_OT_left_mapping,
    OBJECT_OT_right_mapping,
    VIEW3D_OT_imperial_measurement,
    VIEW3D_OT_metric_measurement,
    OBJECT_OT_carton_base,
    OBJECT_OT_add_bevel,
    PANEL_PT_carton_panel,
    OBJECT_OT_cartonflat_base,
    OBJECT_OT_wire_draw,
    OBJECT_OT_apply_xmirror
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
