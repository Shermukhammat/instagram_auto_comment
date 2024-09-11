from loader import app, TOKEN, db
from fastapi import Request, HTTPException
from fastapi.responses import PlainTextResponse


# This route will handle the verification process from Instagram
@app.get("/webhooks")
async def verify_webhook(request: Request):
    mode = request.query_params.get('hub.mode')
    token = request.query_params.get('hub.verify_token')
    challenge = request.query_params.get('hub.challenge')

    if mode and token:
        if mode == 'subscribe' and token == TOKEN:
            return PlainTextResponse(content=challenge, status_code=200)
        else:
            raise HTTPException(status_code=403, detail="Forbidden mode or token no match")
    
    raise HTTPException(status_code=403, detail="Forbidden, mode or token no found")



# This route will handle the incoming data from Instagram
@app.post("/webhooks")
async def handle_webhook(request: Request):
    data = await request.json()
    print(f"Received data: {data}")
    
    return {"success": True}