from fastapi import FastAPI
from config import TOKEN
from data import DataBase

app = FastAPI()
db = DataBase('data/data.db')