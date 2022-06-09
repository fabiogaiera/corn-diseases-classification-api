# Corn Diseases Classification

## Dataset: https://www.tensorflow.org/datasets/catalog/plant_village

## Get started with FastAPI

1. Create a directory called api

2. python -m venv .venv

3. 1. source .venv/bin/activate (Linux)

3. 2. .venv\Scripts\activate (Windows)

4. pip install --upgrade pip

5. pip install fastapi==0.73.0

6. pip install uvicorn==0.17.1

7. pip install tensorflow==2.6.0

8. pip uninstall protobuf

9. pip install protobuf==3.20.0

10. pip uninstall keras

11. pip install keras==2.6.0

12. pip install Pillow==9.0.0

12. pip freeze > requirements.txt

13. Create main.py file as follows

```
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

html_open_tag = """<html>"""
html_close_tag = """</html>"""
head_tag = """<head><meta name="viewport" content="width=device-width, initial-scale=1"/></head>"""
body_open_tag = """<body>"""
body_close_tag = """</body>"""

it_works = html_open_tag + head_tag + body_open_tag + """It works!""" + body_close_tag + html_close_tag

app = FastAPI()

@app.get("/", response_class = HTMLResponse)
async def ping():
    return it_works

```

14. uvicorn main:app --reload

15. Open a web browser with this URL: http://localhost:8000