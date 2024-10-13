from loader import app, TOKEN, db, CommentAnswer, INSTAGRAM_TOKEN, proxies
from fastapi import Request, HTTPException, Query
from fastapi.responses import PlainTextResponse, JSONResponse
import requests, re


@app.get("/comment")
async def get_comments_list(token : str = Query(..., description="Token for authentication")):
    if token != TOKEN:
        raise HTTPException(403, detail="Invalid token")
    
    comments_data = db.get_comments_data()
    return JSONResponse({'succses' : True, 'data' : [answer.get_row_data() for answer in comments_data]})
    
