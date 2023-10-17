from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, auth


# Your web app's Firebase configuration
# For Firebase JS SDK v7.20.0 and later, measurementId is optional

cred = credentials.Certificate("../masquerade-92984-firebase-adminsdk-4dgll-38f641c3fb.json")
firebase_admin.initialize_app(cred)

app = FastAPI(
    title="Masquerade API",
    docs_url="/"
)

# Simulated data storage (replace with a database in a real application)
users_db = {}
facemasqs_db = {}
projects_db = {}
videos_db = {}

# Models
class User(BaseModel):
    id: int
    email: str
    username: str
    password: str
    facemasqs: list = []

class Facemasq(BaseModel):
    id: int #id for s3 bucket

class Video(BaseModel):
    id: int #id for s3 bucket

# API Endpoints

@app.post('/signup')
async def create_an_account(user: User):
    email = user.email
    password = user.password

    try:
        user = auth.create_user(
            email = email,
            password = password
        )

        return JSONResponse(content={"message" : f"User account created successfuly for user {user.uid}"},
                            status_code= 201
               )
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail= f"Account already created for the email {email}"
        )

# 1. Generate New Face (Facemasq)
@app.post("/facemasqs/")
async def generate_facemasq():
    # Simulated Facemasq generation logic
    # Replace with your actual implementation
    facemasq_id = "123"  # Replace with the generated Facemasq ID
    return {"facemasq_id": facemasq_id}

# 3. Save Generated Face to User Account
@app.post("/facemasqs/save/")
async def save_facemasq(user_id: int, facemasq: Facemasq):
    # Simulated saving logic
    facemasqs_db[facemasq.image] = facemasq
    return {"message": "Facemasq saved successfully"}

# 4. List User's Saved Facemasqs
@app.get("/facemasqs/")
async def list_facemasqs(user_id: int):
    user_facemasqs = [facemasq for facemasq in facemasqs_db.values() if facemasq.user_id == user_id]
    return {"facemasqs": user_facemasqs}

# 5. Delete Saved Facemasq
@app.delete("/facemasqs/{facemasq_id}/")
async def delete_facemasq(user_id: int, facemasq_id: int):
    if facemasq_id not in facemasqs_db:
        raise HTTPException(status_code=404, detail="Facemasq not found")
    
    facemasq = facemasqs_db[facemasq_id]
    if facemasq.user_id != user_id:
        raise HTTPException(status_code=403, detail="Permission denied")

    del facemasqs_db[facemasq_id]
    return {"message": "Facemasq deleted successfully"}

# 10. Upload Video for Deepfake (within a Project)
@app.post("/videomasq/")
async def upload_video(user_id: int, facemasq_id: int, video: Video):
    # Simulated video upload and processing logic
    video_id = "789"  # Replace with the generated Video ID
    return {"video_id": video_id}