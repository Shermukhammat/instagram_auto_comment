from loader import app, TOKEN, MAX_FILE_SIZE, ALLOWED_MIME_TYPES
from fastapi import Request, UploadFile, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os, shutil
from uuid import uuid4


os.makedirs("data/photo_test", exist_ok=True)

@app.post('/photo_test/upload')
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
        
    
    path = f"data/photo_test/{file_name}"
    with open(path, 'wb') as file:
        shutil.copyfileobj(photo.file, file)
    
    return JSONResponse(content={"filename": file_name, "message": "Photo uploaded successfully!"})


def get_file_name(photo : UploadFile, atemps : int = 3) -> str:
    for _ in range(atemps):
        filename = f"{uuid4().hex}.{photo.content_type.split('/')[-1]}" 
        if os.path.exists(f"data/photo_test/{filename}"):
            continue
        return filename