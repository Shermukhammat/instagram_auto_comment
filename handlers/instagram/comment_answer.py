from loader import app, TOKEN, dp, WebhookEntry
from fastapi import Request, HTTPException, Query
from fastapi.responses import PlainTextResponse



@app.post("/comments")
async def comment_answer_add(id : str, instagram_ur : str, code : str, movi_url : str, token : str = Query(..., description="Token for authentication")):
    pass


@app.delete("/comments")
async def delete_comment_answer():
    pass