import uuid
from datetime import datetime
from pydantic import BaseModel

class Movie(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    director: str
    runtime: int
    genre: str
    language: str
    release_year: int
    rating: int
    created_at: datetime
    updated_at: datetime
