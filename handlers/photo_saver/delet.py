from loader import app, TOKEN, db
from fastapi import HTTPException, Query
import os



@app.delete("/photos")
async def delete_photo(filename: str, token : str = Query(..., description="Token for authentication")):
    if token != TOKEN:
        raise HTTPException(403, detail='Invalid token')
    
    if os.path.exists(f'data/photos/{filename}'):
        os.remove(f'data/photos/{filename}')
        db.delet_file(filename)

        return {'status' : 'success', 'message' : "The photo has been deleted succsesfuly"}

    raise HTTPException(403, detail='Phot doesn\'t exist')