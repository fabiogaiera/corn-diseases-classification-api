import tensorflow as tf
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

MODEL = tf.keras.models.load_model("../model")

web_page = """<html><body>It works!</body></html>"""

@app.get("/", response_class=HTMLResponse)
async def ping():
    return web_page