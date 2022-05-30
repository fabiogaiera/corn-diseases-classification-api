import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse


app = FastAPI()

model = tf.keras.models.load_model("../model")

html_open_tag = """<html>"""
html_close_tag = """</html>"""
body_open_tag = """<body>"""
body_close_tag = """</body>"""


web_page = html_open_tag + body_open_tag + """It works!""" + body_close_tag + html_close_tag

@app.get("/", response_class = HTMLResponse)
async def ping():
    return web_page

@app.post("/predict", response_class = HTMLResponse)
async def predict(file: UploadFile = File(...)):

    f = await file.read()