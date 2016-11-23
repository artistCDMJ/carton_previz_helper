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
           "version": (1, 00, 0),
           "blender": (2, 78, 0),
           "location": "Toolbar > Misc Tab > Carton Panel",
           "description": "Carton Previs Studio Tool",
           "warning": "Run only in Cycles",
           "category": "Object"}

import bpy

class ReprojectMask(bpy.types.Operator):
    """Reproject Mask"""
    bl_idname = "artist_paint.reproject_mask" 
                                     
     
    bl_label = "Reproject Mask by View"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        bpy.ops.object.editmode_toggle() #toggle edit mode
        bpy.ops.uv.project_from_view(camera_bounds=True, correct_aspect=False, scale_to_bounds=False) #project from view
        bpy.ops.object.editmode_toggle() #toggle back from edit mode
        bpy.ops.object.convert(target='MESH')#in obj mode, convert to mesh for correction on Artist Panel Vector Masks/Gpencil Masks

        bpy.ops.paint.texture_paint_toggle() #toggle texpaint
        return {'FINISHED'}
    

#next operator
class RemoveMods(bpy.types.Operator):
    """Remove Modifiers"""
    bl_idname = "artist_paint.remove_modifiers"
    bl_label = "Remove Modifiers"
    bl_options = { 'REGISTER','UNDO' }
    
    def execute(self, context):
        scene = context.scene
                
        
        #new code
        context = bpy.context
        scene = context.scene
        obj = context.object

        # get a reference to the current obj.data
        old_mesh = obj.data

        # settings for to_mesh
        apply_modifiers = False
        settings = 'PREVIEW'
        new_mesh = obj.to_mesh(scene, apply_modifiers, settings)

        # object will still have modifiers, remove them
        obj.modifiers.clear()

        # assign the new mesh to obj.data 
        obj.data = new_mesh

        # remove the old mesh from the .blend
        bpy.data.meshes.remove(old_mesh)
        bpy.context.object.draw_type = 'TEXTURED'    
            
        return {'FINISHED'}
    
    
class FrontMapping(bpy.types.Operator):
    """Unwrap Front"""
    bl_idname = "object.unwrap_front" 
                                     
     
    bl_label = "Unwrap Project Front"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        
        bpy.ops.view3d.viewnumpad(type='FRONT')
        bpy.ops.view3d.view_persportho()
        bpy.ops.uv.project_from_view(camera_bounds=False, correct_aspect=True, scale_to_bounds=False)
        bpy.context.space_data.viewport_shade = 'TEXTURED'

        return {'FINISHED'}
    
class BackMapping(bpy.types.Operator):
    """Unwrap Back"""
    bl_idname = "object.unwrap_back" 
                                     
     
    bl_label = "Unwrap Project Back"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        
        bpy.ops.view3d.viewnumpad(type='BACK')
        bpy.ops.view3d.view_persportho()
        bpy.ops.uv.project_from_view(camera_bounds=False, correct_aspect=True, scale_to_bounds=False)
        bpy.context.space_data.viewport_shade = 'TEXTURED'

        return {'FINISHED'} 

class TopMapping(bpy.types.Operator):
    """Unwrap Top"""
    bl_idname = "object.unwrap_top" 
                                     
     
    bl_label = "Unwrap Project Top"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        
        bpy.ops.view3d.viewnumpad(type='TOP')
        bpy.ops.view3d.view_persportho()
        bpy.ops.uv.project_from_view(camera_bounds=False, correct_aspect=True, scale_to_bounds=False)
        bpy.context.space_data.viewport_shade = 'TEXTURED'

        return {'FINISHED'} 

class BottomMapping(bpy.types.Operator):
    """Unwrap Bottom"""
    bl_idname = "object.unwrap_bottom" 
                                     
     
    bl_label = "Unwrap Project Bottom"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        
        bpy.ops.view3d.viewnumpad(type='BOTTOM')
        bpy.ops.view3d.view_persportho()
        bpy.ops.uv.project_from_view(camera_bounds=False, correct_aspect=True, scale_to_bounds=False)
        bpy.context.space_data.viewport_shade = 'TEXTURED'

        return {'FINISHED'}

class LeftMapping(bpy.types.Operator):
    """Unwrap Left"""
    bl_idname = "object.unwrap_left" 
                                     
     
    bl_label = "Unwrap Project Left"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        
        bpy.ops.view3d.viewnumpad(type='LEFT')
        bpy.ops.view3d.view_persportho()
        bpy.ops.uv.project_from_view(camera_bounds=False, correct_aspect=True, scale_to_bounds=False)
        bpy.context.space_data.viewport_shade = 'TEXTURED'

        return {'FINISHED'} 

class RightMapping(bpy.types.Operator):
    """Unwrap Right"""
    bl_idname = "object.unwrap_right" 
                                     
     
    bl_label = "Unwrap Project Right"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        
        bpy.ops.view3d.viewnumpad(type='RIGHT')
        bpy.ops.view3d.view_persportho()
        bpy.ops.uv.project_from_view(camera_bounds=False, correct_aspect=True, scale_to_bounds=False)
        bpy.context.space_data.viewport_shade = 'TEXTURED'

        return {'FINISHED'} 
  

class ImperialMeasurement(bpy.types.Operator):
    """Imperial"""
    bl_idname = "object.imperial_measure" 
                                     
     
    bl_label = "Imperial Measurement"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        
        bpy.context.scene.unit_settings.system = 'IMPERIAL'

        return {'FINISHED'} 

class MetricMeasurement(bpy.types.Operator):
    """Metric"""
    bl_idname = "object.metric_measure" 
                                     
     
    bl_label = "Metric Measurement"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        
        bpy.context.scene.unit_settings.system = 'METRIC'

        return {'FINISHED'} 

class CartonBase(bpy.types.Operator):
    """Add Carton Base"""
    bl_idname = "object.carton_base" 
                                     
     
    bl_label = "Carton Base"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        
        bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.object.editmode_toggle()
        bpy.ops.transform.translate(value=(0, 0, 1.00741), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
        bpy.ops.object.editmode_toggle()
        bpy.context.object.dimensions[0] = 2
        bpy.context.object.dimensions[1] = 2
        bpy.context.object.dimensions[2] = 2
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)




        return {'FINISHED'}  

class AddBevel(bpy.types.Operator):
    """Add Mod"""
    bl_idname = "object.add_bevel" 
                                     
     
    bl_label = "Add Bevel"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):

        scene = context.scene


        #new code
        
        bpy.ops.object.modifier_add(type='BEVEL')        
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].width = 0.021
        bpy.context.object.modifiers["Bevel"].show_in_editmode = False





        return {'FINISHED'} 
    
    
class CartonPanel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_label = "Carton Helper"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Carton Helper"
    
    
    def draw(self, context):
        layout = self.layout
        
        box = layout.box()                             #MACRO
        col = box.column(align = True)
        col.label(text="Carton Units") 
           
        row = col.row(align=True)
        #row.scale_y = 2.0
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=2.0
        row1.operator("object.imperial_measure", text = "Imperial", icon = 'MOD_DECIM')
        
        row2 = row.split(align=True)
        
        row2.scale_x=0.50
        row2.scale_y=2.0
        row2.operator("object.metric_measure", text = "Metric", icon = 'MOD_BUILD')
        
        #col.separator()
        # Big render button
        #layout.label(text=":")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.carton_base", text = "Carton Base", icon = 'VIEW3D')
        row.operator("object.add_bevel", text = "Add Bevel", icon = 'MESH_ICOSPHERE')
        
        box = layout.box()                        #big buttons aligned
        col = box.column(align = True)
        col.label('Carton Sides')
        
        row = col.row(align=True)
        #row.scale_y = 2.0
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=2.0
        row1.operator("object.unwrap_front", text = "Front", icon = 'TRIA_LEFT')
        row2 = row.split(align=True)
        
        row2.scale_x=0.50
        row2.scale_y=2.0
        row2.operator("object.unwrap_back", text = "Back", icon = 'TRIA_RIGHT')
        
        #col.separator()
        
        #box = layout.box()                        #big buttons aligned
        col = box.column(align = True)
        #col.label('Carton Sides')
        
        row = col.row(align=True)
        #row.scale_y = 2.0
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=2.0
        row1.operator("object.unwrap_top", text = "Top", icon = 'TRIA_UP')
        
        row2 = row.split(align=True)
        row2.scale_x=0.50
        row2.scale_y=2.0
        row2.operator("object.unwrap_bottom", text = "Bottom", icon = 'TRIA_DOWN')
        
        #col.separator()
        
        row = col.row(align=True)
        #row.scale_y = 2.0
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=2.0
        row1.operator("object.unwrap_left", text = "Left", icon = 'PREV_KEYFRAME')
        
        row2 = row.split(align=True)
        row2.scale_x=0.50
        row2.scale_y=2.0
        row2.operator("object.unwrap_right", text = "Right", icon = 'NEXT_KEYFRAME')
        
        #col.separator()
        # Big render button
        #layout.label(text=":")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("render.render")
        
        
        
        
#bpy.context.scene.unit_settings.system = 'IMPERIAL'
#bpy.context.scene.unit_settings.system = 'METRIC'




def register():
    bpy.utils.register_class(ImperialMeasurement)
    bpy.utils.register_class(CartonBase)
    bpy.utils.register_class(AddBevel)
    bpy.utils.register_class(FrontMapping)
    bpy.utils.register_class(BackMapping)
    bpy.utils.register_class(TopMapping)
    bpy.utils.register_class(BottomMapping)
    bpy.utils.register_class(LeftMapping)
    bpy.utils.register_class(RightMapping)
    bpy.utils.register_class(MetricMeasurement)
    bpy.utils.register_class(CartonPanel)
    
def unregister():
    bpy.utils.unregister_class(ImperialMeasurement)
    bpy.utils.unregister_class(CartonBase)
    bpy.utils.unregister_class(AddBevel)
    bpy.utils.unregister_class(FrontMapping)
    bpy.utils.unregister_class(BackMapping)
    bpy.utils.unregister_class(TopMapping)
    bpy.utils.unregister_class(BottomMapping)
    bpy.utils.unregister_class(LeftMapping)
    bpy.utils.unregister_class(RightMapping)
    bpy.utils.unregister_class(MetricMeasurement)
    bpy.utils.unregister_class(CartonPanel)
    
    
       
if __name__ == "__main__":
    register()
