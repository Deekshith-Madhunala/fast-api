from fastapi import FastAPI

from src.movies.routes import movie_router

version = "v1.0"

app = FastAPI(
    title="MovieTix",
    description="A simple movie ticket booking API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    terms_of_service_url="https://example.com/terms/",
    version=version,
)

app.include_router(movie_router, prefix=f"/api/{version}/movies", tags=['movies'])
