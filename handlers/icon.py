from loader import app
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse


# Mount the static folder
app.mount("/static", StaticFiles(directory="data/static"), name="static")

# Route for favicon.ico
# @app.get("/favicon", include_in_schema=False)
# async def favicon():
#     return  FileResponse("data/static/favicon.ico")