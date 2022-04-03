# carton_previz_helper
Carton PreViz Helper addon

**Simple Carton Workflow**(03/08/22)

    • Set Scene Units with the Imperial or Metric buttons depending on measurements provided
    • Add a New Carton using the Carton 3D Base button, and input the measurements in the popup dialog in the lower corner
    • In Carton Finishing Tools, add the Base Shader and in the Shader Editor, add the corresponding Dieline, Colormap and Bumpmap images exported form the vector software
    • in UV Editing Workspace, use the Face Selection in Edit mode to select the faces of the Carton one at a time, projecting them onto the UV Editor with the Face project buttons in Carton UV Mapping Tools.
    • Swap to Shading Workspace and Apply Scale and Rotation with Ctrl-A. Use Center Object in Carton Finishing tools  to snap the cursor and the carton to the World Origin to align to the Scene.
    • Add a slight bevel to the carton with the Bevel preset button, and set up for render. 
    • WIP – A single bone with pose library is a manual set up for now, but later the intent is to have this generated via button press so that standard poses for camera are automatic.

**Flat Folded Carton Workflow** (03/08/22)

    • Set Scene Units with the Imperial or Metric buttons depending on measurements provided.
    • Focusing on the Carton Modeling Tools, use the button ‘Load Dieline’ to bring the main dieline art into the 3d view with the Images as Planes Addon – choose ‘Flat’ and ‘Texture’ in the view properties.
    • With the Dieline plane selected, use the ‘Die Cam’ button to set a working camera to model in that will allow UV Project from View after modeling is final.
    • Initiate modeling with ‘Flat Carton’ and use ‘Wire’ to toggle wire view so that modeling can be carried out in Edit mode while still seeing the dieline art.
    • Grab the edges one at a time and move them to match the center panel(s). Extrude the edges to create the next panels in a vertical fashion, covering all the face without worrying about the flaps.
    • Hovering over the newly created panels, press ‘Ctrl-R’ to cut an Edge Loop that falls in the Center of the panel faces. Select the right side Vertexes and delete them, leaving the center edge and the left side of the model.
    • Select the center line and press ‘Add Mirror’. This will snap the Object Origin to the selection and add a Mirror Modifier to enable modeling the side flaps. 
    • Extrude out for each flap taking care to consider the boundary of the dieline, and rounded corners can be achieved with Vertex Beveling. N-Gons are welcome here.
    • Tab to Object Mode and use ‘Xmirror’ to apply the modifier and enable X Mirror topology movement for folding. Empty Vertex Groups are added already named for the main areas for folding. 
    • Select all faces and press’ Flat Project’ in Carton UV Mapping Tools to project the mesh through the camera to the texture on the reference dieline obect. Personal preference si to dissolve the midline edge loop in the carton faces that was the pivot in the mirror modifier.
    • Toggle Wire again to have a solid Textured view of the mesh.
    • In Carton Finishing Tools, press ‘Base Shader’ to add a preset shader for plugging the export textures into.
    • Swap to the Shader Editor and indicate the textures in their corresponding Texture Nodes named for Dieline, Colormap and Bumpmap. Make sure that the Color Mix Node labeled ‘Switch’ is set to Fac value of 0 to see the Dieline lines.
    • In Layout Workspace, in Edit Mode confirm that the Selection Mode is set to both Edge and Face still from the Xmirror button. Toggle Pivot in Carton Building panel so that the pivot is set to Cursor.
    • Select the folding lip and assign it to ‘lip’, assign the next face panel and its side flaps and assign to ‘back’. Select the next panel and side flaps and assign to ‘top’, next set to ‘front’ and last set to ‘bottom’.
    • Snap the cursor to the edge for each flap on the side and select the faces for the flap – rotate on Y axis and the opposite side will also rotate into position.
    • Do this for all of the faces and result will be a closed, folded carton.
    • In Object Mode, use ‘Cardboard Set’ to add a Solidify modifier that expects a second shader, and then use ‘Fiberboard to set a procedural fiberboard material to the inside and exposed edges.
    • Optional Corrugate for anything needing heavier thickness, but the Solidify modifier then needs to be adjusted.
    • ‘Center Object’ to center the cursor and the object to the World Origin, and set up for Camera View. 
    • Beveling can be done with the ‘Bevel’ button, but manual bevel edits can give a better result.
    • Rename the object with the ‘ Name:’ field, and hover over it to copy the name to then paste in when (M)oving to a New Collection. Also pays to paste that same name onto the Shader name for keeping multiple cartons available in file.
    • WIP – A single bone with pose library is a manual set up for now, but later the intent is to have this generated via button press so that standard poses for camera are automatic.


