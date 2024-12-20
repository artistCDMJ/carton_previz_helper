import bpy
from string import Template
from mathutils import Vector

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

# NON <pep8 compliant>
###############################################################################

bl_info = {"name": "Carton Viz Helper",
           "author": "CDMJ",
           "version": (3, 50, 3),
           "blender": (4, 2, 0),
           "location": "N-Panel > Carton Viz",
           "description": "CDMJ In-House Carton PreViz Helper Tool",
           "warning": "",
           "category": "Object"}


#------------------------ CV SCENE
class SCENE_OT_CartonScene(bpy.types.Operator):
    """Create Carton PreViz Scene"""
    bl_description = "Create Scene for Working in Carton Previz Helper"
    bl_idname = "cpv.create_cpv_scene"
    bl_label = "Create Scene for Carton Viz"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        for sc in bpy.data.scenes:
            if sc.name == "Carton PreViz":
                return False
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        _name = "Carton PreViz"
        for sc in bpy.data.scenes:
            if sc.name == _name:
                return {'FINISHED'}

        bpy.ops.scene.new(type='NEW')
        context.scene.name = _name
       
       
        #set to top view
        bpy.ops.view3d.view_axis(type='TOP', align_active=True)
        #set to Cycles
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.display_settings.display_device = 'sRGB'
        bpy.context.scene.view_settings.view_transform = 'Filmic'
        bpy.context.scene.view_settings.look = 'Very High Contrast'

        



       

        return {'FINISHED'}

class SCENE_OT_pose_frames(bpy.types.Operator):
    """Set up empty and keyframes over 5 frames for posing to camera"""
    bl_idname = "scene.pose_frames"
    bl_label = "Set Pose Frames"
    bl_options = { 'REGISTER', 'UNDO' }
    
#    @classmethod
#    def poll(cls, context):
#        return context.active_object is not None

    def execute(self, context):

        scene = context.scene


        #new code
        ################# Empty And Key Frames for Poses in 5 Frames
        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', 
                                location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.name = "Key Pose"
        bpy.context.object.empty_display_size = 5

        bpy.context.scene.frame_current = 1

        bpy.ops.anim.keyframe_insert_by_name(type="BUILTIN_KSI_LocRot")

        bpy.context.scene.frame_current = 2
        bpy.ops.transform.rotate(value=-0.785398, orient_axis='Z', 
                        orient_type='GLOBAL', 
                        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                        orient_matrix_type='GLOBAL', 
                        constraint_axis=(False, False, True), 
                        mirror=False, use_proportional_edit=False, 
                        proportional_edit_falloff='SMOOTH', 
                        proportional_size=1, use_proportional_connected=False, 
                        use_proportional_projected=False, snap=False, 
                        snap_elements={'INCREMENT'}, 
                        use_snap_project=False, snap_target='CLOSEST', 
                        use_snap_self=False, use_snap_edit=False, 
                        use_snap_nonedit=False, use_snap_selectable=False)


        bpy.ops.anim.keyframe_insert_by_name(type="BUILTIN_KSI_LocRot")

        #bpy.ops.object.rotation_clear(clear_delta=False)

        bpy.context.scene.frame_current = 3

        bpy.ops.transform.rotate(value=1.5708, orient_axis='Z', 
                        orient_type='GLOBAL',
                         orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
                         orient_matrix_type='GLOBAL', 
                         constraint_axis=(False, False, True), 
                         mirror=False, use_proportional_edit=False, 
                         proportional_edit_falloff='SMOOTH', 
                         proportional_size=1, use_proportional_connected=False, 
                         use_proportional_projected=False, snap=False, 
                         snap_elements={'INCREMENT'}, use_snap_project=False, 
                         snap_target='CLOSEST', use_snap_self=False, 
                         use_snap_edit=False, use_snap_nonedit=False, 
                         use_snap_selectable=False)

        bpy.ops.anim.keyframe_insert_by_name(type="BUILTIN_KSI_LocRot")



        bpy.context.scene.frame_current = 4

        bpy.ops.object.rotation_clear(clear_delta=False)
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', 
                        orient_type='GLOBAL', 
                        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
                        orient_matrix_type='GLOBAL', 
                        constraint_axis=(True, False, False), 
                        mirror=False, use_proportional_edit=False, 
                        proportional_edit_falloff='SMOOTH', 
                        proportional_size=1, use_proportional_connected=False, 
                        use_proportional_projected=False, snap=False, 
                        snap_elements={'INCREMENT'}, use_snap_project=False, 
                        snap_target='CLOSEST', use_snap_self=False, 
                        use_snap_edit=False, use_snap_nonedit=False, 
                        use_snap_selectable=False)

        bpy.ops.anim.keyframe_insert_by_name(type="BUILTIN_KSI_LocRot")


        #bpy.ops.object.rotation_clear(clear_delta=False)

        bpy.context.scene.frame_current = 5

        bpy.ops.transform.rotate(value=3.14159, orient_axis='X', 
                        orient_type='GLOBAL', 
                        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
                        orient_matrix_type='GLOBAL', 
                        constraint_axis=(True, False, False), mirror=False, 
                        use_proportional_edit=False, 
                        proportional_edit_falloff='SMOOTH', 
                        proportional_size=1, use_proportional_connected=False, 
                        use_proportional_projected=False, snap=False, 
                        snap_elements={'INCREMENT'}, use_snap_project=False, 
                        snap_target='CLOSEST', use_snap_self=False, 
                        use_snap_edit=False, use_snap_nonedit=False, 
                        use_snap_selectable=False)


        bpy.ops.anim.keyframe_insert_by_name(type="BUILTIN_KSI_LocRot")

        bpy.context.scene.frame_current = 1
        
        bpy.context.scene.frame_end = 5

        ##########################end new code 5 frames
        
        return {'FINISHED'}
##################### RENDER PREVIEW AND FINAL RENDER SETTINGS MACROS
class SCENE_OT_camera_targetrender(bpy.types.Operator):
    """Set New Camera Target Render System for Output of Poses"""
    bl_idname = "scene.camera_targetrender"
    bl_label = "Camera Target Render"
    bl_options = { 'REGISTER', 'UNDO' }


    def execute(self, context):
        #add new camera target empty

        #bpy.ops.object.empty_add(type='SPHERE', 
                    #align='WORLD', 
                    #location=(0, 0, 0), 
                    #scale=(1, 1, 1))
        #ctarget = bpy.context.object
        #ctarget.name = "Camera Target"

        #add new camera to scene make it track the target empty
        bpy.ops.object.camera_add(enter_editmode=False, align='WORLD', 
                    location=(0, -3.78, 1.75), 
                    rotation=(1.12574, 0, 0), 
                    scale=(1, 1, 1))
        my_cam = bpy.context.object
        bpy.context.scene.camera = my_cam
        bpy.context.object.name = "Camera Target Render"
        bpy.context.object.data.show_composition_thirds = True

        #bpy.ops.object.constraint_add(type='TRACK_TO')
        #bpy.context.object.constraints["Track To"].target = ctarget    
            
            

        return {'FINISHED'}

##################### RENDER PREVIEW AND FINAL RENDER SETTINGS MACROS
class SCENE_OT_playblast_fullrender(bpy.types.Operator):
    """Set output name and render all five frames to TMP folder"""
    bl_idname = "scene.playblast_fullrender"
    bl_label = "Playblast Full Render"
    bl_options = { 'REGISTER', 'UNDO' }
    
#    @classmethod
#    def poll(cls, context):
#        return context.active_object is not None

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        context.selected_objects
        
        name = mytool.carton_obj_name
       
        bpy.context.scene.render.filepath = "/tmp\\" + name

        bpy.ops.render.render(animation=True, use_viewport=True)
        
        

        return {'FINISHED'}



class SCENE_OT_preview_render(bpy.types.Operator):
    """preview render scene settings convenience"""
    bl_idname = "scene.preview_render"
    bl_label = "Preview Render"
    bl_options = { 'REGISTER', 'UNDO' }
    
#    @classmethod
#    def poll(cls, context):
#        return context.active_object is not None

    def execute(self, context):

        scene = context.scene


        #new code
        bpy.context.scene.render.resolution_x = 1200
        bpy.context.scene.render.resolution_y = 1200
        bpy.context.scene.render.resolution_percentage = 50
        

        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.use_denoising = True
        bpy.context.scene.render.film_transparent = True
        
        bpy.context.scene.view_settings.view_transform = 'Filmic'
        bpy.context.scene.view_settings.look = 'High Contrast'
        
        return {'FINISHED'}

class SCENE_OT_full_render(bpy.types.Operator):
    """full render scene settings convenience"""
    bl_idname = "scene.full_render"
    bl_label = "Full Render"
    bl_options = { 'REGISTER', 'UNDO' }
    
#    @classmethod
#    def poll(cls, context):
#        return context.active_object is not None

    def execute(self, context):

        scene = context.scene


        #new code
        bpy.context.scene.render.resolution_x = 1200
        bpy.context.scene.render.resolution_y = 1200
        bpy.context.scene.render.resolution_percentage = 200
        

        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.use_denoising = True
        bpy.context.scene.render.film_transparent = True
        bpy.context.scene.view_settings.look = 'High Contrast'
        
        

        return {'FINISHED'}






################## add Scene Unit Choice

    
class SCENE_OT_scene_unit(bpy.types.Operator):
    """Toggle Metric or Imperial"""
    bl_idname = "scene.scene_unit"
    bl_label = "Toggle Unit"
    bl_options = { 'REGISTER', 'UNDO' }
    


    def execute(self, context):

        scene = context.scene


        #new code

        if bpy.context.scene.unit_settings.system == 'METRIC':
            bpy.context.scene.unit_settings.system = 'IMPERIAL'
        elif bpy.context.scene.unit_settings.system == 'IMPERIAL':
            bpy.context.scene.unit_settings.system = 'METRIC'
            
        else:
            bpy.context.scene.unit_settings.system = 'METRIC'

        return {'FINISHED'}
    
############################### need to rewrite for toggle on single button :D

class OBJECT_OT_front_mapping(bpy.types.Operator):
    """Project selected face to UV Map in UV Editor using Shift \
     to Front View and Project"""
    bl_idname = "object.unwrap_front"
    bl_label = "Unwrap Project Front"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene
        # new code
        bpy.ops.view3d.view_persportho()
        bpy.ops.view3d.view_axis(type='FRONT')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True,
                                     correct_aspect=True,
                                     scale_to_bounds=False)
        return {'FINISHED'}


class OBJECT_OT_back_mapping(bpy.types.Operator):
    """Project selected face to UV Map in UV Editor using Shift \
    to Back View and Project"""
    bl_idname = "object.unwrap_back"
    bl_label = "Unwrap Project Back"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene
        # new code
        bpy.ops.view3d.view_persportho()
        bpy.ops.view3d.view_axis(type='BACK')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True,
                                     correct_aspect=True,
                                     scale_to_bounds=False)
        return {'FINISHED'}


class OBJECT_OT_top_mapping(bpy.types.Operator):
    """Project selected face to UV Map in UV Editor using Shift \
     to Top View and Project"""
    bl_idname = "object.unwrap_top"
    bl_label = "Unwrap Project Top"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene

        bpy.ops.view3d.view_persportho()
        bpy.ops.view3d.view_axis(type='TOP')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True,
                                     correct_aspect=True,
                                     scale_to_bounds=False)
        return {'FINISHED'}


class OBJECT_OT_bottom_mapping(bpy.types.Operator):
    """Project selected face to UV Map in UV Editor using Shift \
     to Bottom View and Project"""
    bl_idname = "object.unwrap_bottom"
    bl_label = "Unwrap Project Bottom"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene

        bpy.ops.view3d.view_persportho()
        bpy.ops.view3d.view_axis(type='BOTTOM')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True,
                                     correct_aspect=True,
                                     scale_to_bounds=False)
        return {'FINISHED'}


class OBJECT_OT_left_mapping(bpy.types.Operator):
    """Project selected face to UV Map in UV Editor using Shift \
    to Left View and Project"""
    bl_idname = "object.unwrap_left"
    bl_label = "Unwrap Project Left"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene

        bpy.ops.view3d.view_persportho()
        bpy.ops.view3d.view_axis(type='LEFT')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True,
                                     correct_aspect=True,
                                     scale_to_bounds=False)
        return {'FINISHED'}


class OBJECT_OT_right_mapping(bpy.types.Operator):
    """Project selected face to UV Map in UV Editor using Shift \
    to Right View and Project"""
    bl_idname = "object.unwrap_right"
    bl_label = "Unwrap Project Right"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene
        # new code
        bpy.ops.view3d.view_persportho()
        bpy.ops.view3d.view_axis(type='RIGHT')
        bpy.ops.view3d.view_selected()
        bpy.ops.uv.project_from_view(camera_bounds=True,
                                     correct_aspect=True,
                                     scale_to_bounds=False)
        return {'FINISHED'}


class CARTONVIZ_PG_add_object_helper(bpy.types.PropertyGroup):
    carton_obj_name: bpy.props.StringProperty(
        name="Name",
        description="Name for Generated Object and Collection",
    )
    carton_obj_name_flag: bpy.props.BoolProperty(
        name="Include units",
        description="Add units to name",
        default=False,
    )
    carton_obj_dimensions: bpy.props.FloatVectorProperty(
        name="Dims",
        description="Dimensions at unit scale",
        soft_min=0,
        soft_max=1000,
        default=(1, 1, 1),
        precision=16,
    )
    carton_enum_objs: bpy.props.EnumProperty(
        name="Add",
        description="Primitives to Add",
        items=[
            ("MESH_PLANE", "Plane", "primitive_plane_add"),
            ("MESH_CUBE", "Cube", "primitive_cube_add")
        ],
    )
    carton_enum_unit: bpy.props.EnumProperty(
        name="Units",
        description="Measurements for Use in Scene and Object",
        items=[
            ('UN1', "Millimeters mm", ""),
            ('UN2', "Inches IN", ""),
        ]
    )


class CARTONVIZ_OT_AddStart(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "cartonviz.myop_operator"

    item_type: bpy.props.StringProperty(
        name="Mesh Primitive",
        description="Type of mesh primitive to add",
        default="primitive_plane_add",
    )
    item_dimensions: bpy.props.FloatVectorProperty(
        name="Dimensions",
        description="Dimensions at unit scale",
        soft_min=0,
        soft_max=1000,
        default=(1, 1, 1),
        precision=16,
    )
    item_name: bpy.props.StringProperty(
        name="Name",
        description="Name for Generated Object",
    )

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        scalable_objs = [
            "primitive_cube_add",
            "primitive_uv_sphere_add",
            "primitive_cylinder_add",
            "primitive_cone_add",
        ]
        x, y, z = unit_conversion(context, Vector(self.item_dimensions))
        if self.item_type in scalable_objs:
            cmd = f"bpy.ops.mesh.{self.item_type}(scale=({x}, {y}, {z}))"
            eval(cmd)
        else:
            cmd = f"bpy.ops.mesh.{self.item_type}()"
            eval(cmd)
            ob = context.view_layer.objects.active
            ob.dimensions = Vector((x, y, z)) * 2
            bpy.ops.object.transform_apply(location=False, 
                                rotation=False, scale=True)

        # Set the name of the generated object
        context.view_layer.objects.active.name = self.item_name

        # Make the generated object a child of "ref_dieline_proxy"
        generated_object = bpy.data.objects.get(self.item_name)
        parent_object = bpy.data.objects.get("ref_dieline_proxy")

        if generated_object and parent_object:
            generated_object.parent = parent_object
            print(f"'{self.item_name}' is now parented to 'ref_dieline_proxy'.")

        bpy.ops.transform.translate(value=(0, 0, 4.68563e-05))

        return {'FINISHED'}


class CARTONVIZ_OT_my_collection(bpy.types.Operator):
    bl_label = "Add to Collection"
    bl_idname = "cartonviz.my_collection"
    bl_options = {'REGISTER', 'UNDO'}

    coll_name: bpy.props.StringProperty(
        name="Name",
        description="Name for Generated Collection",
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        context.selected_objects
        bpy.ops.object.move_to_collection(
            collection_index=0,
            is_new=True,
            new_collection_name=self.coll_name)
        return {'FINISHED'}


class OBJECT_OT_add_bevel(bpy.types.Operator):
    """Applies Scale and Adds Bevel Modifier to 3D Carton Base"""
    bl_idname = "object.add_bevel"
    bl_label = "Add Bevel"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene
        # add bevel mod to carton base
        bpy.ops.object.transform_apply(location=False,
                                       rotation=True,
                                       scale=True)
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].width = 0.0019752
        bpy.context.object.modifiers["Bevel"].show_in_editmode = True
        return {'FINISHED'}


class OBJECT_OT_wire_draw(bpy.types.Operator):
    """Toggles Wire Draw and Tex Draw and \
    sets Selection Mode to Edge and Vertex"""
    bl_idname = "object.wire_draw"
    bl_label = "Object to Wire"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    # bpy.ops.object.editmode_toggle()

    def execute(self, context):
        if bpy.context.object.display_type == 'TEXTURED':
            bpy.context.object.display_type = 'WIRE'
        elif bpy.context.object.display_type == 'WIRE':
            bpy.context.object.display_type = 'TEXTURED'
        else:
            bpy.context.object.display_type = 'WIRE'

        bpy.context.tool_settings.mesh_select_mode = (True, True, False)
        return {'FINISHED'}


class OBJECT_OT_center_mirror(bpy.types.Operator):
    """Center Origin to Selection and add\
    Mirror Modifier for construct of Carton Flat"""
    bl_idname = "object.center_mirror"
    bl_label = "Center and Add Mirror"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # idea to align cursor to selection and center and add a mirror modifier        
        
        bpy.ops.view3d.snap_cursor_to_selected()
        
        mode = bpy.context.mode        
        if mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')
            
        
        #bpy.ops.object.editmode_toggle()
        
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_clip = True
        
        return {'FINISHED'}


class OBJECT_OT_apply_xmirror(bpy.types.Operator):
    """Apply Mirror Modifier and Set X Mirror and Empty Vertex 
                    Groups plus two Shape Keys for Fold Work"""
    bl_idname = "object.apply_xmirror"
    bl_label = "Xmirror ApplyMods"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        #set up loop to make this work in Edit or Object
        mode = bpy.context.mode        
        if mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')
        
        
        
        bpy.ops.object.convert(target='MESH')
        # bpy.ops.object.editmode_toggle()
        bpy.context.object.data.use_mirror_x = True
        bpy.context.object.data.use_mirror_topology = False
        # change to Edge and Face Select to prepare for Folding Stage
        bpy.context.tool_settings.mesh_select_mode = (False, True, True)

        # create empty vertex groups for assignment
        bpy.context.active_object.vertex_groups.new(name='_lip_')
        bpy.context.active_object.vertex_groups.new(name='_back_')
        bpy.context.active_object.vertex_groups.new(name='_top_')
        bpy.context.active_object.vertex_groups.new(name='_front_')
        bpy.context.active_object.vertex_groups.new(name='_bottom_')
        
        ########### experimental break to shape key storage of flat and fold
        context = bpy.context
        obj = context.object

        sk_flat = obj.shape_key_add(name='FLAT CARTON', from_mix=False)
        bpy.data.shape_keys["Key"].key_blocks["FLAT CARTON"].lock_shape = True
        obj.data.shape_keys.use_relative = True
        bpy.context.object.active_shape_key_index = 1


        sk_fold = obj.shape_key_add(name='FOLDED', from_mix = False)


        return {'FINISHED'}


class OBJECT_OT_select_project(bpy.types.Operator):
    """Project through Die Camera to Align Texture to Reference"""
    bl_idname = "object.select_project"
    bl_label = "Project From View"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.uv.project_from_view(camera_bounds=True,
                                     correct_aspect=False,
                                     scale_to_bounds=False)

        return {'FINISHED'}


class OBJECT_OT_center_object(bpy.types.Operator):
    """Snaps cursor and Selected Object to World Center"""
    bl_idname = "object.center_object"
    bl_label = "Center Object to World"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # cursor to world origin
        bpy.ops.view3d.snap_cursor_to_center()
        # selected object origin to geometry
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        return {'FINISHED'}


class SCENE_OT_scene_pivot(bpy.types.Operator):
    """Toggle Pivot between Cursor and Median Point in 3D View"""
    bl_idname = "scene.pivot"
    bl_label = "Set Pivot Toggle"

    def execute(self, context):
        scene = context.scene

        #pivot = bpy.context.scene.tool_settings.transform_pivot_point
        if bpy.context.scene.tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        elif bpy.context.scene.tool_settings.transform_pivot_point == 'CURSOR':
            bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'
        else:
            bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'

        return {'FINISHED'}


class OBJECT_OT_cardboard(bpy.types.Operator):
    """Set A Cardboard Solidify Ready for Material Index 1 and an Edge Split"""
    bl_idname = "object.cardboard"
    bl_label = "Set Cardboard Thickness and Material"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        scene = context.scene

        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = 0.000575158
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        bpy.context.object.modifiers["Solidify"].material_offset = 1
        bpy.context.object.modifiers["Solidify"].material_offset_rim = 1
        
        #edge split as well
        bpy.ops.object.modifier_add(type='EDGE_SPLIT')
        bpy.ops.object.shade_smooth()



        return {'FINISHED'}


class OBJECT_OT_Cameraview_model(bpy.types.Operator):
    """Set up Camera to match and follow Dieline"""
    bl_idname = "image.cameraview_model"
    bl_label = "Camera View Model"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        obj = context.active_object
        A = obj is not None
        if A:
            B = obj.type == 'MESH'
            return B

    def execute(self, context):
        scene = context.scene
        # toggle on/off textpaint
        obj = context.active_object

        # save selected plane by rename
        bpy.context.object.name = "ref_dieline_proxy"
        # variable to get image texture dimensions - thanks to Mutant Bob \
        # http://blender.stackexchange.com/users/660/mutant-bob
        # select_mat = bpy.context.active_object.data.materials[0]
        # .texture_slots[0].texture.image.size[:]
        # select_mat = []

        for ob in bpy.context.scene.objects:
            for s in ob.material_slots:
                if s.material and s.material.use_nodes:
                    for n in s.material.node_tree.nodes:
                        if n.type == 'TEX_IMAGE':
                            select_mat = n.image.size[:]
                            # print(obj.name,'uses',n.image.name,
                            # 'saved at',n.image.filepath)

        # add camera
        bpy.ops.object.camera_add(enter_editmode=False,
                                  align='VIEW',
                                  location=(0, 0, 0),
                                  rotation=(0, -0, 0))

        # ratio full
        bpy.context.scene.render.resolution_percentage = 100

        # name it
        bpy.context.object.name = "Dieline Camera View"

        # switch to camera view
        bpy.ops.view3d.object_as_camera()

        # ortho view on current camera
        bpy.context.object.data.type = 'ORTHO'
        # move cam up in Z by 1 unit
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

        # switch on composition guides for use in cameraview paint

        bpy.context.object.data.show_composition_center = True

        # found on net Atom wrote this simple script

        # image_index = 0

        rnd = bpy.data.scenes[0].render
        rnd.resolution_x, rnd.resolution_y = select_mat
        # bpy.context.object.data.ortho_scale = orthoscale

        rndx = rnd.resolution_x
        rndy = rnd.resolution_y
        # orthoscale = ((rndx - rndy)/rndy)+1

        if rndx >= rndy:
            orthoscale = ((rndx - rndy) / rndy) + 1

        elif rndx < rndy:
            orthoscale = 1

        # set to orthographic
        bpy.context.object.data.ortho_scale = orthoscale        
        
        # need to make "ref_dieline_proxy" Parent of "Dieline Camera View"
        # then no matter what rotation the ref dieline is, the camera follows
        # Names of the objects
        child_object_name = "Dieline Camera View"
        parent_object_name = "ref_dieline_proxy"

        # Get the objects
        child_object = bpy.data.objects.get(child_object_name)
        parent_object = bpy.data.objects.get(parent_object_name)

        # Check if both objects exist
        if child_object and parent_object:
            # Set the parent
            child_object.parent = parent_object
            print(f"'{child_object_name}' is now parented to '{parent_object_name}'.")
        else:
            print("One or both objects were not found.")
            
        bpy.context.object.data.show_name = True
        # hide camera itself
        bpy.ops.object.hide_view_set(unselected=False)
        bpy.context.selectable_objects

        # deselect camera
        bpy.ops.object.select_all(action='TOGGLE')
        # select plane
        bpy.ops.object.select_all(action='DESELECT')
        ob = bpy.data.objects["ref_dieline_proxy"]
        bpy.context.view_layer.objects.active = ob
        
        ###########   MUST USE FLAT AND TEXTURED VIEW
        bpy.context.space_data.shading.type = 'SOLID'
        bpy.context.space_data.shading.light = 'FLAT'
        bpy.context.space_data.shading.color_type = 'TEXTURE'

        


        

        return {'FINISHED'}


class CARTONVIZ_OT_add_basic(bpy.types.Operator):
    """Add Full Carton Base Shader Node Group to Selected Carton"""
    bl_idname = "cartonviz.addbasic_operator"
    bl_label = "Carton Shader Base"
    bl_options = { 'REGISTER', 'UNDO' }
    

    @classmethod
    def poll(self, context):
        obj = context.active_object
        A = obj is not None
        if A:
            B = obj.type == 'MESH'
            return B

    def execute(self, context):
        material_basic = bpy.data.materials.new(name="Carton Shader Base")
        material_basic.use_nodes = True

        bpy.context.object.active_material = material_basic

        principled_node = material_basic.node_tree.nodes.get('Principled BSDF')

        ###Principled Node Options
        principled_node.inputs[0].default_value = (1, 0, 0, 1)
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

        ###Color Mix Node named Multiply
        mix_node2 = material_basic.node_tree.nodes.new('ShaderNodeMixRGB')
        mix_node2.location = (-175, 100)
        mix_node2.label = ("Multiply Tex")
        mix_node2.inputs[0].default_value = 0.475
        mix_node2.blend_type = 'MULTIPLY'

        ###Mapping node for texture
        mapping = material_basic.node_tree.nodes.new('ShaderNodeMapping')
        mapping.location = (-175, 100)
        mapping.label = ("Mapping of Pattern")
        mapping.inputs[2].default_value[2] = 0.785398

        ###Brick Tex Node named Print Pattern
        brick = material_basic.node_tree.nodes.new('ShaderNodeTexBrick')
        brick.location = (-75, 100)
        brick.offset_frequency = 1
        brick.squash_frequency = 24
        brick.inputs[3].default_value = (0, 0, 0, 0)
        brick.inputs[4].default_value = 800
        brick.inputs[7].default_value = -0.680
        brick.inputs[9].default_value = 0.50

        #####LINKING
        link = material_basic.node_tree.links.new
        link(dieline_node.outputs[0], mix_node.inputs[1])
        link(colormap_node.outputs[0], mix_node.inputs[2])
        link(mix_node.outputs[0], mix_node2.inputs[1])
        link(bumpmap_node.outputs[0], bump_node.inputs[2])
        link(bump_node.outputs[0], principled_node.inputs[22])

        link(uv_node.outputs[0], dieline_node.inputs[0])
        link(uv_node.outputs[0], colormap_node.inputs[0])
        link(uv_node.outputs[0], bumpmap_node.inputs[0])
        link(uv_node.outputs[0], mapping.inputs[0])
        link(mapping.outputs[0], brick.inputs[0])
        link(brick.outputs[0], mix_node2.inputs[2])
        link(mix_node2.outputs[0], principled_node.inputs[0])

        return {'FINISHED'}


class CARTONVIZ_OT_add_fiberboard(bpy.types.Operator):
    """Applies a Procedural Fiberboard Texture to Solidy Surface"""    
    bl_idname = "cartonviz.add_fiberboard"
    bl_label = "Carton Fiberboard Shader"
    bl_options = { 'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        obj = context.active_object
        A = obj is not None
        if A:
            B = obj.type == 'MESH'
            return B

    def execute(self, context):
        material_fiber = bpy.data.materials.new(name="Carton FiberBoard Shader")
        material_fiber.use_nodes = True
        bpy.ops.object.material_slot_add()

        bpy.context.object.active_material = material_fiber

        material_fiber.pass_index = 1

        # Principled Main Shader in Tree
        principled_node = material_fiber.node_tree.nodes.get('Principled BSDF')

        ###Principled Node Options for Fiberboard
        principled_node.inputs[0].default_value = (1, 1, 1, 1)
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

        ###noisegrave Tex Node       
        noise1 = material_fiber.node_tree.nodes.new('ShaderNodeTexNoise')
        noise1.location = (-700, 400)
        noise1.label = ("Breaking Pattern")
        noise1.noise_type = 'HYBRID_MULTIFRACTAL'
        noise1.inputs[2].default_value = 368.4
        noise1.inputs[3].default_value = 15
        noise1.inputs[4].default_value = 62.4
        noise1.inputs[5].default_value = 1.1

        ###Color Mix Node Mix
        mix = material_fiber.node_tree.nodes.new('ShaderNodeMixRGB')
        mix.location = (-500, 400)
        mix.blend_type = 'MIX'
        mix.label = ("Color Mix")
        mix.inputs[1].default_value = (0.0784733, 0.0723242, 0.0403656, 1)
        mix.inputs[2].default_value = (0.134364, 0.117563, 0.0779412, 1)

        ###noisegrave Tex Node       
        noise2 = material_fiber.node_tree.nodes.new('ShaderNodeTexNoise')
        noise2.location = (-800, 100)
        noise2.label = ("overlay Pattern")
        noise2.noise_type = 'FBM'
        noise2.inputs[2].default_value = 57.7
        noise2.inputs[3].default_value = 2.0
        noise2.inputs[4].default_value = 2.0
        noise2.inputs[5].default_value = 2.0

        ###Ramp for Overlay       
        ramp = material_fiber.node_tree.nodes.new('ShaderNodeValToRGB')
        ramp.location = (-700, 100)
        ramp.label = ("Spread of Overlay")
        ramp.color_ramp.elements[0].position = 0.5

        # ramp.elements[0].position = 0.513636

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

        link(texcoord.outputs[0], mapping.inputs[0])
        link(mapping.outputs[0], voronoi.inputs[0])
        link(mapping.outputs[0], noise2.inputs[0])
        link(voronoi.outputs[0], noise1.inputs[6])
        link(noise1.outputs[0], mix.inputs[0])
        link(mix.outputs[0], mult.inputs[1])
        link(noise2.outputs[0], ramp.inputs[0])
        link(ramp.outputs[0], invert.inputs[1])
        link(invert.outputs[0], mult.inputs[2])
        link(mult.outputs[0], color.inputs[1])
        link(color.outputs[0], principled_node.inputs[0])

        return {'FINISHED'}


class CARTONVIZ_OT_add_corrugate(bpy.types.Operator):
    """Applies a Procedural Corrugate Texture to Solidify Surface"""
    bl_idname = "cartonviz.add_corrugate"
    bl_label = "Corrugate Shader"    
    bl_options = { 'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        obj = context.active_object
        A = obj is not None
        if A:
            B = obj.type == 'MESH'
            return B

    def execute(self, context):
        material_corrugate = bpy.data.materials.new(
            name="Carton Cardboard Shader"
        )
        material_corrugate.use_nodes = True
        bpy.ops.object.material_slot_add()

        bpy.context.object.active_material = material_corrugate

        material_corrugate.pass_index = 1

        # Principled Main Shader in Tree
        principled_node = material_corrugate.node_tree.nodes.get('Principled BSDF')

        ###Principled Node Options for Fiberboard
        principled_node.inputs[0].default_value = (1, 1, 1, 1)
        # principled_node.inputs[9].default_value = (0.575)

        ###Tex Coordinate Node       
        texcoord = material_corrugate.node_tree.nodes.new('ShaderNodeTexCoord')
        texcoord.location = (-1400, 400)
        texcoord.label = ("Coordinate Control")

        ###Mapping Node       
        mapping = material_corrugate.node_tree.nodes.new('ShaderNodeMapping')
        mapping.location = (-1200, 400)
        mapping.label = ("Mapping Control")

        ###noisegrave Tex Node       
        noiseG = material_corrugate.node_tree.nodes.new('ShaderNodeTexNoise')
        noiseG.location = (-1000, 300)
        noiseG.label = ("Fine Detail")
        noiseG.noise_type = 'FBM'
        noiseG.inputs[2].default_value = 392.5
        noiseG.inputs[3].default_value = 4.7
        noiseG.inputs[4].default_value = 2.0
        noiseG.inputs[5].default_value = 21.6

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

        link(texcoord.outputs[0], mapping.inputs[0])
        link(mapping.outputs[0], noiseG.inputs[0])
        link(mapping.outputs[0], wave.inputs[0])
        link(noiseG.outputs[0], wave.inputs[6])
        link(wave.outputs[0], mix.inputs[0])
        link(wave.outputs[0], bump.inputs[2])
        link(mix.outputs[0], mult.inputs[1])
        link(mult.outputs[0], principled_node.inputs[0])
        link(bump.outputs[0], principled_node.inputs[22])

        return {'FINISHED'}


class CARTONVIZ_PT_main_panel(bpy.types.Panel):
    bl_label = "Carton Primitive Panel"
    bl_idname = "cartonviz_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Carton Viz"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Carton Building Starts Here")
        row = col.row(align=True)
        

        row1 = row.split(align=True)
        row1.scale_x = 0.50
        row1.scale_y = 1.25
        row1.operator("image.import_as_mesh_planes",
                      text="Load Dieline",
                      icon='MESH_GRID')
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        row2.operator("image.cameraview_model",
                      text="DieCam",
                      icon="OUTLINER_OB_CAMERA")
        row = col.row(align=True)
        row3 = row.split(align=True)
        row3.scale_x = 0.50
        row3.scale_y = 1.25
        
        row3.operator("cpv.create_cpv_scene",
                        text="New Scene",
                        icon='PREFERENCES')
        
        scunit = bpy.context.scene.unit_settings.system
        
        if scunit == 'METRIC':
            toggle = "Scene is Metric"
            scicon = "URL"
        elif scunit == 'IMPERIAL':
            toggle = "Scene is Imperial"
            scicon = "HOOK"

        
        row3.operator("scene.scene_unit",
                      text=toggle,
                      icon=scicon)
        
        

        col = layout.column()
        col.prop(mytool, "carton_enum_unit")
        row = layout.row()
        row.prop(mytool, "carton_obj_dimensions")
        row = layout.row()
        row.prop(mytool, "carton_obj_name")
        row.prop(mytool, "carton_obj_name_flag")
        col = layout.column()
        if not mytool.carton_obj_name_flag:
            obj_name = mytool.carton_obj_name
        else:
            s = Template(
                "${obj_name} ${x_dim} ${unit} x ${y_dim}\
                 ${unit} x ${z_dim} ${unit}"
            )
            if mytool.carton_enum_unit == "UN1":
                obj_name = s.substitute(
                    obj_name=mytool.carton_obj_name,
                    x_dim=mytool.carton_obj_dimensions[0],
                    unit="mm",
                    y_dim=mytool.carton_obj_dimensions[1],
                    z_dim=mytool.carton_obj_dimensions[2])
            else:
                obj_name = s.substitute(
                    obj_name=mytool.carton_obj_name,
                    x_dim=mytool.carton_obj_dimensions[0],
                    unit="IN",
                    y_dim=mytool.carton_obj_dimensions[1],
                    z_dim=mytool.carton_obj_dimensions[2])
        col.label(text=f"ex: {obj_name}")
        items = mytool.bl_rna.properties['carton_enum_objs'].enum_items
        enum = items[mytool.carton_enum_objs]
        col.prop(
            mytool,
            "carton_enum_objs",
            text="Object type",
            icon=enum.identifier)

        make_obj = col.operator(
            "cartonviz.myop_operator",
            text=enum.name,
            icon=enum.identifier)
        make_obj.item_type = enum.description

        make_obj.item_dimensions = mytool.carton_obj_dimensions
        make_obj.item_name = obj_name

        make_coll = col.operator("cartonviz.my_collection")
        make_coll.coll_name = obj_name

        box = layout.box()
        col = box.column(align=True)
        col.label(text="Extras for Modeling")
        row = layout.row()
        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        row3 = row.split(align=True)
        row3.operator("object.wire_draw",
                      text="Wire",
                      icon='MOD_SOLIDIFY')
                      
        if bpy.context.scene.tool_settings.transform_pivot_point == 'CURSOR':
            pivot = 'PIVOT_CURSOR'
        elif bpy.context.scene.tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            pivot = 'PIVOT_MEDIAN'
        else:
            pivot='ERROR'


        row3.operator("scene.pivot",
                      text="Pivot",
                      icon=pivot)

        row = layout.row()
        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        # row = row.split(align=False)
        row.operator("object.center_mirror",
                     text="Add Mirror",
                     icon='ORIENTATION_VIEW')
        row.operator("object.apply_xmirror",
                     text="XMirror",
                     icon='MOD_MIRROR')


def unit_conversion(context, item_dims):
    scene = context.scene
    mytool = scene.my_tool
    # divide by 2 since items are created based on radius dimensions
    # also variable for sphere is listed as radius but cube is listed as size
    item_dims = item_dims / 2

    # since the operation of bpy.ops.mesh.primitive_xx_add
    # is based on a 1 meter scale always
    # conversion is only based on the unit selection
    # in the enumerator property

    # metric to mm conversions (1m = 1000mm)
    if mytool.carton_enum_unit == 'UN1':
        item_dims = item_dims / 1000

    # imperial to IN conversions (1m = 39.36in)
    if mytool.carton_enum_unit == 'UN2':
        item_dims = item_dims / 39.36
    return item_dims


class CARTONVIZ_PT_CartonUVMapping(bpy.types.Panel):
    """Carton Mapping Tools"""
    bl_label = "Carton UV Mapping Tools"
    bl_idname = "cartonviz_PT_CartonMapping"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Carton Viz"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        box = layout.box()  # big buttons aligned
        col = box.column(align=True)
        col.label(text='Project Each Face for Mapping')

        row = col.row(align=True)
        row1 = row.split(align=True)
        row1.scale_x = 0.50
        row1.scale_y = 1.25
        row1.operator("object.unwrap_front", text="Front")
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        row2.operator("object.unwrap_back", text="Back")
        col = box.column(align=True)
        row1 = row.split(align=True)
        row1.scale_x = 0.50
        row1.scale_y = 1.25
        row1.operator("object.unwrap_top", text="Top")

        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        row2.operator("object.unwrap_bottom", text="Bottom")

        row = col.row(align=True)
        row1 = row.split(align=True)
        row1.scale_x = 0.50
        row1.scale_y = 1.25
        row1.operator("object.unwrap_left",
                      text="Left",
                      icon='PREV_KEYFRAME')

        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        row2.operator("object.unwrap_right",
                      text="Right",
                      icon='NEXT_KEYFRAME')
        row3 = row.split(align=True)
        row3.scale_x = 0.50
        row3.scale_y = 1.25
        row3.operator("object.select_project",
                      text="Flat Project",
                      icon='ZOOM_PREVIOUS')


class CARTONVIZ_PT_CartonFinishing(bpy.types.Panel):
    """Carton Finishing Tools"""
    bl_label = "Carton Finishing Tools"
    bl_idname = "cartonviz_PT_CartonFinishing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Carton Viz"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = context.object

        box = layout.box()  # big buttons aligned
        col = box.column(align=True)
        col.label(text='Presets for Prep of Final Products')

        row = col.row(align=True)

        row1 = row.split(align=True)
        row1.scale_x = 0.50
        row1.scale_y = 1.25
        row1.operator("object.center_object",
                      text="Center Object Origin",
                      icon='ANCHOR_CENTER')
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        # row2.operator("render.render")
        row2.operator("object.cardboard",
                      text="Cardboard Set",
                      icon='MOD_LINEART')

        row = col.row(align=True)
        row = layout.row()
        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        row1 = row.split(align=True)
        row1.operator("object.add_bevel",
                      text="Bevel",
                      icon='MESH_ICOSPHERE')
        row1.operator("cartonviz.addbasic_operator",
                      text="Base Shader",
                      icon='CON_FOLLOWTRACK')

        row = col.row(align=True)
        row = layout.row()
        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        row1 = row.split(align=True)
        row1.operator("cartonviz.add_fiberboard",
                      text="Fiberboard",
                      icon='MESH_GRID')
        row1.operator("cartonviz.add_corrugate",
                      text="Corrugate",
                      icon='ALIGN_JUSTIFY')

        

class CARTONVIZ_PT_SceneRendering(bpy.types.Panel):
    """Carton Rendering Tools"""
    bl_label = "Carton Rendering Tools"
    bl_idname = "cartonviz_PT_CartonRendering"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Carton Viz"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = context.object

        box = layout.box()  # big buttons aligned
        col = box.column(align=True)
        col.label(text='Magic Render Buttons ;)')

        row = col.row(align=True)

        row1 = row.split(align=True)
        row1.scale_x = 0.50
        row1.scale_y = 1.25
        

        renpercent = bpy.context.scene.render.resolution_percentage
        if renpercent == 50:
            row1.operator("scene.full_render",
                      text="Set Full Shot",
                      icon='OUTPUT')
        elif renpercent == 200:
            row1.operator("scene.preview_render",
                      text="Set Preview Snap",
                      icon='SCENE')
        else:
            row1.operator("scene.full_render",
                      text="Set Full Shot",
                      icon='OUTPUT')
        
        row = col.row(align=True)
        row = layout.row()
        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        row2 = row.split(align=True)   
        row2.operator("scene.pose_frames", 
                        text="Set Pose Frames",
                        icon='ARMATURE_DATA')
        row2.operator("scene.camera_targetrender", 
                        text="Set Camera & Target",
                        icon='RESTRICT_RENDER_OFF')
                            
        row = col.row(align=True)
        row = layout.row()
        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        row3 = row.split(align=True)
        row3.operator("render.render",
                      text="Render Shot",
                      icon='WORKSPACE')
        row3.operator("scene.playblast_fullrender",
                      text="Render Frames",
                      icon='RENDER_ANIMATION')



classes = [
    CARTONVIZ_PG_add_object_helper,
    CARTONVIZ_PT_main_panel,
    CARTONVIZ_OT_AddStart,
    CARTONVIZ_OT_my_collection,
    SCENE_OT_scene_unit,
    OBJECT_OT_front_mapping,
    OBJECT_OT_back_mapping,
    OBJECT_OT_top_mapping,
    OBJECT_OT_bottom_mapping,
    OBJECT_OT_left_mapping,
    OBJECT_OT_right_mapping,
    OBJECT_OT_add_bevel,
    CARTONVIZ_PT_CartonUVMapping,
    CARTONVIZ_PT_CartonFinishing,
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
    CARTONVIZ_OT_add_corrugate,
    SCENE_OT_preview_render,
    SCENE_OT_full_render,
    SCENE_OT_pose_frames,
    SCENE_OT_playblast_fullrender,
    SCENE_OT_camera_targetrender,
    CARTONVIZ_PT_SceneRendering,
    SCENE_OT_CartonScene
    
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(
        type=CARTONVIZ_PG_add_object_helper)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
