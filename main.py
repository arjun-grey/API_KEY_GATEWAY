from fastapi import FastAPI
from router.admin import router as admin_router
from router.admin import router as data_router

app = FastAPI()

app.include_router(admin_router)
app.include_router(data_router)
