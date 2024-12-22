from fastapi import APIRouter, HTTPException

from typing import Optional
from src.movies.movies_data import Movies
from src.movies.schemas import Movie

movie_router = APIRouter()


@movie_router.get('/greet')
async def greet_user(name: Optional[str] = "User", age: int = 20) -> dict:
    return {"message": f"Hello, {name}", "age": age}


@movie_router.get('/')
def get_movies():
    return Movies


@movie_router.get('/{movie_id}')
async def get_movie(movie_id: int):
    for x in Movies:
        if x.id == movie_id:
            return x
    raise HTTPException(
        status_code=404, detail=f"Movie with id: {movie_id} not found"
    )


@movie_router.post('/')
def create_movie(movie: Movie):
    Movies.movie_routerend(movie)
    return movie


@movie_router.delete('/{movie_id}')
def delete_movie(movie_id: int):
    for index, x in enumerate(Movies):
        if x.id == movie_id:
            del Movies[index]
            return {"detail": "Movie deleted successfully"}
    raise HTTPException(
        status_code=404, detail=f"Movie with id: {movie_id} not found"
    )


@movie_router.put('/{movie_id}')
def update_movie(movie_id: int, movie: Movie):
    for index, x in enumerate(Movies):
        print(f"Checking movie with id {x.id} against {movie_id}")
        if x.id == movie_id:
            Movies[index] = movie
            return Movies[index]
    raise HTTPException(
        status_code=404, detail=f"Movie with id: {movie_id} not found"
    )
