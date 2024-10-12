from loader import app
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse, HTMLResponse, RedirectResponse
import os


# Mount the static folder
app.mount("/static", StaticFiles(directory="data/static"), name="static")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("data/static/favicon.ico")



@app.get("/")
async def serve_homepage():
    return RedirectResponse(url="/static/index.html")
    # with open(os.path.join("data/static", "index.html")) as f:
    #     return HTMLResponse(content=f.read(), status_code=200)