from fastapi import APIRouter , status , Depends
from dependencies.auth import authentication , AdminAuth
from dependencies.rate_limit import rate_limits

from typing import Dict

router = APIRouter(prefix='/data' , tags=['data'])

@router.get('/public' , status_code=status.HTTP_200_OK , dependencies=[Depends(rate_limits)])
def public():
    return {"status":"sucess" ,"data":"This data is public , any body can access it with out API key"}

@router.get('/private' ,status_code=status.HTTP_200_OK , response_model=Dict , dependencies=[Depends(rate_limits)])
def private(key_detail = Depends(authentication)):
    return  {"status":"sucess" ,
             "data":"This is private data only can acesss by API keys" ,
             "reponse":key_detail
             }

@router.get('/admin' , dependencies =  [Depends(AdminAuth)])
def admin():
    return {"message" : "you have a admin access"}