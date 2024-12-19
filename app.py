from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from main import translate
import uvicorn

app = FastAPI()
template = Jinja2Templates(directory="template/")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def root(request: Request):
    return template.TemplateResponse(name="index.html", context={"request": request})

@app.get('/api/trans/{word}')
async def trans(word):
    result = translate(word)
    return {"result": result};

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)