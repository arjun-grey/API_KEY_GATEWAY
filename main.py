from fastapi import FastAPI , middleware
from router.admin import router as admin_router
from router.data import router as data_router
from middleware.logging import (logging_middle)
from contextlib import asynccontextmanager
from corelife.lifespan import lifespan

app = FastAPI(lifespan=lifespan)

app.include_router(admin_router)
app.include_router(data_router)
app.middleware('https')(
    logging_middle
)
