# Corn Diseases Classifier API

## Model training with dataset https://www.tensorflow.org/datasets/catalog/plant_village

1. Execute python notebook in notebook/Model Training.ipynb 

## API deployment that serves the model

1. cd api

2. python -m venv .venv

3. source .venv/bin/activate (Linux) or .venv\Scripts\activate (Windows) 

4. pip install --upgrade pip

5. pip install -r requirements.txt

6. Create main.py file (main.py file already created in repository)

7. uvicorn main:app --reload 

8. 1. GET http://localhost:8000/api/ping (Postman collection available in repository)

8. 2. POST http://localhost:8000/api/predict (Postman collection available in repository)