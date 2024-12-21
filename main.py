from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Movie(BaseModel):
    id: int = Field()
    title: str = Field(min_length=1)
    description: str = Field(min_length=10)
    release_year: int = Field(gt=1900)
    rating: int = Field(gt=3, lt=10)

Movies = []

@app.get('/greet')
async def greet_user(name: Optional[str] = "User", age: int =20) -> dict:
    return {"message": f"Hello, {name}", "age": age }

@app.get('/')
def greeting():
    return Movies

@app.post('/')
def create_movie(movie: Movie):
    Movies.append(movie)
    return movie

@app.delete('/{movie_id}')
def delete_movie(movie_id: int):
    for index, x in enumerate(Movies):
        if x.id == movie_id:
            del Movies[index]
            return {"detail": "Movie deleted successfully"}
    raise HTTPException(
        status_code=404, detail=f"Movie with id: {movie_id} not found"
    )

@app.put('/{movie_id}')
def update_movie(movie_id: int, movie: Movie):
    for index, x in enumerate(Movies):
        print(f"Checking movie with id {x.id} against {movie_id}")
        if x.id == movie_id:
            Movies[index] = movie
            return Movies[index]
    raise HTTPException(
        status_code=404, detail=f"Movie with id: {movie_id} not found"
    )
