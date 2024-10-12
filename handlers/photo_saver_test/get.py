from loader import app, TOKEN
from fastapi import Request, UploadFile, File, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os, shutil
from uuid import uuid4



os.makedirs("data/photo_test", exist_ok=True)
app.mount("/files_test", StaticFiles(directory="data/photo_test"), name="photo_test")
    


