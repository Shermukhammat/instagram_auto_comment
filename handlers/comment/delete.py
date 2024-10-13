from loader import app, TOKEN, db, CommentAnswer, INSTAGRAM_TOKEN, proxies
from fastapi import Request, HTTPException, Query
from fastapi.responses import PlainTextResponse, JSONResponse
import requests, re


@app.delete("/comment")
async def delete_comment_data(id : str, token : str = Query(..., description="Token for authentication")):
    if token != TOKEN:
        raise HTTPException(403, detail="Invalid token")
    
    comment_data = db.get_comment_data(id)
    if not comment_data:
        raise HTTPException(403, detail="Comment answer no found")

    db.delet_commit_data(id)
    return JSONResponse({'succses' : True})
    
