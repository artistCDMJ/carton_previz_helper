
<img width="1920" height="1009" alt="example for new carton master4" src="https://github.com/user-attachments/assets/f64bafbd-8225-4c85-a137-208dc7737fec" />
<img width="1920" height="1009" alt="example for new carton master3" src="https://github.com/user-attachments/assets/0ef99153-e8b5-4688-a6ef-5be417ab45d2" />
<img width="1920" height="1009" alt="example for new carton master2" src="https://github.com/user-attachments/assets/12d5ba4d-b4ef-4306-8699-4776ef5e61f3" />
<img width="1920" height="1009" alt="example for new carton master" src="https://github.com/user-attachments/assets/3079cf03-d544-4b35-a612-d71c6b4cd208" />


Carton PreViz Helper addon

*Carton Creation*

*Initial Dieline to Camera/Scene*

Load the Dieline image and immediately set the workspace to Imperial or Metric in the Edge Settings tab. 
With the dieline image plane selected, set the DPI of the image reference and then Apply Scaling to correct the image plane size to match the Scene Unit Scale.
  
Set a new Scene and then set the DieCam to match a camera view to the image plane - this is used for UV mapping after the modeling is finished.

*Edge Settings*

Since Unit type is already set, we can turn on Edge Length drawing to see the edge lengths in Edit mode. 
Edge Length can be set here for drawing new edges or resizing existing edges selected. 
Constrain to Cursor ON will scale the edge in relation to the cursor, OFF will scale them to their median point.
Auto Merge will allow vertex to be combined though you need to toggle Snap off before doing so.

*Edge Primitive*

Choose the Axis X or Y to draw the edge, press Generate EDge to draw from cursor.

*Plane Primitive*

Input Width and Height(X and Y) for a plane generation. Toggle Join to Active Object ON if you are already in Edit mode of an object mesh.

Press 'Add Scaled Plane' to generate the plane at the cursor (lower left corner is origin). Use the half of width desired and mirror mod for easier modeling.


*Extras for Modeling*

Wire Transparency is for toggling from solid/textured to wireframe, and Toggle Show Edges is for showing all edges in Object Mode.

Apply Scale is for Edit mode to allow scale to be corrected when necessary.

Snap to World will center the selected object to the World Origin 0,0,0.

Pivot Cursor/Median toggles from Median pivot to Cursor pivot and back.

Add Mirror adds a Mirror modifier wih clipping at center axis on X.
XMirror applies the Mirror mod and sets XMirror on while also assigning empty vertex groups and a basis and initial shape key as active.

*Bevel Corner Vertex*

Bevel width and Segments allow you to set the corner rounding once and apply it to all selected vertex by pressing Vertex Bevel.

*Knock Oout Cutter*
Three options:
    Circle, Square are primitives that can be scaled with the Size slider and then Cutters at Selected Vertex will generate copies at each selected vertex.
    Tag Object as Cutter will allow you to draw a mesh shape and name it as a cutter before generating at the selected vertex.
    Project Cutters cuts the shapes from the mesh and leaves faces that can be selected and deleted, creating holes in the mesh.
    
*Image Plane DPI Scaler*

Set the DPI to match the DPI used to create the image and the it will report the target size and the scale in Blender Units.
Apply Scaling will rescale the image plane to match the DPI translation into Inches or MM depending on the units used in scene.

*Carton Finishing*

Flat Project through Diecam - UV Project from View to Bounds matching the camera view.
Center Object Origin - recenters the selected object to the World Origin. Possibly redundant and might be deleted (Snap to World).

Cardboard Set - adds a Solidify Modifier and an Edge Split modifier with basic settings

Bevel - adds a Bevel modifier, though manual bevel works much better with anything having NGons.

Base Shader - adds the main Cycles shader tree for the outer surface complete with print patterns and bump map.

Fiberboard - a basic fiberboard material for the edge and back of the carton after the Cardboard Set is used.

Corrugate - similar to Fiberboard but with a faking of organic corrugate patterns.

*Carton Rendering*

Set Full Shot/Set Preview Shot toggles between regular full size and preview size renders

Set Pose Frames - this sets up a frame range of 5 frames and a single bone with initial rotations for parenting to the carton

Set Camera and Target - this sets the initial position of the camera and uses and empty for keeping the camera focused, not as useful so ok to delete.

Render shot - sets a render of the current frame

Render Frames - renders the foll 5 frame animation 



