# House Price Prediction API

This project develops a web-based API for predicting house prices using machine learning. The API is built using FastAPI and is capable of delivering real-time predictions based on input features like house size, location, age, and more.

## Features

- **Machine Learning Model**: Utilizes a Gradient Boosting model trained on comprehensive housing data to predict prices with high accuracy.
- **Real-Time Predictions**: Offers a FastAPI server that provides predictions in real-time through RESTful endpoints.
- **Scalable and Production-Ready**: Includes configurations for deployment using Gunicorn and Uvicorn, making it ready for both development and production environments.
- **Data Analysis and Processing**: Implements advanced data processing and analysis within the Jupyter notebook, ensuring data quality and feature optimization for the model.

## Installation

Ensure you have Python 3.9.15 installed as specified in `runtime.txt`. Follow these steps to set up your environment:

### Clone the repository

```bash

git clone https://yourproject/repository.git
cd repository

```


### Install dependencies
```
pip install -r app/requirements.txt

```


## Project structure
- `api.py`: The API endpoints using FastAPI for handling predictions.
- `utils.py`: Helper functions for data processing and model interaction.
- `gb.pkl`: The serialized Gradient Boosting model used for making predictions.
- `Procfile` and `requirements.txt`: Setup for Heroku deployment and dependency management.
- `runtime.txt`: Specifies the Python version.


## Usage 
Start the API locally with:
```
uvicorn app.api:app --reload  # This activates the FastAPI server with live reloading

```


