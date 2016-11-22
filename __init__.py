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
    
    
class TestPanel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_label = "Test Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Tests"
    
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
    bpy.utils.register_class(FrontMapping)
    bpy.utils.register_class(BackMapping)
    bpy.utils.register_class(TopMapping)
    bpy.utils.register_class(BottomMapping)
    bpy.utils.register_class(LeftMapping)
    bpy.utils.register_class(RightMapping)
    bpy.utils.register_class(MetricMeasurement)
    bpy.utils.register_class(TestPanel)
    
def unregister():
    bpy.utils.unregister_class(ImperialMeasurement)
    bpy.utils.unregister_class(FrontMapping)
    bpy.utils.unregister_class(BackMapping)
    bpy.utils.unregister_class(TopMapping)
    bpy.utils.unregister_class(BottomMapping)
    bpy.utils.unregister_class(LeftMapping)
    bpy.utils.unregister_class(RightMapping)
    bpy.utils.unregister_class(MetricMeasurement)
    bpy.utils.unregister_class(TestPanel)
    
    
       
if __name__ == "__main__":
    register()

