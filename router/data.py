from fastapi import APIRouter , status , Depends
from dependencies.auth import authentication


router = APIRouter(prefix='data' , tags=['data'])

@router.get('/public' , status_code=status.HTTP_200_OK)
def public():
    return {"status":"sucess" ,"data":"This data is public , any body can access it with out API key"}

@router.get('/private')
def private(key_detail :dict =  [Depends(authentication)]):
    return  {"status":"sucess" ,
             "data":"This is private data only can acesss by API keys" ,
             "reponse":key_detail
             }

@router.get('/admin')
def admin():
    return