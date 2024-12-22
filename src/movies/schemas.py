from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int = Field()
    title: str = Field(min_length=1)
    description: str = Field(min_length=10)
    release_year: int = Field(gt=1900)
    rating: int = Field(gt=3, lt=10)
