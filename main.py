import uvicorn

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html",{'request': request},)


if __name__ == "__main__":
    # models.Base.metadata.drop_all(bind=engine)
    uvicorn.run(app, host='127.0.0.1', port=8003)