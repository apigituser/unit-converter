from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/length")
def length(request: Request):
    return templates.TemplateResponse(request=request, name="length.html")

@app.post("/length")
def length(request: Request, len_in: str = Form(), len_from: str = Form(), len_to: str = Form()):
    return templates.TemplateResponse(request=request, name="result.html", context={"input": len_in, "from": len_from, "to": len_to})

@app.get("/weight")
def weight(request: Request):
    return templates.TemplateResponse(request=request, name="weight.html")

@app.post("/weight")
def weight(request: Request, weight_in: str = Form(), weight_from: str = Form(), weight_to: str = Form()):
    return templates.TemplateResponse(request=request, name="result.html", context={"input": weight_in, "from": weight_from, "to": weight_to})

@app.get("/temperature")
def length(request: Request):
    return templates.TemplateResponse(request=request, name="temperature.html")

@app.post("/temperature")
def length(request: Request, temp_in: str = Form(), temp_from: str = Form(), temp_to: str = Form()):
    return templates.TemplateResponse(request=request, name="result.html", context={"input": temp_in, "from": temp_from, "to": temp_to})