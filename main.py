from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/length")
def length():
    return {"unit":"length"}

@app.get("/weight")
def weight():
    return {"unit":"weight"}

@app.get("/temperature")
def temperature():
    return {"unit":"temperature"}