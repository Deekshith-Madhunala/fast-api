from fastapi import APIRouter, HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.movies.schemas import Movie
from src.movies.service import MovieService
import logging
from src.movies.models import Movie as MovieModel

movie_router = APIRouter()
movie_service = MovieService()

@movie_router.get('/')
async def get_movies(session: AsyncSession = Depends(get_session)):
    logging.info("Getting all movies")  # Log the request
    return await movie_service.get_all_movies(session)

@movie_router.get('/{movie_id}')
async def get_movie(movie_id: str, session: AsyncSession = Depends(get_session)):
    movie = await movie_service.get_movie(movie_id, session)
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with id: {movie_id} not found")
    return movie

@movie_router.post("/")
async def create_movie(movie: Movie, session: AsyncSession = Depends(get_session)):
    try:
        # Map Pydantic model to SQLModel model
        movie_data = MovieModel(**movie.dict())
        session.add(movie_data)
        await session.commit()
        await session.refresh(movie_data)
        return movie_data
    except Exception as e:
        logging.error(f"Error: {e}")  # Use logging instead of print
        raise HTTPException(status_code=500, detail="Internal Server Error")


@movie_router.put('/{movie_id}')
async def update_movie(movie_id: str, movie: Movie, session: AsyncSession = Depends(get_session)):
    movie_dict = movie.dict()
    return await movie_service.update_movies(movie_id, movie_dict, session)

@movie_router.delete('/{movie_id}')
async def delete_movie(movie_id: str, session: AsyncSession = Depends(get_session)):
    return await movie_service.delete_movie(movie_id, session)