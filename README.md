An example project of scikit-learn model deployment with FastAPI and Docker.

## Project description
```
sklearn_model_fastapi_docker
  ├───model
      │   wine.py
      ├───ml
          │   train.ipynb
          │   wine_model.joblib
  ├─── .dockerignore
  ├─── .gitignore
  ├─── app.py
  ├─── deploy.sh
  ├─── Dockerfile
  ├─── requirements.txt

```
**app.py** is an entry point of the project

  
## How To Run
The only thing you need to run project in Docker is **Docker Desktop installed on your computer**.

1. Run ***deploy.sh*** file
2. Go to http://127.0.0.1:8080/docs
3. Try out the post /predict method.
You can use predefined test data or your custom data like
```
{
  "data": [
    [14.23, 1.71, 2.43, 15.6, 127.0, 2.80, 3.06, 0.28, 2.29, 5.64, 1.04, 3.92, 1065.0],
    [13.20, 1.78, 2.14, 15.6, 127.0, 2.80, 3.06, 0.28, 2.29, 5.64, 1.04, 3.92, 1065.0]
  ]
}
```

## Additionally

* To create **requirements.txt** file use `pip list --format=freeze > requirements.txt` command to avoid weirdly looking paths
