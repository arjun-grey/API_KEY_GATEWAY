import secrets
from fastapi import APIRouter, status
from database.keys import create_key
from dependencies import auth

router = APIRouter(prefix='/admin')

API_DATABASE = {}

@router.post("/keys", status_code=status.HTTP_201_CREATED)
async def Create_API(client: create_key):
    api_key = secrets.token_hex(32)
    
    API_DATABASE[api_key] = {
        "Client_name" : client.name,
        "Scope" : client.scope,
        "Rate_limit" : client.limit
    }
    return {"api_key":api_key , "data" : API_DATABASE[api_key]}
