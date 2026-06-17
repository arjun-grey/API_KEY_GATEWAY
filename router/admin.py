import secrets
from typing import  Dict
from fastapi import APIRouter, status  , HTTPException 
from database.keys import create_key
from database.api import API_DATABASE
router = APIRouter(prefix='/admin')



@router.post("/keys", status_code=status.HTTP_201_CREATED)
async def Create_API(client: create_key):
    global API_DATABASE
    api_key = secrets.token_hex(32)
    
    API_DATABASE[api_key] = {
        "name": client.name,
        "scope" : client.scope,
    }
    return {"api_key":api_key , "data" : API_DATABASE[api_key]}

@router.get("/keys" , status_code=status.HTTP_200_OK , response_model=Dict)
def keys_list():
    if not API_DATABASE:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail="Dictionary is empty"
        )
    return API_DATABASE

@router.delete('/keys/{key}', status_code=status.HTTP_200_OK)
def key_revoke(key):
    global API_DATABASE
    if key not in API_DATABASE:
        raise HTTPException(
           status_code=status.HTTP_202_ACCEPTED ,
           detail="Dictionary is empty"
       )
    del API_DATABASE[key]
    return {"message " : "key deleted"}