from fastapi import FastAPI
from router.admin import router as admin_router

app = FastAPI()

app.include_router(admin_router)
