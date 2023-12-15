from sqlalchemy import Table, Column, Integer, String
from database import metadata

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
)
