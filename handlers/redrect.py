from loader import db, TOKEN, app
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException


#tg://resolve?domain=FilmBufferBot&start=12

@app.get("/redirect")
async def redirect_user(id : str):
    if id.isnumeric():
        return RedirectResponse(url=f"tg://resolve?domain=FilmBufferBot&start={id}")
    
    raise HTTPException(403, detail="Invalid id")