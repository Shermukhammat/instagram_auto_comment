from loader import app, TOKEN
from fastapi import HTTPException, Query
import os



@app.delete("/photo")
async def delete_photo(filename: str, token : str = Query(..., description="Token for authentication")):
    if token != TOKEN:
        raise HTTPException(403, detail='Invalid token')
    
    if os.path.exists(f'data/photo/{filename}'):
        os.remove(f'data/photo/{filename}')
        
        return {'status' : 'success', 'message' : "The photo has been deleted succsesfuly"}

    raise HTTPException(403, detail='Phot doesn\'t exist')