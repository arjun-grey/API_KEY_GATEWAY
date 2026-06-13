from fastapi import HTTPException , status
from database.api import API_DATABASE


async def authentication(api):
    
    if not API_DATABASE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="API key database is empty"
        )

    if api not in API_DATABASE:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="API key not present in database"
        )
    
    return API_DATABASE[api]