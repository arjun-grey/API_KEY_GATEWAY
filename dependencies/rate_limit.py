import time
from fastapi import FastAPI , APIRouter , Depends , HTTPException , status
from dependencies.auth import authentication
from typing import Dict
app = APIRouter()

RATE_STORE = {}
def rate_limits(key_detail :Dict  =  Depends(authentication)):
     
    key = key_detail['api_key']

    limit = key_detail['rate_limit']  

    now = time.time()

    timestamp  = RATE_STORE.get(key , [])

    timestamp  = [
        ts 
        for ts in timestamp
        if now - ts < 60
    ]
    
    if len(timestamp) > rate_limits:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail = "rate limit accesed "
        )