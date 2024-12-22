from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.db.main import init_db
from src.movies.routes import movie_router


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting... ")
    await init_db()
    yield
    print(f"Server has been stopped")


version = "v1.0"

app = FastAPI(
    title="MovieTix",
    description="A simple movie ticket booking API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    terms_of_service_url="https://example.com/terms/",
    version=version,
    lifespan=life_span
)

app.include_router(movie_router, prefix=f"/api/{version}/movies", tags=['movies'])
