from doctest import debug

from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.db.main import init_db
from src.movies.routes import movie_router
import logging

@asynccontextmanager
async def life_span(app: FastAPI):
    try:
        print("Server is starting...")
        await init_db()
        yield
    except Exception as e:
        logging.error(f"Error during app startup: {e}", exc_info=True)
    finally:
        print("Server has been stopped")


version = "v1.0"

app = FastAPI(
    title="MovieTix",
    description="A simple movie ticket booking API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    terms_of_service_url="https://example.com/terms/",
    version=version,
    lifespan=life_span,
    debug= True
)

app.include_router(movie_router, prefix=f"/api/{version}/movies", tags=['movies'])
