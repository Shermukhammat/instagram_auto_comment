from fastapi import FastAPI
from config import TOKEN, INSTAGRAM_TOKEN, MAX_FILE_SIZE, ALLOWED_MIME_TYPES
from data import DataBase, CommentAnswer



app = FastAPI()
# db = DataBase('data/data.db')