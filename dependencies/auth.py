from fastapi import HTTPException , status , Header  , Depends
from database.api import API_DATABASE  


async def authentication(api :str = Header(None)):

    if not API_DATABASE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Missing API key "
        )

    if api not in API_DATABASE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key or key not found"
        )
    
    return API_DATABASE[api]

async def AdminAuth(key_detail :dict = Depends(authentication)):
    
    if "admin" not in key_detail['scope']:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail = "Not have admin access"
        )

    return key_detail