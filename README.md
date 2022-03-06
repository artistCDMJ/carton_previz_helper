# carton_previz_helper
Helper add on for Blender for unwrapping simple mesh objects based on cubes
The panel appears in the N panel sidebar once activated.
The first box is for setting Imperial or Metric World units,
The second box is for adding either a Carton 3d box primitive that allows setting the measurements in the popup, or using the Flat primitive to build with.

The workflow for the Flat Primitive:  
  * Add the Reference Dieline (uses the Add Images as Planes addon)
  * with that selected still, add the Die Cam(era) to allow the work throguh the camera view to line up UV mapping later
  * add the Flat primitive
  * toggle Wire view mode for the selected flat plane so that it will be visible - once in Edit Mode, the selection modes are combined Vertex and Edge
  * manually match the flat primitive face to the first center flap and extrude to cover the center flaps up. Ctrl-R to add a center loop cut, and then select the righ outermost vertex loop and delete.
  * Select the edge loop still in the center and press 'Add Mirror' to set the Object Origin to the selected edge loop and add a Mirror Modifier to the mesh.
  * finish modeling the flaps and then tab to Object Mode - pressing XMirror will apply the mirro modifier and turn on X Mirror mode as well as create a set of empty vertex groups for the carton zones.
  * Once the model is done, use the Carton 3D base and Wire buttons to create a reference guide for scale to align the flat carton to world scale.
  * In Object Mode, apply scale with Ctrl-A and then switch to the Shading Workspace.
  * Follow steps to create carton shader

Workflow for Carton 3D Base:
  * Press relevant Imperial or Metric button to set World units correctly for dieline
  * Using UV Editing Workspace, Add Carton 3D Base and scale(measurements) to the Dieline measurements in the UV Editor window
  * In Edit Mode, select each face of the Carton Base and use the Carton UV Mapping buttons to project the faces into the dieline - manually align them to the corresponding panels in the dieline art.
  * In Object Mode, apply scale with Ctrl-A, press 'Add Bevel', and then switch to the Shading Workspace.
  * Follow steps to create carton shader
  
 Workflow for Shader Creation:
  * With selection active, add a new shader to the Object.
  * Default is Principled Shader, this will work. Add UV mapping node, 3 image texture nodes and a Bump node.
  * Add the Dieline, Colormap, and Bump Map images to the image nodes and plug the bump map into a bump node fed to the Normal of the Principled shader.
  * Use a Color Mix Node between the Dieline and the Colormap to feed to the color input on the Principled shader. Using the mix factor of 0/1 will switch between them.
  * Use the Dieline view to make cuts and extrusions to 'fake' flaps on simple models. Switch to Colormap for render.
