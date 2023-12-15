from models import movies
from fastapi import FastAPI
from database import engine, metadata, database

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/movies/")
async def create_movie(title: str, description: str):
    query = movies.insert().values(title=title, description=description)
    last_record_id = await database.execute(query)
    return {"id": last_record_id, "title": title, "description": description}

@app.get("/movies/")
async def read_movies():
    query = movies.select()
    return await database.fetch_all(query)

@app.put("/movies/{movie_id}")
async def update_movie(movie_id: int, title: str, description: str):
    query = movies.update().where(movies.c.id == movie_id).values(title=title, description=description)
    await database.execute(query)
    return {"message": "Movie updated successfully"}

@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    query = movies.delete().where(movies.c.id == movie_id)
    await database.execute(query)
    return {"message": "Movie deleted successfully"}



# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

