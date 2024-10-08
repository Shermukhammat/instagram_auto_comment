from loader import app, TOKEN, dp, WebhookEntry, db, CommentAnswer, INSTAGRAM_TOKEN
from fastapi import Request, HTTPException, Query
from fastapi.responses import PlainTextResponse, JSONResponse
import requests, re


@app.post("/comments")
async def comment_answer_add(instagram_url : str, code : str, movi_url : str, token : str = Query(..., description="Token for authentication")):
    if token != TOKEN:
        raise HTTPException(403, detail="Invalid token")
    
    media_id = extract_media_id(instagram_url)
    if not media_id:
        raise HTTPException(403, detail = "Invalid instagram url")
    
    
    media_data = get_medias()
    if not media_data.get('data'):
        raise HTTPException(504, detail="Can't get medias")
    
    
    for media in media_data['data']:
        if media.get('permalink') and extract_media_id(media['permalink']) == media_id:
            check_id(media['id'])
            db.add_comment_data(CommentAnswer(media['id'], media_id, code, movi_url))
            
            return JSONResponse({'succses' : True})
                
    raise HTTPException(403, detail="Insagram url doesn't belong to you")
    
    
def check_id(id : str):
    if db.get_comment_data(id):
        raise HTTPException(403, detail = "Instagram url alredy exsist")

def get_medias() -> dict:
    re = requests.get(f"https://graph.instagram.com/me/media?fields=id,permalink&access_token={INSTAGRAM_TOKEN}")
    if re.status_code == 200:
        return re.json()
    return {}

def extract_media_id(instagram_ur : str) -> str:
    resolt = re.search(r"instagram.com/reel/.*/|instagram.com/p/.*/", instagram_ur)
    if resolt:
        return resolt.group()[0:-1].split('/')[-1]
        