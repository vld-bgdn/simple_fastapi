from typing import List, Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


class Movie(BaseModel):
    id: str
    title: str
    director: str
    year: int
    description: Optional[str] = None


class MovieCreate(BaseModel):
    title: str
    director: str
    year: int
    description: Optional[str] = None


MOVIES_DB = [
    Movie(
        id="1",
        title="The Shawshank Redemption",
        director="Frank Darabont",
        year=1994,
        description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    ),
    Movie(
        id="2",
        title="The Godfather",
        director="Francis Ford Coppola",
        year=1972,
        description="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    ),
]

movies_router = APIRouter(prefix="/movies", tags=["movies"])


@movies_router.get("/", response_model=List[Movie])
def read_movies():
    return MOVIES_DB


@movies_router.get("/{movie_id}", response_model=Movie)
def read_movie(movie_id: str):
    for movie in MOVIES_DB:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")


@movies_router.post("/", response_model=Movie, status_code=status.HTTP_201_CREATED)
def create_movie(movie: MovieCreate):
    if not MOVIES_DB:
        next_id = 1
    else:
        next_id = max(int(existing_movie.id) for existing_movie in MOVIES_DB) + 1
    new_movie = Movie(id=str(next_id), **movie.dict())
    MOVIES_DB.append(new_movie)
    return new_movie
