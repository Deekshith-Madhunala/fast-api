from fastapi import HTTPException
from sqlmodel import select, desc
from sqlmodel.ext.asyncio.session import AsyncSession
from src.movies.models import Movie  # Use the correct Movie model
import logging

class MovieService:

    async def get_all_movies(self, session: AsyncSession):
        statement = select(Movie).order_by(desc(Movie.title))
        result = await session.exec(statement)
        logging.info("fetching movies: ")
        return result.all()

    async def get_movie(self, movie_id: str, session: AsyncSession):
        statement = select(Movie).where(Movie.id == movie_id)
        result = await session.exec(statement)
        return result.first()

    async def create_movie(self, movie_data: dict, session: AsyncSession):
        new_movie = Movie(**movie_data)  # Create the database model instance
        session.add(new_movie)
        await session.commit()
        await session.refresh(new_movie)  # Refresh to get updated fields (e.g., `id`)
        return new_movie

    async def update_movies(self, movie_id: str, movie_data: dict, session: AsyncSession):
        movie = await self.get_movie(movie_id, session)
        if movie is None:
            raise HTTPException(status_code=404, detail=f"Movie with id: {movie_id} not found")

        for key, value in movie_data.items():
            setattr(movie, key, value)

        await session.commit()
        await session.refresh(movie)  # Refresh to get updated fields
        return movie

    async def delete_movie(self, movie_id: str, session: AsyncSession):
        movie = await self.get_movie(movie_id, session)
        if movie is None:
            raise HTTPException(status_code=404, detail=f"Movie with id: {movie_id} not found")
        await session.delete(movie)
        await session.commit()
        return {"message": "Movie deleted successfully"}
