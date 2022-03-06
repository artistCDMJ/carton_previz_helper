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
           "version": (3, 20, 0),
           "blender": (3, 00, 0),
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
        default=(0.1, 0.1, 0.1),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):
        #add plane to just above the image plane reference
        bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0.002), scale=(1, 1, 1))
        #scale the new plane down to usable scale
        bpy.ops.transform.resize(value=(0.0818148, 0.0818148, 0.0818148), orient_type='GLOBAL')


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
    
    #bpy.ops.object.editmode_toggle()
    
    def execute(self, context):
        if bpy.context.object.display_type == 'TEXTURED':
            bpy.context.object.display_type = 'WIRE'
        elif bpy.context.object.display_type == 'WIRE':
            bpy.context.object.display_type = 'TEXTURED'
        else:
            bpy.context.object.display_type = 'WIRE'
            
        #toggle editmode - NIX THAT, too many button presses
        #bpy.ops.object.editmode_toggle()
        #set selection mode
        bpy.context.tool_settings.mesh_select_mode = (True, True, False)
        return {'FINISHED'}

class OBJECT_OT_center_mirror(bpy.types.Operator):
    """Center to selection and add mirror"""
    bl_idname = "object.center_mirror"
    bl_label = "Center and Add Mirror"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    #bpy.ops.object.editmode_toggle()
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        #idea to align cursor to selection and center and add a mirror modifier
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_add(type='MIRROR')
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
        #change to Edge and Face Select to prepare for Folding Stage
        bpy.context.tool_settings.mesh_select_mode = (False, True, True)


        return {'FINISHED'}
    
class OBJECT_OT_select_project(bpy.types.Operator):
    """Select All and Project from View"""
    bl_idname = "object.select_project"
    bl_label = "Project From View"
    bl_options = { 'REGISTER', 'UNDO' }
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        
        #bpy.ops.mesh.select_all(action='TOGGLE')
        #bpy.ops.mesh.select_all()

        bpy.ops.uv.project_from_view(camera_bounds=True, correct_aspect=False, scale_to_bounds=False)



        return {'FINISHED'} 
    
class OBJECT_OT_center_object(bpy.types.Operator):
    """center object and cursor to world"""
    bl_idname = "object.center_object"
    bl_label = "Center Object to World"
    bl_options = { 'REGISTER', 'UNDO' }
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        #cursor to world origin
        bpy.ops.view3d.snap_cursor_to_center()
        #selected object origin to geometry
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        bpy.ops.view3d.snap_selected_to_cursor(use_offset = False)

        return {'FINISHED'}   
    
############# haxx Solution for Camera Scale - adopt operators from paint camera and canvas import

#-----------------------------cameraview paint

class OBJECT_OT_Cameraview_model(bpy.types.Operator):
    """Set up Camera to match and follow Dieline"""
    bl_idname = "image.cameraview_model" 
    bl_label = "Camera View Model"
    bl_options = { 'REGISTER', 'UNDO' }

    
    @classmethod
    def poll(self, context):
        obj =  context.active_object
        A = obj is not None
        if A:
            B = obj.type == 'MESH'
            return B

    def execute(self, context):

        scene = context.scene

        #toggle on/off textpaint

        obj = context.active_object

       # if obj:
       #     mode = obj.mode
       #     # aslkjdaslkdjasdas
       #     if mode == 'TEXTURE_PAINT':
       #         bpy.ops.paint.texture_paint_toggle()

        #save selected plane by rename
        bpy.context.object.name = "ref_dieline_proxy"


        #variable to get image texture dimensions - thanks to Mutant Bob http://blender.stackexchange.com/users/660/mutant-bob
        #select_mat = bpy.context.active_object.data.materials[0].texture_slots[0].texture.image.size[:]
        
        #select_mat = []

        for ob in bpy.context.scene.objects:
            for s in ob.material_slots:
                if s.material and s.material.use_nodes:
                    for n in s.material.node_tree.nodes:
                        if n.type == 'TEX_IMAGE':
                            select_mat = n.image.size[:]
                            #print(obj.name,'uses',n.image.name,'saved at',n.image.filepath)

        #add camera
        bpy.ops.object.camera_add(enter_editmode=False,
        align='VIEW',
        location=(0, 0, 0),
        rotation=(0, -0, 0))

        #ratio full
        bpy.context.scene.render.resolution_percentage = 100

        #name it
        bpy.context.object.name = "Dieline Camera View"


        #switch to camera view
        bpy.ops.view3d.object_as_camera()

        #ortho view on current camera
        bpy.context.object.data.type = 'ORTHO'
        #move cam up in Z by 1 unit
        bpy.ops.transform.translate(value=(0, 0, 1),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(False, False, True),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff='SMOOTH',
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False)



        #switch on composition guides for use in cameraview paint
        #bpy.context.space_data.context = 'DATA'
        bpy.context.object.data.show_composition_center = True




        #found on net Atom wrote this simple script

        #image_index = 0

        rnd = bpy.data.scenes[0].render
        rnd.resolution_x, rnd.resolution_y = select_mat
        #bpy.context.object.data.ortho_scale = orthoscale

        rndx = rnd.resolution_x
        rndy = rnd.resolution_y
        #orthoscale = ((rndx - rndy)/rndy)+1


        if rndx >= rndy:
            orthoscale = ((rndx - rndy)/rndy)+1

        elif rndx < rndy:
            orthoscale = 1

        #set to use background image and assign from image texture- needs triage
        #bpy.context.object.data.show_background_images = True
        
        #set to orthographic
        bpy.context.object.data.ortho_scale = orthoscale
        #try to constrain cam to canvas here
        bpy.ops.object.constraint_add(type='COPY_ROTATION')
        bpy.context.object.constraints["Copy Rotation"].target = bpy.data.objects["ref_dieline_proxy"]
        
        bpy.context.object.data.show_name = True
        #hide camera itself
        bpy.ops.object.hide_view_set(unselected=False)


        bpy.context.selectable_objects

        #deselect camera
        bpy.ops.object.select_all(action='TOGGLE')
       # bpy.ops.object.select_all(action='TOGGLE')

        #select plane
        bpy.ops.object.select_all(action='DESELECT')
        ob = bpy.data.objects["ref_dieline_proxy"]
        bpy.context.view_layer.objects.active = ob
        
        return {'FINISHED'}
    

    
    

class PANEL_PT_carton_panel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_idname = "ch.settings"
    bl_space_type = 'VIEW_3D'
    bl_label = "Carton Viz Helper"
    bl_region_type = "UI"
    bl_category = "Carton Viz Helper"

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
        
                
        box = layout.box()                             
        col = box.column(align = True)
        col.label(text="Carton Primitives and Operations")
        row = col.row(align=True)
        #row.scale_y = 2.0
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.5
        row1.operator("object.carton_base", text = "Carton 3D Base", icon = 'VIEW3D')
        row2 = row.split(align=True)
        row2.scale_x=0.50
        row2.scale_y=1.5
        row2.operator("object.cartonflat_base", text = "Flat Carton", icon = 'MOD_MESHDEFORM')
        #row = layout.row()
        #row.scale_y = 1.5
        #row.operator("object.carton_base", text = "Carton 3D Base", icon = 'VIEW3D')
        row = layout.row()
        row = col.row(align=True)
        row.scale_x=0.50
        row.scale_y = 1.5
        row1 = row.split(align=True)
        row1.operator("object.add_bevel", text = "Bevel", icon = 'MESH_ICOSPHERE')
        
        row1.operator("object.wire_draw", text = "Wire", icon = 'MOD_SOLIDIFY')
                
        row = layout.row()
        row = col.row(align=True)
        row.scale_x=0.50
        row.scale_y = 1.5
        row2 = row.split(align=True)
        row2.operator("import_image.to_plane", text="Load Dieline", icon = 'MESH_GRID')
        row2.operator("image.cameraview_model", text = "DieCam", icon ="OUTLINER_OB_CAMERA")
        #row.operator("object.cartonflat_base", text = "Flat Carton", icon = 'MOD_MESHDEFORM')
        
        row = layout.row()
        row = col.row(align=True)
        row.scale_x=0.50
        row.scale_y = 1.5
        row3 = row.split(align=True)
        row3.operator("object.center_mirror", text = "Add Mirror", icon = 'ORIENTATION_VIEW')
        row3.operator("object.apply_xmirror", text = "XMirror", icon = 'MOD_MIRROR')
        

        box = layout.box()                        #big buttons aligned
        col = box.column(align = True)
        col.label(text='Carton UV Mapping')

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
        row3 = row.split(align=True)
        row3.scale_x=0.50
        row3.scale_y = 1.5
        row3.operator("object.select_project", text = "Flat Project", icon='ZOOM_PREVIOUS')

        #col.separator()
        # Big render button
        #layout.label(text=":")
       # row = layout.row()
       # row.scale_y = 1.5
        #row.operator("render.render")
        row = col.row(align=True)
        #row.scale_y = 2.0
        row3=row.split(align=True)
        row3.scale_x=0.50
        row3.scale_y=1.5
        row3.operator("object.center_object", text = "Center Object Origin", icon = 'ANCHOR_CENTER')

        row4 = row.split(align=True)
        row4.scale_x=0.50
        row4.scale_y=1.5
        row4.operator("render.render")


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
    OBJECT_OT_apply_xmirror,
    OBJECT_OT_select_project,
    OBJECT_OT_center_object,
    OBJECT_OT_Cameraview_model,
    OBJECT_OT_center_mirror
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
