## fit circle with given radius from the imported GDS file
## to be used to remove small dotted connected features
## can be used to fit other shape by replacing the sketch fuction

def fitCircle(current_body, R):
    selectionDesignFace = current_body.Faces[0]
    selectionFace = FaceSelection.Create(selectionDesignFace)

    # # Set Sketch Plane
    result = ViewHelper.SetSketchPlane(selectionFace)
    # # EndBlock

    # # Sketch Circle
    origin = Point2D.Create(MM(0), MM(0))
    result = SketchCircle.Create(origin, MM(R))
    # # EndBlock

def setInvisible(current_body):
    # # Change Object Visibility
    visibility = VisibilityType.Hide
    inSelectedView = False
    faceLevel = False
    selectionDesignbody = current_body
    selectionBody = BodySelection.Create(selectionDesignbody)
    ViewHelper.SetObjectVisibility(selectionBody, visibility, inSelectedView, faceLevel)
    # # EndBlock

def deleteBody(current_body):
    # delete surface
    selectionDesignbody = current_body
    selectionBody = BodySelection.Create(selectionDesignbody)
    result = Delete.Execute(selectionBody)

    # # Solidify Sketch
    mode = InteractionMode.Solid
    result = ViewHelper.SetViewMode(mode)
    # # EndBlock

def createCylinder(height):
    # # Extrude 1 Face
    selectionDesignFace = GetRootPart().Bodies[-1].Faces[0]
    selection = FaceSelection.Create(selectionDesignFace)
    options = ExtrudeFaceOptions()
    options.ExtrudeType = ExtrudeType.Add
    result = ExtrudeFaces.Execute(selection, MM(height), options)
    # # EndBlock

def createCylinderAll(height):
    # # Extrude all Faces
    visible_faces = [body.Faces[0] for body in GetRootPart().Bodies]
    selection = FaceSelection.Create(visible_faces)

    options = ExtrudeFaceOptions()
    options.ExtrudeType = ExtrudeType.Add
    result = ExtrudeFaces.Execute(selection, MM(height), options)

# # Get the root part
part = GetRootPart()
print(part.GetName())

# Get the bodies directly under the root part
bodies = part.GetBodies()

# # ------------------set R and height of a cylinder----------------------
# # !! mimimum value of R should be larger than 0.03 or software will not generate anything
R = 0.031
height = 0.02
# # ----------------------------------------------------------------------

 # # Loop through the bodies
for current_body in bodies:
    fitCircle(current_body, R)
    ## choose to hide original surface, but need to move it before creating body
    # setInvisible(current_body)
    deleteBody(current_body)
    ## choose to pull the cylinder body one by one in the loop
    # createCylinder(height)

# # choose to pull all the cylinder body all at once, may hang at large number
createCylinderAll(height)

Selection.Clear()
ViewHelper.ZoomToEntity()

# # EndBlock