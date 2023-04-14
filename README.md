![initial testr for ycsand100](https://user-images.githubusercontent.com/16747273/161411533-6e6b4dec-4f49-49a3-8696-32e2fcece2db.png)

# carton_previz_helper
Carton PreViz Helper addon

Carton Building

"Load Dieline" - load the dieline image as a plane into the 3d view, preferably top down.
"DieCam" - adds a Camera View to work through for UV Mapping and modeling purposes.
"Scene is ___ (toggle)" - Press to set the Scene units to Metric or Imperial depending on your project dieline measurements.
"Units", "Dims","Name", Include Units(toggle)" - set your object dimensions and name for your model, including dimensions if desired.
This is even more for your Domain object for rescale after model is done and folded.

"Object type" - choose Plane or Cube depending on if you are beginning to model the flat dieline or setting the Domain for rescal eof the folded carton
Press the action button to create the object at cursor.
"Add to Collection" - this creates a Collection from the anme of the object and puts it inside the collection.

Extras for Modeling
"Wire" - toggles selected object to Wireframe or Textured Solid in the 3d view for working with Domain object.
"Pivot(toggle)" - press to toggle between Mdeian Point or Cursor as pivot, and if neither is selected it will display an error icon
"Add Mirror" - in edit mode with the center edge loop selected and the negative axis deleted, this snaps the Origina of the objec to the selection and sets a Mirror modifier.
"XMirror" - in Object Mode, this applies the previous Mirror Modifier, assigns Empty Vertex Groups for the manual Folding, and turns on XMirror for symmetrical movement

Carton UV Mapping Tools
All buttons from legacy workflow at first, the old method of mapping to a simple cube can still be done quickly using the previously mentioned Domain object instead of modeling from a flat plane and manually Folding. The last options "Flat Project" is necessary in Edit mode to align the flat model to the dieline map.

Carton Finishing Tools

"Center Object" snaps the cursor and the selected object to the World Origin.
"Cardboard Set" adds a Solidify modifier to achieve a look of thickness to the flat model.
"Bevel" adds a bevel modifier to help with realism in the bends of the folded model.
"Base Shader" sets a Cycles Node Shader that allows to plug in the corresponding Dieline Map, Color Map and Bump Map from the dieline art exports from your vector program, and includes a procedural Printing Pattern to simulate the appearance of ink printed onto fiberboard.
"Fiberboard" adds a procedural shader that mimics fiberboard for the result of the solidify modifier.
"Corrugate"  adds a procedural shader that mimics cardboard corrugate for the result of the solidify modifier.

"Set Full Shot/Set Preview Snap(toggle)" allows a convenience of setting the basic settings needed for either a 512x512 preview render with color management and transparent background, or Full render settings at 2048x2048 for compositing in external software like Photoshop.
"Render Shot" - convenient location for render at current settings that doesn't require traveling up to the window menus or reaching for F12 key.



