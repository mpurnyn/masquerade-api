# masquerade-api
An api for the masquerade project for providing a new face for use online.

# Goals
Currently I have 4 functions I want to implement
1. Login a user.
2. User requests the server to generate a face (called a facemasq) and display it then the users chooses weather or not save it to their account.
3. User starts a project for a generating a new DeepMasq video.
4. User uploads a video to perform the DeepMasq and selects a generated face from step 

# REST Server Calls

## User Authentication:

### Login User
    Method: POST
    Endpoint: /login
    Parameters:
        Username
        Password
    Expected Output:
        Authentication token (JWT) upon successful login
    Potential Server Responses:
        200 OK: Successful login
        401 Unauthorized: Invalid credentials

## Face Generation:

### Generate New FaceMasq
    Method: POST
    Endpoint: /facemasqs
    Parameters: None (UserID will be extracted from the authentication token)
    Expected Output:
        Newly generated Facemasq image
    Potential Server Responses:
        201 Created: Successful generation
        401 Unauthorized: User not authenticated

### Save Generated FaceMasq to User Account
    Method: POST
    Endpoint: /facemasqs/save
    Parameters:
        UserID (from authentication token)
        Image (Facemasq)
    Expected Output: None (Image is saved to the user's account)
    Potential Server Responses:
        201 Created: Successful save
        401 Unauthorized: User not authenticated
        400 Bad Request: Invalid image data

### List User's Saved Facemasqs
    Method: GET
    Endpoint: /facemasqs
    Parameters: UserID (from authentication token)
    Expected Output:
        List of saved Facemasqs
    Potential Server Responses:
        200 OK: Successful retrieval
        401 Unauthorized: User not authenticated

### Delete Saved Facemasq
    Method: DELETE
    Endpoint: /facemasqs/{FacemasqID}
    Parameters:
        UserID (from authentication token)
        FacemasqID (Facemasq to delete)
    Expected Output: None (Facemasq is deleted)
    Potential Server Responses:
        204 No Content: Successful deletion
        401 Unauthorized: User not authenticated
        403 Forbidden: User does not have permission
        404 Not Found: Facemasq not found

## Project Management (Masqing Project)
### Create a New Project (Deepmasq Video Project)
        Method: POST
        Endpoint: /projects
        Parameters:
            UserID (from authentication token)
            Name (Project name)
        Expected Output:
            Newly created project information
        Potential Server Responses:
            201 Created: Successful project creation
            401 Unauthorized: User not authenticated
            400 Bad Request: Invalid project data

### List User's Projects (including DeepMasq Video Projects)
    Method: GET
    Endpoint: /projects
    Parameters: UserID (from authentication token)
    Expected Output:
        List of user's projects (including DeepMasq Video Projects)
    Potential Server Responses:
        200 OK: Successful retrieval
        401 Unauthorized: User not authenticated

### Rename Project (DeepMasq Video Project)
    Method: PUT
    Endpoint: /projects/{ProjectID}
    Parameters:
        UserID (from authentication token)
        Name (New project name)
    Expected Output: Updated project information
    Potential Server Responses:
        200 OK: Successful renaming
        401 Unauthorized: User not authenticated
        403 Forbidden: User does not have permission
        404 Not Found: Project not found

### Delete Project (DeepMasq Video Project)
    Method: DELETE
    Endpoint: /projects/{ProjectID}
    Parameters:
        UserID (from authentication token)
    Expected Output: None (Project is deleted)
    Potential Server Responses:
        204 No Content: Successful deletion
        401 Unauthorized: User not authenticated
        403 Forbidden: User does not have permission
        404 Not Found: Project not found

## Video Processing:
### Upload Video for DeepMasq (within a Project)
    Method: POST
    Endpoint: /projects/{ProjectID}/videos
    Parameters:
        UserID (from authentication token)
        FacemasqID (Selected face model)
        Video file (to be processed)
    Expected Output: Processed video (DeepMasq)
    Potential Server Responses:
        201 Created: Successful video processing
        401 Unauthorized: User not authenticated
        403 Forbidden: User does not have permission
        404 Not Found: Project not found