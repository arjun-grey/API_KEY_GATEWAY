from contextlib import asynccontextmanager
from fastapi import FastAPI

async def lifespan(app : FastAPI):
 

    app.state.api_database = {}

    app.state.limit_score = {}

    print("Gateway stated")

    yield

    app.state.api_database.clear()

    app.state.limit_score.clear()

    print("Gateway End")
