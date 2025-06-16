import uvicorn

from fastapi import FastAPI, Request
from routers.clean import router as clean
from db.engine import init_db


init_db()

app = FastAPI()
app.include_router(clean)


@app.get("/")
async def main():
    return {'message': 'Main Page'}


if __name__ == "__main__":
    # models.Base.metadata.drop_all(bind=engine)
    uvicorn.run(app, host='127.0.0.1', port=8003)