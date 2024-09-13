from loader import app, TOKEN, dp, WebhookEntry, db, CommentAnswer, INSTAGRAM_TOKEN
from fastapi import Request, HTTPException, Query
from fastapi.responses import PlainTextResponse, JSONResponse
import requests, re


@app.delete("/comments")
async def delete_comment_answer(instagram_url : str, token : str = Query(..., description="Token for authentication")):
    media_id = extract_media_id(instagram_url)
    if not media_id:
        raise HTTPException(403, detail="Invalid instagram url")
    
    comment_answer = db.get_comment_answer_by_media_id(media_id)
    if not comment_answer:
        raise HTTPException(403, detail="Instagram url doesn't exsit")
    
    db.delet_commit_data(comment_answer.id)
    return JSONResponse({'status' : 'succses'})




def extract_media_id(instagram_url : str) -> str:
    resolt = re.search(r"instagram.com/reel/.*/|instagram.com/p/.*/", instagram_url)
    if resolt:
        return resolt.group()[0:-1].split('/')[-1]
        