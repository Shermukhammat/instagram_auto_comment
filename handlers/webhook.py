from loader import app, TOKEN, dp
from fastapi import Request, HTTPException
from fastapi.responses import PlainTextResponse, JSONResponse
from instagram import WebhookEntry
from instagram.types import Field



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
    try:
        # Try to read the JSON body from the request
        data = await request.json()
    except Exception as e:
        # Return a 400 Bad Request response if the JSON body is missing or invalid
        raise HTTPException(status_code=400, detail="Invalid JSON body")

    # print(data)
    if type(data) == dict and data.get('object') == 'instagram' and type(data.get('entry')) == list:
        entry : list = data['entry']
        for entry_data in entry:
            entry_obj = WebhookEntry(entry_data)
            
            await dp.respond(entry_obj)
            
    #         print(data['entry'])
            # entry = WebhookEntry(data)
            # dp.respond(entry)
    # print(f"Received data: {data}")
    
    return {"success": True}