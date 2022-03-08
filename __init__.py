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

bl_info = {"name": "Carton Viz Helper",
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
    """Project selected face to UV Map in UV Editor using Shift to Front View and Project"""
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
    """Project selected face to UV Map in UV Editor using Shift to Back View and Project"""
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
    """Project selected face to UV Map in UV Editor using Shift to Top View and Project"""
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
    """Project selected face to UV Map in UV Editor using Shift to Bottom View and Project"""
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
    """Project selected face to UV Map in UV Editor using Shift to Left View and Project"""
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
    """Project selected face to UV Map in UV Editor using Shift to Right View and Project"""
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
    """Sets World Units to Imperial to input Inches and Feet"""
    bl_idname = "object.imperial_measure"


    bl_label = "Imperial Measurement"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene


        #new code

        bpy.context.scene.unit_settings.system = 'IMPERIAL'

        return {'FINISHED'}

class VIEW3D_OT_metric_measurement(bpy.types.Operator):
    """Sets World Units to Metric to input Centimeters and Millimeters"""
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
    """Add Carton 3D Base at Cursor Position - adjust Dimensions in Item Panel"""
    bl_idname = "object.carton_base"
    bl_label = "Carton 3D Base"
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
        bpy.context.object.name = "Carton Flat"

        #scale the new plane down to usable scale
        bpy.ops.transform.resize(value=(0.0818148, 0.0818148, 0.0818148), orient_type='GLOBAL')


        return {'FINISHED'}

class OBJECT_OT_add_bevel(bpy.types.Operator):
    """Applies Scale and Adds Bevel Modifier to 3D Carton Base"""
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
    """Toggles Wire Draw and Tex Draw and sets Selection Mode to Edge and Vertex"""
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
    """Center Origin to Selection and add Mirror Modifier for construct of Carton Flat"""
    bl_idname = "object.center_mirror"
    bl_label = "Center and Add Mirror"

    
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
    """Apply Mirror Modifier and Set X Mirror and Empty Vertex Groups"""
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
        bpy.context.object.data.use_mirror_topology = False
        #change to Edge and Face Select to prepare for Folding Stage
        bpy.context.tool_settings.mesh_select_mode = (False, True, True)
        
        #create empty vertex groups for assignment
        bpy.context.active_object.vertex_groups.new(name='_lip_')
        bpy.context.active_object.vertex_groups.new(name='_back_')
        bpy.context.active_object.vertex_groups.new(name='_top_')
        bpy.context.active_object.vertex_groups.new(name='_front_')
        bpy.context.active_object.vertex_groups.new(name='_bottom_')
        


        return {'FINISHED'}
    
class OBJECT_OT_select_project(bpy.types.Operator):
    """Project through Die Camera to Align Texture to Reference"""
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
    """Snaps cursor and Selected Object to World Center"""
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

## bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
class SCENE_OT_scene_pivot(bpy.types.Operator):
    """Toggle Pivot between Cursor and Median Point in 3D View"""
    bl_idname = "scene.pivot"
    bl_label = "Set Pivot Toggle"

    
    
    def execute(self, context):
        
        scene = context.scene
        
        #scene.tool_settings.transform_pivot_point : pivot
        if bpy.context.scene.tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        elif bpy.context.scene.tool_settings.transform_pivot_point == 'CURSOR':
            bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'
        else:
            bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
            
        #toggle editmode - NIX THAT, too many button presses
        #bpy.ops.object.editmode_toggle()
        #set selection mode
        #bpy.context.tool_settings.mesh_select_mode = (True, True, False)
        return {'FINISHED'}
    
    
class OBJECT_OT_cardboard(bpy.types.Operator):
    """Set A Cardboard Solidify Ready for Material Index 1"""
    bl_idname = "object.cardboard"
    bl_label = "Set Cardboard Thickness and Material"

    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        
        scene = context.scene
        
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = 0.002
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        bpy.context.object.modifiers["Solidify"].material_offset = 1
        bpy.context.object.modifiers["Solidify"].material_offset_rim = 1
        
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

        #select plane
        bpy.ops.object.select_all(action='DESELECT')
        ob = bpy.data.objects["ref_dieline_proxy"]
        bpy.context.view_layer.objects.active = ob
        
        return {'FINISHED'}
    
class CARTONVIZ_OT_add_basic(bpy.types.Operator):
    bl_label = "Carton Shader Base"
    bl_idname = "cartonviz.addbasic_operator"
    
    @classmethod
    def poll(self, context):
        obj =  context.active_object
        A = obj is not None
        if A:
            B = obj.type == 'MESH'
            return B
    
    def execute(self, context):
        
        material_basic = bpy.data.materials.new(name= "Carton Shader Base")
        material_basic.use_nodes = True
        
        bpy.context.object.active_material = material_basic
        
        principled_node = material_basic.node_tree.nodes.get('Principled BSDF')
        
        ###Principled Node Options
        principled_node.inputs[0].default_value = (1,0,0,1)
        principled_node.inputs[6].default_value = (0.2)
        principled_node.inputs[9].default_value = (0.282)
        
        ###Image Texture Node named Dieline        
        dieline_node = material_basic.node_tree.nodes.new('ShaderNodeTexImage')
        dieline_node.location = (-600, 400)
        dieline_node.label = ("Dieline")
        
        ###Image Texture named Colormap
        colormap_node = material_basic.node_tree.nodes.new('ShaderNodeTexImage')
        colormap_node.location = (-600, 100)
        colormap_node.label = ("Colormap")
        
        ###Image Texture named Bumpmap
        bumpmap_node = material_basic.node_tree.nodes.new('ShaderNodeTexImage')
        bumpmap_node.location = (-600, -200)
        bumpmap_node.label = ("Bumpmap")
        
        ###Color Mix Node named Switch
        mix_node = material_basic.node_tree.nodes.new('ShaderNodeMixRGB')
        mix_node.location = (-275, 250)
        mix_node.label = ("Switch")
        
        ###Color Mix Node named Switch
        bump_node = material_basic.node_tree.nodes.new('ShaderNodeBump')
        bump_node.location = (-275, -200)
        bump_node.label = ("Perforations")
        
        ###UV Mapping Node
        uv_node = material_basic.node_tree.nodes.new('ShaderNodeUVMap')
        uv_node.location = (-900, 60)
        uv_node.label = ("UV Projection")
        uv_node.uv_map = "UVMap"
        
        #####LINKING
        material_basic.node_tree.links.new(dieline_node.outputs[0], mix_node.inputs [1])
        material_basic.node_tree.links.new(colormap_node.outputs[0], mix_node.inputs [2])
        material_basic.node_tree.links.new(mix_node.outputs[0], principled_node.inputs [0])
        material_basic.node_tree.links.new(bumpmap_node.outputs[0], bump_node.inputs [2])
        material_basic.node_tree.links.new(bump_node.outputs[0], principled_node.inputs [22])
        
        material_basic.node_tree.links.new(uv_node.outputs[0], dieline_node.inputs [0])
        material_basic.node_tree.links.new(uv_node.outputs[0], colormap_node.inputs [0])
        material_basic.node_tree.links.new(uv_node.outputs[0], bumpmap_node.inputs [0])
        
        return {'FINISHED'}

class CARTONVIZ_OT_add_fiberboard(bpy.types.Operator):
    bl_label = "Carton Fiberboard Shader"
    bl_idname = "cartonviz.add_fiberboard"
    
    @classmethod
    def poll(self, context):
        obj =  context.active_object
        A = obj is not None
        if A:
            B = obj.type == 'MESH'
            return B
    
    def execute(self, context):
        
        material_fiber = bpy.data.materials.new(name= "Carton FiberBoard Shader")
        material_fiber.use_nodes = True
        bpy.ops.object.material_slot_add()

        bpy.context.object.active_material = material_fiber
        
        material_fiber.pass_index = 1

        #Principled Main Shader in Tree
        principled_node = material_fiber.node_tree.nodes.get('Principled BSDF')
        
        ###Principled Node Options for Fiberboard
        principled_node.inputs[0].default_value = (1,1,1,1)
        principled_node.inputs[9].default_value = (0.575)
        
        ###Tex Coordinate Node       
        texcoord = material_fiber.node_tree.nodes.new('ShaderNodeTexCoord')
        texcoord.location = (-1200, 400)
        texcoord.label = ("Coordinate Control")
        
        ###Mapping Node       
        mapping = material_fiber.node_tree.nodes.new('ShaderNodeMapping')
        mapping.location = (-1000, 400)
        mapping.label = ("Mapping Control")
        
        ###Voronoi Tex Node       
        voronoi = material_fiber.node_tree.nodes.new('ShaderNodeTexVoronoi')
        voronoi.location = (-800, 400)
        voronoi.label = ("Clumping Pattern")
        voronoi.inputs[2].default_value = 1

        
        ###Musgrave Tex Node       
        mus1 = material_fiber.node_tree.nodes.new('ShaderNodeTexMusgrave')
        mus1.location = (-700, 400)
        mus1.label = ("Breaking Pattern")
        mus1.musgrave_type = 'HYBRID_MULTIFRACTAL'
        mus1.inputs[2].default_value = 368.4
        mus1.inputs[3].default_value = 15
        mus1.inputs[4].default_value = 62.4
        mus1.inputs[5].default_value = 1.1
        
        ###Color Mix Node Mix
        mix = material_fiber.node_tree.nodes.new('ShaderNodeMixRGB')
        mix.location = (-500, 400)
        mix.blend_type = 'MIX'
        mix.label = ("Color Mix")
        mix.inputs[1].default_value = (0.0784733, 0.0723242, 0.0403656, 1)
        mix.inputs[2].default_value = (0.134364, 0.117563, 0.0779412, 1)

        


        
        ###Musgrave Tex Node       
        mus2 = material_fiber.node_tree.nodes.new('ShaderNodeTexMusgrave')
        mus2.location = (-800, 100)
        mus2.label = ("overlay Pattern")
        mus2.musgrave_type = 'FBM'
        mus2.inputs[2].default_value = 57.7
        mus2.inputs[3].default_value = 2.0
        mus2.inputs[4].default_value = 2.0
        mus2.inputs[5].default_value = 2.0
        
        ###Ramp for Overlay       
        ramp = material_fiber.node_tree.nodes.new('ShaderNodeValToRGB')
        ramp.location = (-700, 100)
        ramp.label = ("Spread of Overlay")
        ramp.color_ramp.elements[0].position = 0.5

        #ramp.elements[0].position = 0.513636
        
        ###Color Invert Node       
        invert = material_fiber.node_tree.nodes.new('ShaderNodeInvert')
        invert.location = (-500, 100)
        invert.label = ("overlay Pattern")

                
        ###Color Mix Node Multiply
        mult = material_fiber.node_tree.nodes.new('ShaderNodeMixRGB')
        mult.location = (-275, 400)
        mult.blend_type = 'MULTIPLY'
        mult.label = ("Multiplied Fiber")
        
        ###Color Mix Node Color
        color = material_fiber.node_tree.nodes.new('ShaderNodeMixRGB')
        color.location = (-200, 400)
        color.blend_type = 'MULTIPLY'
        color.label = ("Color Overlay")
        color.inputs[2].default_value = (0.5, 0.346006, 0.190594, 1)
        color.inputs[0].default_value = 0.125
        

        
        
        
        
        #####LINKING
        link = material_fiber.node_tree.links.new
        
        link(texcoord.outputs[0], mapping.inputs [0])
        link(mapping.outputs[0], voronoi.inputs [0])
        link(mapping.outputs[0], mus2.inputs [0])
        link(voronoi.outputs[0], mus1.inputs [6])
        link(mus1.outputs[0], mix.inputs [0])
        link(mix.outputs[0], mult.inputs [1])
        link(mus2.outputs[0], ramp.inputs [0])
        link(ramp.outputs[0], invert.inputs [1])
        link(invert.outputs[0], mult.inputs [2])
        link(mult.outputs[0], color.inputs [1])
        link(color.outputs[0], principled_node.inputs [0])
        

            
        return {'FINISHED'}

class CARTONVIZ_OT_add_corrugate(bpy.types.Operator):
    bl_label = "Carton Cardboard Shader"
    bl_idname = "cartonviz.add_corrugate"
    
    @classmethod
    def poll(self, context):
        obj =  context.active_object
        A = obj is not None
        if A:
            B = obj.type == 'MESH'
            return B
    
    def execute(self, context):
        
        material_corrugate = bpy.data.materials.new(name= "Carton Cardboard Shader")
        material_corrugate.use_nodes = True
        bpy.ops.object.material_slot_add()

        bpy.context.object.active_material = material_corrugate
        
        material_corrugate.pass_index = 1

        #Principled Main Shader in Tree
        principled_node = material_corrugate.node_tree.nodes.get('Principled BSDF')
        
        ###Principled Node Options for Fiberboard
        principled_node.inputs[0].default_value = (1,1,1,1)
        #principled_node.inputs[9].default_value = (0.575)
        
        ###Tex Coordinate Node       
        texcoord = material_corrugate.node_tree.nodes.new('ShaderNodeTexCoord')
        texcoord.location = (-1400, 400)
        texcoord.label = ("Coordinate Control")
        
        ###Mapping Node       
        mapping = material_corrugate.node_tree.nodes.new('ShaderNodeMapping')
        mapping.location = (-1200, 400)
        mapping.label = ("Mapping Control")
        
        ###Musgrave Tex Node       
        musG = material_corrugate.node_tree.nodes.new('ShaderNodeTexMusgrave')
        musG.location = (-1000, 300)
        musG.label = ("Fine Detail")
        musG.musgrave_type = 'FBM'
        musG.inputs[2].default_value = 392.5
        musG.inputs[3].default_value = 4.7
        musG.inputs[4].default_value = 2.0
        musG.inputs[5].default_value = 21.6

        
        ###Wave Tex Node       
        wave = material_corrugate.node_tree.nodes.new('ShaderNodeTexWave')
        wave.location = (-800, 400)
        wave.label = ("Corrugate Pattern")
        wave.wave_type = 'BANDS'
        wave.wave_profile = 'SIN'
        wave.inputs[1].default_value = 19.3
        wave.inputs[2].default_value = 1.7
        wave.inputs[3].default_value = 7.2
        wave.inputs[4].default_value = 1.0
        wave.inputs[5].default_value = 0.846
        
        ###Color Mix Node Mix
        mix = material_corrugate.node_tree.nodes.new('ShaderNodeMixRGB')
        mix.location = (-600, 400)
        mix.blend_type = 'MIX'
        mix.label = ("Color Mix")
        mix.inputs[1].default_value = (0.768151, 0.527115, 0.304987, 1)
        mix.inputs[2].default_value = (0.418289, 0.285621, 0.153472, 1)
        
        ###Color Mix Node Multiply
        mult = material_corrugate.node_tree.nodes.new('ShaderNodeMixRGB')
        mult.location = (-600, 400)
        mult.blend_type = 'MULTIPLY'
        mult.label = ("Color Multiply")        
        mult.inputs[2].default_value = (0.569034, 0.242213, 0.0763981, 1)        

        ###Bump Node
        bump = material_corrugate.node_tree.nodes.new('ShaderNodeBump')
        bump.location = (-600, 100)
        bump.inputs[0].default_value = 0.092
        
        
        

        
        
        
        
        #####LINKING
        link = material_corrugate.node_tree.links.new
        
        link(texcoord.outputs[0], mapping.inputs [0])
        link(mapping.outputs[0], musG.inputs [0])
        link(mapping.outputs[0], wave.inputs [0])
        link(musG.outputs[0], wave.inputs [6])
        link(wave.outputs[0], mix.inputs [0])
        link(wave.outputs[0], bump.inputs [2])
        link(mix.outputs[0], mult.inputs [1])
        link(mult.outputs[0], principled_node.inputs [0])
        link(bump.outputs[0], principled_node.inputs [22])
        
        

            
        return {'FINISHED'} 

    
    

class PANEL_PT_carton_panel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_idname = "Carton_panel"
    bl_space_type = 'VIEW_3D'
    bl_label = "Carton Units"
    bl_region_type = "UI"
    bl_category = "Carton Viz Helper"
    bl_options = {'DEFAULT_CLOSED'}
    

    
    def draw(self, context):
        layout = self.layout
        
        box = layout.box()                             #MACRO
        col = box.column(align = True)
        col.label(text="Change to Appropriate Units for Scene")
        row = col.row(align=True)
        #row.scale_y = 2.0
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.25
        row1.operator("object.imperial_measure", text = "Imperial", icon = 'MOD_DECIM')
        row2 = row.split(align=True)
        row2.scale_x=0.50
        row2.scale_y=1.25
        row2.operator("object.metric_measure", text = "Metric", icon = 'MOD_BUILD')
        
class PANEL_PT_CartonPrimitives(bpy.types.Panel):
    """Carton Modeling Tools"""
    bl_label = "Carton Modeling Tools"
    bl_idname = "PANEL_PT_CartonPrimitives"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Carton Viz Helper"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
                
        box = layout.box()                             
        col = box.column(align = True)
        col.label(text="Carton Building Starts Here")
        row = col.row(align=True)
        
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.25
        row1.operator("import_image.to_plane", text="Load Dieline", icon = 'MESH_GRID')
        row2 = row.split(align=True)
        row2.scale_x=0.50
        row2.scale_y=1.25
        row2.operator("image.cameraview_model", text = "DieCam", icon ="OUTLINER_OB_CAMERA")
                
        row = layout.row()
        row = col.row(align=True)
        row.scale_x=0.50
        row.scale_y = 1.25
        row2 = row.split(align=True)
        row2.operator("object.carton_base", text = "Carton 3D Base", icon = 'VIEW3D')
        row2.operator("object.cartonflat_base", text = "Flat Carton", icon = 'MOD_MESHDEFORM')
                
        row = layout.row()
        row = col.row(align=True)
        row.scale_x=0.50
        row.scale_y = 1.25
        row3 = row.split(align=True)
        row3.operator("object.wire_draw", text = "Wire", icon = 'MOD_SOLIDIFY')
        row3.operator("scene.pivot", text="Toggle Pivot", icon = 'PIVOT_CURSOR')

        row = layout.row()
        row = col.row(align=True)
        row.scale_x=0.50
        row.scale_y = 1.25
        row = row.split(align=False)
        row.operator("object.center_mirror", text = "Add Mirror", icon = 'ORIENTATION_VIEW')
        row.operator("object.apply_xmirror", text = "XMirror", icon = 'MOD_MIRROR')
        
        
class PANEL_PT_CartonUVMapping(bpy.types.Panel):
    """Carton Mapping Tools"""
    bl_label = "Carton UV Mapping Tools"
    bl_idname = "PANEL_PT_CartonMapping"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Carton Viz Helper"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
    
        box = layout.box()                        #big buttons aligned
        col = box.column(align = True)
        col.label(text='Project Each Face for Mapping')

        row = col.row(align=True)
        
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.25
        row1.operator("object.unwrap_front", text = "Front")
        row2 = row.split(align=True)

        row2.scale_x=0.50
        row2.scale_y=1.25
        row2.operator("object.unwrap_back", text = "Back")


        col = box.column(align = True)
        

       
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.25
        row1.operator("object.unwrap_top", text = "Top")

        row2 = row.split(align=True)
        row2.scale_x=0.50
        row2.scale_y=1.25
        row2.operator("object.unwrap_bottom", text = "Bottom")

       

        row = col.row(align=True)
       
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.25
        row1.operator("object.unwrap_left", text = "Left", icon = 'PREV_KEYFRAME')

        row2 = row.split(align=True)
        row2.scale_x=0.50
        row2.scale_y=1.25
        row2.operator("object.unwrap_right", text = "Right", icon = 'NEXT_KEYFRAME')
        row3 = row.split(align=True)
        row3.scale_x=0.50
        row3.scale_y = 1.25
        row3.operator("object.select_project", text = "Flat Project", icon='ZOOM_PREVIOUS')

        
       
        
class PANEL_PT_CartonFinishing(bpy.types.Panel):
    """Carton Finishing Tools"""
    bl_label = "Carton Finishing Tools"
    bl_idname = "PANEL_PT_CartonFinishing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Carton Viz Helper"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
    
        box = layout.box()                        #big buttons aligned
        col = box.column(align = True)
        col.label(text='Presets for Prep of Final Products')
        
        row = col.row(align=True)
        
        row1=row.split(align=True)
        row1.scale_x=0.50
        row1.scale_y=1.25
        row1.operator("object.center_object", text = "Center Object Origin", icon = 'ANCHOR_CENTER')
        row2 = row.split(align=True)

        row2.scale_x=0.50
        row2.scale_y=1.25
        #row2.operator("render.render")
        row2.operator("object.cardboard", text = "Cardboard Set", icon = 'MOD_LINEART')
        
        row = col.row(align=True)
        row = layout.row()
        row = col.row(align=True)
        row.scale_x=0.50
        row.scale_y = 1.25
        row1 = row.split(align=True)
        row1.operator("object.add_bevel", text = "Bevel", icon = 'MESH_ICOSPHERE')
        row1.operator("cartonviz.addbasic_operator", text = "Base Shader", icon = 'CON_FOLLOWTRACK')
        
        row = col.row(align=True)
        row = layout.row()
        row = col.row(align=True)
        row.scale_x=0.50
        row.scale_y = 1.25
        row1 = row.split(align=True)
        row1.operator("cartonviz.add_fiberboard", text = "Fiberboard", icon = 'MESH_GRID')
        row1.operator("cartonviz.add_corrugate", text = "Corrugate", icon = 'ALIGN_JUSTIFY')
        
        #cartonviz.add_fiberboard
        
        #row = col.row(align=True)
        row = layout.row()
        row2=row.split(align=True)
        row2.scale_x=0.50
        row2.scale_y=1.25
        
        row2.operator("render.render", text = "Render", icon = 'OUTLINER_OB_IMAGE')
        
        row = col.row(align=True)
        row.prop(obj, "name")

        





classes = [
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
    PANEL_PT_CartonPrimitives,
    PANEL_PT_CartonUVMapping,
    PANEL_PT_CartonFinishing,
    OBJECT_OT_cartonflat_base,
    OBJECT_OT_wire_draw,
    OBJECT_OT_apply_xmirror,
    OBJECT_OT_select_project,
    OBJECT_OT_center_object,
    OBJECT_OT_Cameraview_model,
    OBJECT_OT_center_mirror,
    SCENE_OT_scene_pivot,
    OBJECT_OT_cardboard,
    CARTONVIZ_OT_add_basic,
    CARTONVIZ_OT_add_fiberboard,
    CARTONVIZ_OT_add_corrugate
]


register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == '__main__':
    register()
