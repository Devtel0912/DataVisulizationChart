import random
from unicodedata import category
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="Data Visualization App")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_index():
    with open("static/index.html", "r", encoding="utf-8") as file:
        return file.read()
    
data = {
    day: {
        "online": random.randint(1000, 5000),
        "offline": random.randint(1000, 5000)
    }
    for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
}

@app.get("/data/{name}")
def get_data_by_name(name: str):
    if name not in data:
        raise HTTPException(status_code=404, detail="Not found")

    return data[name]