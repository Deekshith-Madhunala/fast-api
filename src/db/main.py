from jinja2.runtime import async_exported
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import declarative_base
from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config import Config

async_engine=AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL,
        echo= True,
        future=True
    )
)

from sqlalchemy.exc import SQLAlchemyError

async def init_db():
    try:
        async with async_engine.begin() as conn:
            from src.movies.models import Movie  # Ensure your models are imported correctly
            print("Running database initialization...")
            await conn.run_sync(SQLModel.metadata.create_all)
            print("Database initialized successfully")
    except SQLAlchemyError as e:
        print(f"Error during database initialization: {e}")
        raise

async def get_session() -> AsyncSession:
    try:
        Session = sessionmaker(
            bind=async_engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

        async with Session() as session:
            yield session
    except SQLAlchemyError as e:
        print(f"Error while creating a session: {e}")
        raise
