# Corn Diseases Classification

## Dataset: https://www.tensorflow.org/datasets/catalog/plant_village

## Get started with FastAPI

1. Create a directory called api

2. python -m venv .venv

3. 1. source .venv/bin/activate (Linux)

3. 2. .venv\Scripts\activate (Windows)

4. pip install --upgrade pip

5. pip install fastapi

6. pip freeze > requirements.txt

7. Create main.py file as follows

```
from fastapi import FastAPI


app = FastAPI()

@app.get("/ping")
async def ping():
    return "It works!"

```

8. uvicorn main:app --reload

9. Open a web browser with this URL: http://localhost:8000/ping