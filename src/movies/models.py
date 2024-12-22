from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg

from datetime import datetime
import uuid


class Movie(SQLModel, table=True):
    __tablename__ = 'movies'

    id: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4()
        )
    )
    title: str
    description: str
    director: str
    runtime: int
    genre: str
    language: str
    release_year: int
    rating: int
    created_at: datetime = Field(Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(Column(pg.TIMESTAMP, default=datetime.now))


def __repr__(self):
    return (f"<Movie(id='{self.id}', title='{self.title}', description='{self.description}', "
            f"director='{self.director}', runtime='{self.runtime}', genre='{self.genre}',"
            f" language='{self.language}', release_year='{self.release_year}', rating='{self.rating}', "
            f"created_at='{self.created_at}', updated_at='{self.updated_at}')>")
