from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/length")
def length(request: Request):
    return templates.TemplateResponse(request, "length.html")

@app.get("/weight")
def weight(request: Request):
    return templates.TemplateResponse(request, "weight.html")

@app.get("/temperature")
def length(request: Request):
    return templates.TemplateResponse(request, "temperature.html")