import tensorflow as tf
from fastapi import FastAPI


app = FastAPI()

MODEL = tf.keras.models.load_model("../model")

@app.get("/ping")
async def ping():
    return "It works!"