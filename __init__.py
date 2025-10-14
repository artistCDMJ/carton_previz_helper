#_________________head and license
import bpy
from string import Template
from mathutils import Vector
import bmesh

from bpy.types import Panel, Operator, PropertyGroup
from bpy.props import FloatProperty, PointerProperty, EnumProperty, IntProperty, BoolProperty

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
           "version": (3, 50, 7),
           "blender": (4, 5, 1),
           "location": "N-Panel > Carton Viz",
           "description": "CDMJ In-House Carton PreViz Helper Tool",
           "warning": "",
           "category": "Object"}

#______________Functions

# ---------- Helper ----------
def get_image_from_object(obj):
    if obj and obj.type == 'MESH':
        for mat in obj.data.materials:
            if mat and mat.node_tree:
                for node in mat.node_tree.nodes:
                    if node.type == 'TEX_IMAGE' and node.image:
                        return node.image
    return None


def get_image_from_object(obj):
    """Get the first image texture from the object's material slots."""
    if obj.type != 'MESH':
        return None
    for mat in obj.data.materials:
        if mat and mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.type == 'TEX_IMAGE' and node.image:
                    return node.image
    return None



#_______________________Property Type

class CartonCADMirrorProperties(PropertyGroup):
    mirror_axis: EnumProperty(
        name="Axis",
        description="Choose mirror axis",
        items=[
            ('X', "X", "Mirror across X axis"),
            ('Y', "Y", "Mirror across Y axis"),
            ('Z', "Z", "Mirror across Z axis")
        ],
        default='X'
    )
    
##____________________DPI_CORRECTION
# ---------- Property Group ----------
class DPIScalerProperties(bpy.types.PropertyGroup):
    dpi: bpy.props.IntProperty(
        name="DPI",
        default=150,
        min=1,
        description="Dots per inch for scaling image plane"
    )

#_____________________set measure apply conditional
class SELProperties(PropertyGroup):
    edge_length: FloatProperty(
        name="Edge Length",
        description="Target length for selected edge",
        default=1.0,
        min=0.0,
        subtype='DISTANCE'
    )

    constrain_to_cursor: bpy.props.BoolProperty(
        name="Constrain to Cursor",
        description="Anchor edge to the vertex closest to the 3D cursor",
        default=False
    )

    bevel_width: FloatProperty(
        name="Bevel Width",
        description="Bevel width for selected vertices",
        default=0.01,
        min=0.0,
        subtype='DISTANCE'
    )

    bevel_segments: bpy.props.IntProperty(
        name="Segments",
        description="Number of segments in vertex bevel",
        default=2,
        min=1,
        max=12
    )
    edge_orientation: EnumProperty(
        name="Orientation",
        description="Direction to align the edge primitive",
        items=[
            ('X', "X Axis", "Align edge along the X axis"),
            ('Y', "Y Axis", "Align edge along the Y axis"),
        ],
        default='X'
    )

    plane_width: FloatProperty(
        name="Plane Width",
        description="Width (X) of the new plane",
        default=1.0,
        min=0.0,
        subtype='DISTANCE'
    )

    plane_height: FloatProperty(
        name="Plane Height",
        description="Height (Y) of the new plane",
        default=1.0,
        min=0.0,
        subtype='DISTANCE'
    )
    join_plane_to_active: BoolProperty(
        name="Join to Active Object",
        description="Join the new plane to the currently edited object",
        default=True
    )

class KnockoutProperties(bpy.types.PropertyGroup):
    cutter_shape: EnumProperty(
        name="Shape",
        items=[
            ("CIRCLE", "Circle", "Circle profile cutter"),
            ("PLANE", "Plane", "Flat plane cutter"),
        ],
        default="CIRCLE"
    )

    cutter_size: FloatProperty(
        name="Size",
        description="Size of the cutter object",
        default=0.02,
        min=0.001,
        subtype='DISTANCE'
    )



#_______________________Operator Type

class CARTON_OT_snap_cursor_set_pivot(Operator):
    """Snap Cursor to Selection and Set Pivot"""
    bl_idname = "carton.snap_cursor_set_pivot"
    bl_label = "Snap Cursor & Set Pivot"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'EDIT' and
                context.object.type == 'MESH')

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        self.report({'INFO'}, "Cursor snapped to selection and pivot set to cursor.")
        return {'FINISHED'}


class CARTON_OT_mirror_to_cursor(Operator):
    """Duplicate and Mirror Selection on Chosen Axis"""
    bl_idname = "carton.mirror_to_cursor"
    bl_label = "Mirror to Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'EDIT' and
                context.object.type == 'MESH')

    def execute(self, context):
        props = context.scene.carton_cad_mirror_props
        axis = props.mirror_axis

        # Duplicate the selected mesh
        bpy.ops.mesh.duplicate_move()
        
        # Scale on chosen axis by -1
        scale_dict = {'X': (-1, 1, 1), 'Y': (1, -1, 1), 'Z': (1, 1, -1)}
        scale = scale_dict.get(axis, (1, 1, 1))
        bpy.ops.transform.resize(value=scale)
        
        self.report({'INFO'}, f"Mirrored selection on {axis} axis.")
        return {'FINISHED'}
    
# ---------- Operator ----------
class OBJECT_OT_scale_image_plane(bpy.types.Operator):
    bl_idname = "object.scale_image_plane_dpi"
    bl_label = "Scale Image Plane to DPI"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        dpi = context.scene.dpi_scaler_props.dpi
        scene = context.scene
        unit_system = scene.unit_settings.system
        scale_length = scene.unit_settings.scale_length

        image = get_image_from_object(obj)
        if not image:
            self.report({'ERROR'}, "Active object has no image texture")
            return {'CANCELLED'}

        width_px, height_px = image.size

        # Physical size in inches
        width_in = width_px / dpi
        height_in = height_px / dpi

        # Convert to BU depending on unit system
        if unit_system == 'IMPERIAL':
            inches_per_BU = scale_length * 39.3701
            target_width_BU = width_in / inches_per_BU
            target_height_BU = height_in / inches_per_BU
        elif unit_system == 'METRIC':
            mm_per_BU = scale_length * 1000
            target_width_BU = (width_in * 25.4) / mm_per_BU
            target_height_BU = (height_in * 25.4) / mm_per_BU
        else:
            target_width_BU = (width_in * 0.0254) / scale_length
            target_height_BU = (height_in * 0.0254) / scale_length

        # Apply dimensions directly
        obj.dimensions = (target_width_BU, target_height_BU, obj.dimensions.z)

        self.report({'INFO'}, f"Scaled to {width_in:.2f} x {height_in:.2f} real units")
        return {'FINISHED'}




#_________________________classes from set measure apply
class MESH_OT_add_scaled_plane(bpy.types.Operator):
    bl_idname = "mesh.add_scaled_plane"
    bl_label = "Add Scaled Plane"
    bl_description = "Add a plane with specified X/Y dimensions and set origin to lower-left"
    bl_options = {'REGISTER', 'UNDO'}

    join_to_edit_object: bpy.props.BoolProperty(
        name="Join to Active",
        description="Join new plane to the current object in Edit Mode",
        default=True
    )

    def execute(self, context):
        import bmesh
        from mathutils import Vector

        props = context.scene.sel_props
        width = props.plane_width
        height = props.plane_height
        join_to_edit = context.scene.sel_props.join_plane_to_active

        props = context.scene.sel_props
        join_to_edit = props.join_plane_to_active

        original_obj = context.edit_object

        # Only require Edit Mode if we plan to join to an existing mesh
        if join_to_edit:
            if original_obj is None or original_obj.type != 'MESH':
                self.report({'ERROR'}, "Must be in Edit Mode on a mesh object.")
                return {'CANCELLED'}

        if context.active_object and context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        # Switch to Object Mode before creating new mesh
        # bpy.ops.object.mode_set(mode='OBJECT')

        # Add plane at cursor location
        bpy.ops.mesh.primitive_plane_add(location=context.scene.cursor.location)
        plane_obj = context.active_object

        # Scale to desired size
        plane_obj.scale = (width / 2.0, height / 2.0, 1)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

        # Enter Edit Mode on the new plane to adjust origin
        bpy.ops.object.mode_set(mode='EDIT')
        bm = bmesh.from_edit_mesh(plane_obj.data)
        bm.verts.ensure_lookup_table()
        lower_left = min(bm.verts, key=lambda v: (v.co.x, v.co.y))
        origin_pos = lower_left.co.copy()
        bpy.ops.object.mode_set(mode='OBJECT')

        # Offset so origin aligns to lower-left
        plane_obj.location += plane_obj.matrix_world.to_3x3() @ origin_pos
        for v in plane_obj.data.vertices:
            v.co -= origin_pos

        # Snap to cursor
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        if join_to_edit:
            # Join new plane to original object
            plane_obj.select_set(True)
            original_obj.select_set(True)
            context.view_layer.objects.active = original_obj
            bpy.ops.object.join()

            # Return to Edit Mode
            bpy.ops.object.mode_set(mode='EDIT')

        return {'FINISHED'}


class MESH_OT_add_edge_to_edit_mesh(bpy.types.Operator):
    bl_idname = "mesh.add_edge_to_edit_mesh"
    bl_label = "Add Edge to Current Mesh"
    bl_description = "Adds an edge to the current object in Edit Mode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.object

        if obj.mode != 'EDIT' or obj.type != 'MESH':
            self.report({'WARNING'}, "Must be in Edit Mode on a mesh object.")
            return {'CANCELLED'}

        props = context.scene.sel_props
        length = props.edge_length
        axis = props.edge_orientation

        if axis == 'X':
            dir = Vector((1, 0, 0))
        elif axis == 'Y':
            dir = Vector((0, 1, 0))
        else:
            dir = Vector((1, 0, 0))

        # Use the 3D cursor as insertion point
        base = context.scene.cursor.location
        offset = dir.normalized() * length

        bm = bmesh.from_edit_mesh(obj.data)
        v1 = bm.verts.new(base)
        v2 = bm.verts.new(base + offset)
        bm.edges.new((v1, v2))

        bm.normal_update()
        bmesh.update_edit_mesh(obj.data, loop_triangles=False, destructive=False)

        return {'FINISHED'}


class MESH_OT_vertex_bevel(bpy.types.Operator):
    bl_idname = "mesh.vertex_bevel_custom"
    bl_label = "Vertex Bevel"
    bl_description = "Bevel Selected Vertex with Current Settings"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.sel_props

        # Perform vertex-only bevel on selected vertices
        bpy.ops.mesh.bevel(
            offset=props.bevel_width,
            segments=props.bevel_segments,
            affect='VERTICES',  # <- Correct keyword
            offset_pct=0,  # <- Disable percentage mode
            profile=0.5  # Optional: standard profile
        )

        return {'FINISHED'}


class MESH_OT_set_edge_length(Operator):
    bl_idname = "mesh.set_edge_length"
    bl_label = "Set Edge Length"
    bl_description = "Set the Edge(s) to the Current Length"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (
                context.object is not None and
                context.object.type == 'MESH' and
                context.mode == 'EDIT_MESH'
        )

    def execute(self, context):
        obj = context.object
        if obj.mode != 'EDIT':
            self.report({'WARNING'}, "Must be in Edit mode")
            return {'CANCELLED'}

        bm = bmesh.from_edit_mesh(obj.data)
        props = context.scene.sel_props
        target_length = props.edge_length
        constrain = props.constrain_to_cursor
        cursor_location = context.scene.cursor.location

        selected_edges = [e for e in bm.edges if e.select]

        if not selected_edges:
            self.report({'WARNING'}, "No edges selected")
            return {'CANCELLED'}

        for edge in selected_edges:
            if len(edge.verts) != 2:
                continue

            v1, v2 = edge.verts
            edge_vec = v2.co - v1.co
            current_length = edge_vec.length

            if current_length == 0:
                self.report({'WARNING'}, "Skipping zero-length edge")
                continue

            direction = edge_vec.normalized()

            if constrain:
                # Constrain one end to the vertex closest to the 3D cursor
                dist_v1 = (v1.co - cursor_location).length
                dist_v2 = (v2.co - cursor_location).length

                if dist_v1 <= dist_v2:
                    anchor = v1
                    moving = v2
                    sign = 1
                else:
                    anchor = v2
                    moving = v1
                    sign = -1

                moving.co = anchor.co + direction * target_length * sign
            else:
                # Scale from midpoint
                center = (v1.co + v2.co) * 0.5
                offset = direction * (target_length * 0.5)
                v1.co = center - offset
                v2.co = center + offset

        bmesh.update_edit_mesh(obj.data)
        return {'FINISHED'}


class MESH_OT_apply_scale(Operator):
    bl_idname = "mesh.apply_scale"
    bl_label = "Apply Scale of Object"
    bl_description = "Apply Object Scale and Return to Edit Mode"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (
                context.object is not None and
                context.object.type == 'MESH' and
                context.mode == 'EDIT_MESH'
        )

    def execute(self, context):
        obj = context.object
        if obj.mode != 'EDIT':
            self.report({'WARNING'}, "Must be in Edit mode")
            return {'CANCELLED'}

        # Switch to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Apply scale
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

        # Switch back to Edit Mode
        bpy.ops.object.mode_set(mode='EDIT')

        return {'FINISHED'}


class MESH_OT_toggle_edge_length(Operator):
    bl_idname = "mesh.toggle_edge"
    bl_label = "Toggle Edge Length Display"
    bl_description = "Toggle Draw Edge Length On or Off"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (
                context.object is not None and
                context.object.type == 'MESH' and
                context.mode == 'EDIT_MESH'
        )

    def execute(self, context):
        obj = context.object
        if obj.mode != 'EDIT':
            self.report({'WARNING'}, "Must be in Edit mode")
            return {'CANCELLED'}

        if bpy.context.space_data.overlay.show_extra_edge_length == False:
            bpy.context.space_data.overlay.show_extra_edge_length = True

        else:
            bpy.context.space_data.overlay.show_extra_edge_length = False

        return {'FINISHED'}

class VIEW3D_OT_snap_cursor_to_selected(bpy.types.Operator):
    bl_idname = "view3d.snap_cursor_quick"
    bl_label = "Snap Cursor to Selected"
    bl_description = "Quickly snap 3D cursor to the Selection"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (
                context.object is not None and
                context.object.type == 'MESH' and
                context.mode == 'EDIT_MESH'
        )

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        return {'FINISHED'}


class VIEW3D_OT_metric_imperial_set(bpy.types.Operator):
    bl_idname = "view3d.metric_imperial_setup"
    bl_label = "Toggle Metric or Imperial UNITS"
    bl_description = "Set to MM or Imperial and Divisions"
    bl_options = {'REGISTER', 'UNDO'}

    # @classmethod
    # def poll(cls, context):
    # return (
    # context.object is not None and
    # context.object.type == 'MESH' and
    # context.mode == 'EDIT_MESH'
    # )

    def execute(self, context):

        # bpy.context.space_data.context = 'SCENE'

        if bpy.context.scene.unit_settings.length_unit == 'MILLIMETERS':
            bpy.context.scene.unit_settings.system = 'IMPERIAL'
            bpy.context.scene.unit_settings.length_unit = 'INCHES'
            bpy.context.space_data.overlay.grid_subdivisions = 12
            bpy.context.scene.unit_settings.scale_length = 0.0833


        else:
            bpy.context.scene.unit_settings.system = 'METRIC'
            bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
            bpy.context.space_data.overlay.grid_subdivisions = 10
            bpy.context.space_data.overlay.grid_scale = 0.1

            bpy.context.scene.unit_settings.scale_length = 0.001

        bpy.context.scene.tool_settings.use_snap = True
        bpy.context.scene.tool_settings.snap_elements_base = {'GRID'}

        return {'FINISHED'}


class VIEW3D_OT_toggle_wire(bpy.types.Operator):
    bl_idname = "view3d.toggle_wire"
    bl_label = "Toggle Wireframe Draw"
    bl_description = "Toggle Draw Wireframe, Allows preview of edges in Object mode for Tracing"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.show_wire == True:
            bpy.context.object.show_wire = False
        else:
            bpy.context.object.show_wire = True

        return {'FINISHED'}


# ------------------------------------
# Cutter Generator
# ------------------------------------
class OBJECT_OT_generate_cutter_instances(bpy.types.Operator):
    bl_idname = "object.generate_cutter_instances"
    bl_label = "Generate Cutter Instances"
    bl_description = "Place cutter objects at selected vertices"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.knockout_props
        cutter_shape = props.cutter_shape
        cutter_size = props.cutter_size

        obj = context.object

        if not obj or obj.type != 'MESH' or obj.mode != 'EDIT':
            self.report({'ERROR'}, "Must be in Edit Mode on a mesh object.")
            return {'CANCELLED'}

        bm = bmesh.from_edit_mesh(obj.data)
        bm.verts.ensure_lookup_table()
        # Cache vertex positions before exiting Edit Mode
        selected_positions = [obj.matrix_world @ v.co.copy() for v in bm.verts if v.select]

        if not selected_positions:
            self.report({'WARNING'}, "No vertices selected.")
            return {'CANCELLED'}

        bpy.ops.object.mode_set(mode='OBJECT')  # Now safe

        for world_pos in selected_positions:
            cutter = self.create_cutter_object(context, shape=cutter_shape, size=cutter_size)
            cutter.location = world_pos

        return {'FINISHED'}

    def create_cutter_object(self, context, shape="CIRCLE", size=0.02):
        if shape == "CIRCLE":
            bpy.ops.mesh.primitive_circle_add(
                vertices=32,
                radius=size * 0.5,
                location=(0, 0, 0),
                fill_type='NOTHING'  # ✅ Must be 'NOTHING' to keep as edge-only
            )
        elif shape == "PLANE":
            bpy.ops.mesh.primitive_grid_add(  # ✅ Use grid to ensure edge-only
                size=size,
                x_subdivisions=2,
                y_subdivisions=2,
                location=(0, 0, 0)
            )

        cutter_obj = context.active_object
        cutter_obj.name = f"Cutter_{shape}"
        return cutter_obj


class OBJECT_OT_knife_project_cutters(bpy.types.Operator):
    bl_idname = "object.knife_project_cutters"
    bl_label = "Knife Project from Cutters"
    bl_description = "Use Cutter_ objects to project into the active object using Knife Project"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        view = context.space_data.region_3d

        if view.view_perspective != 'ORTHO':
            self.report({'WARNING'}, "Knife Project requires orthographic view.")
            return {'CANCELLED'}

        main_obj = context.active_object
        if not main_obj or main_obj.type != 'MESH':
            self.report({'ERROR'}, "Active object must be a mesh (target for projection).")
            return {'CANCELLED'}

        # Get all valid cutter objects (by name prefix)
        view_layer = context.view_layer
        cutter_objs = [
            obj for obj in view_layer.objects
            if obj.name.startswith("Cutter_")
               and obj.type == 'MESH'
               and not obj.hide_get()
               and not obj.hide_viewport
        ]

        if not cutter_objs:
            self.report({'WARNING'}, "No cutter objects named 'Cutter_' found in the scene.")
            return {'CANCELLED'}

        # should have already selected main object to work
        # Select main object and make it active
        main_obj.select_set(True)
        context.view_layer.objects.active = main_obj

        # Enter Edit Mode on main object, select all geometry
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')

        # Select cutters
        for cutter in cutter_objs:
            cutter.select_set(True)

        try:
            # Attempt Knife Project
            bpy.ops.mesh.knife_project(cut_through=False)
        except RuntimeError as e:
            self.report({'ERROR'}, f"Knife Project failed: {str(e)}")
            bpy.ops.object.mode_set(mode='OBJECT')
            return {'CANCELLED'}

        cutter_collection = bpy.data.collections.get("Cutters")
        if not cutter_collection:
            cutter_collection = bpy.data.collections.new("Cutters")
            context.scene.collection.children.link(cutter_collection)

        for cutter in cutter_objs:
            # Remove from all existing collections
            for collection in cutter.users_collection:
                collection.objects.unlink(cutter)

            # Link to 'Cutters' collection
            if cutter.name not in cutter_collection.objects:
                cutter_collection.objects.link(cutter)

        return {'FINISHED'}


class OBJECT_OT_tag_as_cutter(bpy.types.Operator):
    bl_idname = "object.tag_as_cutter"
    bl_label = "Tag Object as Cutter"
    bl_description = "Rename selected object(s) with 'Cutter_' prefix"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_objs = context.selected_objects
        if not selected_objs:
            self.report({'WARNING'}, "No object selected.")
            return {'CANCELLED'}

        for obj in selected_objs:
            if not obj.name.startswith("Cutter_"):
                obj.name = "Cutter_" + obj.name

        return {'FINISHED'}
#_______________________end of classes from SMA



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

        # Store selection before creating scene
        selected_objects = context.selected_objects.copy()

        # Create new scene
        bpy.ops.scene.new(type='NEW')
        new_scene = context.scene
        new_scene.name = _name

        # Link selected objects into the new scene
        if selected_objects:
            for obj in selected_objects:
                if obj.name not in new_scene.collection.objects:
                    new_scene.collection.objects.link(obj)

        # Set to top view
        bpy.ops.view3d.view_axis(type='TOP', align_active=True)
        
        # Set to Cycles with desired settings
        new_scene.render.engine = 'CYCLES'
        new_scene.display_settings.display_device = 'sRGB'
        new_scene.view_settings.view_transform = 'Filmic'
        new_scene.view_settings.look = 'Very High Contrast'

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
        bpy.context.object.modifiers["Solidify"].thickness = 0.00575158
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        bpy.context.object.modifiers["Solidify"].material_offset = 1
        bpy.context.object.modifiers["Solidify"].material_offset_rim = 1
        
        #edge split as well
        bpy.ops.object.modifier_add(type='EDGE_SPLIT')
        bpy.ops.object.shade_smooth()



        return {'FINISHED'}


class OBJECT_OT_Cameraview_model(bpy.types.Operator):
    """Set up Camera to match and follow selected image plane"""
    bl_idname = "image.cameraview_model"
    bl_label = "Camera View Model"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj is not None and obj.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        obj = context.active_object

        # Rename selected plane
        obj.name = "ref_dieline_proxy"

        # Get image texture from the object
        image = get_image_from_object(obj)
        if not image:
            self.report({'ERROR'}, "Selected object has no image texture.")
            return {'CANCELLED'}

        # Get pixel dimensions from image
        px_width, px_height = image.size

        # Get actual world dimensions from the scaled object
        width_world = obj.dimensions.x
        height_world = obj.dimensions.y

        # Add camera at world origin
        bpy.ops.object.camera_add(
            enter_editmode=False,
            align='VIEW',
            location=(0, 0, 0),
            rotation=(0, 0, 0)
        )
        cam = context.active_object
        cam.name = "Dieline Camera View"

        # Switch to camera view
        bpy.ops.view3d.object_as_camera()

        # Set camera to orthographic
        cam.data.type = 'ORTHO'

        # Position camera 1 unit above plane (along Z)
        bpy.ops.transform.translate(
            value=(0, 0, 1),
            orient_type='GLOBAL',
            constraint_axis=(False, False, True)
        )

        # Match render resolution to image pixel size
        scene.render.resolution_percentage = 100
        scene.render.resolution_x = px_width
        scene.render.resolution_y = px_height

        # Set ortho scale to match plane dimensions
        # (Orthographic scale in Blender = full view width in world units)
        if px_width >= px_height:
            cam.data.ortho_scale = width_world
        else:
            cam.data.ortho_scale = height_world

        # Show composition guide
        cam.data.show_composition_center = True
        cam.data.show_name = True

        # Parent camera to the plane
        cam.parent = obj

        # Hide the camera in viewport
        bpy.ops.object.hide_view_set(unselected=False)

        # Reselect the plane
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        context.view_layer.objects.active = obj

        # Set shading to Flat + Textured
        area = next(
            (area for area in context.screen.areas if area.type == 'VIEW_3D'), None
        )
        if area:
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.shading.type = 'SOLID'
                    space.shading.light = 'FLAT'
                    space.shading.color_type = 'TEXTURE'

        self.report({'INFO'}, f"Camera matched to {width_world:.2f} x {height_world:.2f} world units.")
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
        principled_node.inputs[1].default_value = (0.2)
        principled_node.inputs[2].default_value = (0.127)

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
        link(bumpmap_node.outputs[0], bump_node.inputs[3])
        link(bump_node.outputs[0], principled_node.inputs[5])

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
        principled_node.inputs[3].default_value = (0.575)

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
        #noise1.noise_type = 'HYBRID_MULTIFRACTAL'
        noise1.inputs[1].default_value = 368.4
        noise1.inputs[2].default_value = 15
        noise1.inputs[3].default_value = 62.4
        noise1.inputs[4].default_value = 1.1

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
        #noise2.noise_type = 'FBM'
        noise2.inputs[1].default_value = 57.7
        noise2.inputs[2].default_value = 2.0
        noise2.inputs[3].default_value = 2.0
        noise2.inputs[4].default_value = 2.0

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
        link(voronoi.outputs[0], noise1.inputs[5])
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
        #noiseG.noise_type = 'FBM'
        noiseG.inputs[1].default_value = 392.5
        noiseG.inputs[2].default_value = 4.7
        noiseG.inputs[3].default_value = 2.0
        noiseG.inputs[4].default_value = 21.6

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
        link(noiseG.outputs[0], wave.inputs[5])
        link(wave.outputs[0], mix.inputs[0])
        link(wave.outputs[0], bump.inputs[2])
        link(mix.outputs[0], mult.inputs[1])
        link(mult.outputs[0], principled_node.inputs[0])
        link(bump.outputs[0], principled_node.inputs[23])

        return {'FINISHED'}
###new ops
class OBJECT_OT_snap_and_realign(bpy.types.Operator):
    bl_idname = "object.snap_and_realign"
    bl_label = "Snap Cursor to Face and Realign Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object

        if obj is None or obj.type != 'MESH':
            self.report({'ERROR'}, "Active object must be a mesh")
            return {'CANCELLED'}

        if context.mode != 'EDIT_MESH':
            self.report({'ERROR'}, "Start in Edit Mode with a face selected")
            return {'CANCELLED'}

        # Step 1: Get selected face center in world coordinates
        bm = bmesh.from_edit_mesh(obj.data)
        bm.faces.ensure_lookup_table()
        selected_faces = [f for f in bm.faces if f.select]

        if not selected_faces:
            self.report({'ERROR'}, "No face selected")
            return {'CANCELLED'}

        face = selected_faces[0]
        face_center_local = face.calc_center_median()
        face_center_world = obj.matrix_world @ face_center_local

        # Step 2: Snap cursor to selected face center
        context.scene.cursor.location = face_center_world

        # Step 3: Switch to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Step 4: Set origin to cursor (face center)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        # Step 5: Move cursor to world origin
        context.scene.cursor.location = (0.0, 0.0, 0.0)

        # Step 6: Snap object to cursor
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        context.view_layer.objects.active = obj
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

        return {'FINISHED'}

class VIEW3D_PT_carton_creation(Panel):
    bl_label = "Carton Creation"
    bl_idname = "VIEW3D_PT_carton_creation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Carton Viz"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = context.object
        units = bpy.context.scene.unit_settings.system

        props = context.scene.sel_props
        tool_settings = context.tool_settings
        
        box = layout.box()  # big buttons aligned
        col = box.column(align=True)
        col.label(text='Initial Dieline to Camera/Scene')
        row = col.row(align=True)

        row1 = row.split(align=True)
        row1.scale_x = 0.50
        row1.scale_y = 1.25

        if units == 'METRIC':
            row1.operator("view3d.metric_imperial_setup",
                          text="Set Imperial",
                          icon='FULLSCREEN_EXIT')

        else:
            row1.operator("view3d.metric_imperial_setup",
                          text="Set Metric",
                          icon='FULLSCREEN_ENTER')
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

        box = layout.box()  # big buttons aligned
        col = box.column(align=True)
        col.label(text='Edge Settings')

        

        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        # row2.operator("render.render")

        if bpy.context.space_data.overlay.show_extra_edge_length == False:

            row2.operator("mesh.toggle_edge",
                          text="Edge Length",
                          icon='HIDE_OFF')
        else:
            row2.operator("mesh.toggle_edge",
                          text="Edge Length",
                          icon='HIDE_ON')

        row = col.row(align=True)
        row = layout.row()
        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        row1 = row.split(align=True)
        row1.prop(props, "edge_length")
        row1.operator("mesh.set_edge_length",
                      icon='FILE_ALIAS')

        row = col.row(align=True)
        row = layout.row()
        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        row1 = row.split(align=True)
        row1.prop(props, "constrain_to_cursor")
        row1.prop(tool_settings, "use_mesh_automerge",
                  text="Auto Merge",
                  toggle=False)

        

        box = layout.box()  # big buttons aligned
        col = box.column(align=True)
        col.label(text='Edge Primitive:')

        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        # row2.operator("render.render")
        row2.prop(props, "edge_orientation", text="Axis")
        row2.operator("mesh.add_edge_to_edit_mesh", text="Generate Edge")

        col.label(text="Plane Primitive:")
        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        row2.prop(props, "plane_width", text="Width")
        row2.prop(props, "plane_height", text="Height")
        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        # row2.operator("mesh.add_scaled_plane", icon='UV_ISLANDSEL')
        row2.prop(props, "join_plane_to_active")
        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25

        row2.operator("mesh.add_scaled_plane", icon='UV_ISLANDSEL')
        # op.join_to_edit_object = True
        
        col = layout.column()
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Extras for Modeling")
        row = layout.row()
        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        row = row.split(align=True)
        row.operator("object.wire_draw",
                      text="Wire Transparency",
                      icon='MOD_SOLIDIFY')
        
        row = row.split(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        
        row.operator("view3d.toggle_wire",
                      text="Toggle Show Edges",
                      icon='MESH_GRID')
        row = layout.row()
        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        row = row.split(align=True)
        row.operator("mesh.apply_scale",
                      text="Apply Scale",
                      icon='FILE_3D')
        
        row.scale_x = 0.50
        row.scale_y = 1.25
        row = row.split(align=True)
        row.operator("object.snap_and_realign",
                     text="Snap to World",
                     icon='WORLD_DATA')
                      
        if bpy.context.scene.tool_settings.transform_pivot_point == 'CURSOR':
            pivot = 'PIVOT_CURSOR'
        elif bpy.context.scene.tool_settings.transform_pivot_point == 'MEDIAN_POINT':
            pivot = 'PIVOT_MEDIAN'
        else:
            pivot='ERROR'

        row = col.row(align=True)
        row.scale_x = 0.50
        row.scale_y = 1.25
        row = row.split(align=True)
        row.operator("scene.pivot",
                      text="Pivot Cursor/Median",
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
  
        box = layout.box()  # big buttons aligned
        col = box.column(align=True)
        col.label(text='Bevel Corner Vertex')

        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        # row2.operator("render.render")
        row2.prop(props, "bevel_width")
        row2.prop(props, "bevel_segments")

        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        # row2.operator("render.render")
        row2.operator("mesh.vertex_bevel_custom",
                      icon='MOD_BEVEL')
                      
# Mirror to Line CAD imitation
class CARTON_PT_mirror_panel(Panel):
    bl_label = "Carton CAD Mirror"
    #bl_idname = "CARTON_PT_mirror_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Carton Viz"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        props = context.scene.carton_cad_mirror_props
        obj = context.object

        layout.label(text="Mirror Axis:")
        row = layout.row(align=True)
        row.prop(props, "mirror_axis", expand=True)

        # Snap cursor and set pivot
        col = layout.column(align=True)
        col.enabled = obj and obj.mode == 'EDIT'
        col.operator("carton.snap_cursor_set_pivot", icon='PIVOT_CURSOR')

        # Mirror button
        col = layout.column(align=True)
        col.enabled = obj and obj.mode == 'EDIT'
        col.operator("carton.mirror_to_cursor", icon='MOD_MIRROR')

# ---------- Panel ----------
class VIEW3D_PT_dpi_scaler(bpy.types.Panel):
    bl_label = "Image Plane DPI Scaler"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Carton Viz"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        props = scene.dpi_scaler_props
        obj = context.active_object
        unit_system = scene.unit_settings.system
        scale_length = scene.unit_settings.scale_length

        layout.prop(props, "dpi")

        if obj and obj.type == 'MESH':
            image = get_image_from_object(obj)
            if image:
                width_px, height_px = image.size
                dpi = props.dpi

                width_in = width_px / dpi
                height_in = height_px / dpi

                if unit_system == 'IMPERIAL':
                    inches_per_BU = scale_length * 39.3701
                    target_width_BU = width_in / inches_per_BU
                    target_height_BU = height_in / inches_per_BU
                    layout.label(text=f"Target Size: {width_in:.2f}\" x {height_in:.2f}\"")
                elif unit_system == 'METRIC':
                    mm_per_BU = scale_length * 1000
                    target_width_BU = (width_in * 25.4) / mm_per_BU
                    target_height_BU = (height_in * 25.4) / mm_per_BU
                    layout.label(text=f"Target Size: {width_in*25.4:.2f}mm x {height_in*25.4:.2f}mm")
                else:
                    target_width_BU = (width_in * 0.0254) / scale_length
                    target_height_BU = (height_in * 0.0254) / scale_length
                    layout.label(text=f"Target Size: {width_in*25.4:.2f}mm x {height_in*25.4:.2f}mm")

                layout.label(text=f"Blender Units: {target_width_BU:.3f} x {target_height_BU:.3f}")
                layout.operator("object.scale_image_plane_dpi", text="Apply Scaling")
            else:
                layout.label(text="No image found on selected object.")
        else:
            layout.label(text="Select an image plane.")

class VIEW3D_PT_knockout_panel(bpy.types.Panel):
    bl_label = "Knock-Out Cutter"
    bl_idname = "VIEW3D_PT_knockout_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Carton Viz"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        props = context.scene.knockout_props

        box = layout.box()  # big buttons aligned
        col = box.column(align=True)
        # col.label(text='Bevel Corner Vertex')
        row = layout.row()
        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25

        row2.prop(props, "cutter_shape")
        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        row2.prop(props, "cutter_size")
        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        row2.operator("object.generate_cutter_instances",
                      text="Cutter(s) at Selected Vertex",
                      icon='LATTICE_DATA')

        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25

        row2.operator("object.knife_project_cutters",
                      text="Project Cutters",
                      icon='MOD_BOOLEAN')

        row = col.row(align=True)
        row2 = row.split(align=True)
        row2.scale_x = 0.50
        row2.scale_y = 1.25
        row2.operator("object.tag_as_cutter", icon='FONT_DATA')







class CARTONVIZ_PT_CartonFinishing(bpy.types.Panel):
    """Carton Finishing"""
    bl_label = "Carton Finishing"
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
        
        row3 = row.split(align=True)
        row3.scale_x = 0.50
        row3.scale_y = 1.25
        row3.operator("object.select_project",
                      text="Flat Project through Diecam",
                      icon='ZOOM_PREVIOUS')
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
    """Carton Rendering"""
    bl_label = "Carton Rendering"
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


#_______________________register and class
classes = [
    
    OBJECT_OT_add_bevel,    
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
    SCENE_OT_CartonScene,
    OBJECT_OT_snap_and_realign,
    KnockoutProperties,
    OBJECT_OT_generate_cutter_instances,
    OBJECT_OT_knife_project_cutters,
    SELProperties,
    MESH_OT_set_edge_length,
    MESH_OT_apply_scale,
    MESH_OT_toggle_edge_length,
    VIEW3D_OT_snap_cursor_to_selected,
    VIEW3D_OT_metric_imperial_set,
    VIEW3D_OT_toggle_wire,
    MESH_OT_vertex_bevel,
    MESH_OT_add_edge_to_edit_mesh,
    MESH_OT_add_scaled_plane,
    OBJECT_OT_tag_as_cutter,
    VIEW3D_PT_carton_creation,
    VIEW3D_PT_knockout_panel,
    CARTON_PT_mirror_panel,
    DPIScalerProperties,
    OBJECT_OT_scale_image_plane,
    VIEW3D_PT_dpi_scaler,
    CARTONVIZ_PT_CartonFinishing,
    CARTONVIZ_PT_SceneRendering,
    CartonCADMirrorProperties,
    CARTON_OT_snap_cursor_set_pivot,
    CARTON_OT_mirror_to_cursor,
    
    
    
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    

    bpy.types.Scene.sel_props = PointerProperty(type=SELProperties)
    bpy.types.Scene.knockout_props = bpy.props.PointerProperty(type=KnockoutProperties)
    bpy.types.Scene.dpi_scaler_props = bpy.props.PointerProperty(type=DPIScalerProperties)
    bpy.types.Scene.carton_cad_mirror_props = PointerProperty(type=CartonCADMirrorProperties)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Mesh', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.snap_cursor_quick",
            type='V',
            value='PRESS',
            shift=True)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.sel_props
    del bpy.types.Scene.knockout_props
    del bpy.types.Scene.dpi_scaler_props
    del bpy.types.Scene.carton_cad_mirror_props

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km in kc.keymaps:
            for kmi in km.keymap_items:
                if kmi.idname == "view3d.snap_cursor_quick":
                    km.keymap_items.remove(kmi)


if __name__ == "__main__":
    register()
