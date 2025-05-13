from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get("/")
@app.get("/length")
def length(request: Request):
    return templates.TemplateResponse(request=request, name="length.html")

@app.post("/length")
def length(request: Request, len_in: str = Form(), len_from: str = Form(), len_to: str = Form()):
    unitInCentimeters = {
        'mm': 0.1,
        'cm': 1,
        'm': 100,
        'km': 100000,
        'in': 2.54,
        'ft': 30.48,
        'yd': 91.44,
        'mi': 160934.4
    }

    length = float(len_in) * (unitInCentimeters[len_from]/unitInCentimeters[len_to])
    return templates.TemplateResponse(request=request, name="result.html", context={"result": round(length, 4), "unit": len_to})

@app.get("/weight")
def weight(request: Request):
    return templates.TemplateResponse(request=request, name="weight.html")

@app.post("/weight")
def weight(request: Request, weight_in: str = Form(), weight_from: str = Form(), weight_to: str = Form()):
    unitInGrams = {
        'mg': 0.001,
        'g': 1,
        'kg': 1000,
        'oz': 28.3495,
        'lbs': 454.592
    }
    weight = float(weight_in) * (unitInGrams[weight_from]/unitInGrams[weight_to])
    return templates.TemplateResponse(request=request, name="result.html", context={"result": round(weight, 2), "unit": weight_to})

@app.get("/temperature")
def length(request: Request):
    return templates.TemplateResponse(request=request, name="temperature.html")

@app.post("/temperature")
def length(request: Request, temp_in: str = Form(), temp_from: str = Form(), temp_to: str = Form()):
    temp_in = float(temp_in)
    temp = temp_in

    match temp_from:
        case 'C':
            if temp_to == 'F': temp = (temp_in * 9/5) + 32
            elif temp_to == 'K': temp = temp_in + 273.15
        case 'F':
            if temp_to == 'C': temp = (temp_in - 32) * 5/9
            elif temp_to == 'K': temp = (temp_in - 32) * 5/9 + 273.15
        case 'K':
            if temp_to == 'C': temp = temp_in - 273.15
            elif temp_to == 'F': temp = (temp_in - 273.15) * 9/5 + 32
            
    return templates.TemplateResponse(request=request, name="result.html", context={"result": round(temp, 2), "unit": temp_to})