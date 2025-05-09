from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/submit")
def length(request: Request, length: float = Form(), length_from: str = Form(), length_to: str = Form()):
    return {"Length": length, "From_length": length_from, "To_length": length_to}