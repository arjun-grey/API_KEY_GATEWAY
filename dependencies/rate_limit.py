from fastapi import FastAPI , APIRouter


app = APIRouter()


def rate_limits(rate :int = 0 , limit : int = 10):
    
