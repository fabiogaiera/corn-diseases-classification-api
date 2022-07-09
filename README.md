# Corn Diseases Classification API

## Model training with dataset https://www.tensorflow.org/datasets/catalog/plant_village

1. Execute python notebook in notebook/Model Training.ipynb 

## API creation that serves the model

1. Create a directory called api

2. cd api

3. python -m venv .venv

4. 1. source .venv/bin/activate (Linux)

4. 2. .venv\Scripts\activate (Windows)

5. pip install --upgrade pip

6. pip install -r requirements.txt

7. Create main.py file (main.py file already created in repository)

8. uvicorn main:app --reload 

9. 1. GET http://localhost:8000/api/ping (Postman collection available in repository)

9. 2. POST GET http://localhost:8000/api/predict (Postman collection available in repository)