from fastapi import FastAPI
from config import TOKEN, INSTAGRAM_TOKEN, MAX_FILE_SIZE, ALLOWED_MIME_TYPES, proxies
from data import DataBase, CommentAnswer
from instagram import Dispatcher


app = FastAPI()
db = DataBase('data/data.db')
dp = Dispatcher(INSTAGRAM_TOKEN, db)