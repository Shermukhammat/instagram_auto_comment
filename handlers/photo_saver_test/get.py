from loader import app, TOKEN, db
from fastapi import Request, UploadFile, File, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os, shutil
from uuid import uuid4



os.makedirs("data/photos_test", exist_ok=True)
app.mount("/photos_test", StaticFiles(directory="data/photos_test"), name="photos_test")
    


