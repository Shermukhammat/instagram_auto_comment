from loader import app, TOKEN, db
from fastapi import Request, UploadFile, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os, shutil
from uuid import uuid4

MAX_FILE_SIZE = 1024 * 1024
ALLOWED_MIME_TYPES = ["image/jpeg", "image/jpg", "image/png"]

os.makedirs("data/photos", exist_ok=True)
app.mount("/photos", StaticFiles(directory="data/photos"), name="photos")



@app.post('/photo/upload')
async def upload_photo(photo: UploadFile, token : str = Query(..., description="Token for authentication")):
    if token != TOKEN:
        raise HTTPException(403, detail='Invalid token')

    if photo.size > MAX_FILE_SIZE:
        raise HTTPException(400, detail = 'Phot maximum limit is 300Kb')

    if photo.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(400, 'Unsupported file type. Only JPEG and PNG are allowed.')
    
    file_name = get_file_name(photo)
    if not file_name:
        raise HTTPException(500, 'cant generated file name')
        
    
    path = f"data/photos/{file_name}"
    with open(path, 'wb') as file:
        shutil.copyfileobj(photo.file, file)
    
    db.add_file(file_name)
    return JSONResponse(content={"filename": file_name, "message": "Photo uploaded successfully!"})


def get_file_name(photo : UploadFile, atemps : int = 3) -> str:
    for _ in range(atemps):
        filename = f"{uuid4().hex}.{photo.content_type.split('/')[-1]}" 
        if db.is_file_exsist(filename):
            continue
        return filename