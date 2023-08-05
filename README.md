# MlApp-FastAPI
This project aims to build a kidney stone prediction model using machine learning techniques.
The model will predict the likelihood of a patient having kidney stones based on certain features.

### Technologies Used
FastAPI: A modern, fast, web framework for building APIs with Python.
Docker: A containerization platform to ensure consistency across different environments.
Machine Learning Libraries: We will use popular ML libraries such as scikit-learn, pandas, and numpy for data preprocessing, model training, and evaluation.
Jupyter Notebook: We will use Jupyter Notebooks for exploratory data analysis and model development.


.
├── app
│   ├── main.py           # FastAPI application
│   ├── base_data.py         # Pydantic models for request/response
│   └── test_main.py          # Utility functions for data processing
├── notebooks
│   └── W4DataLeakage_and_BinaryClassif.ipynb   # Jupyter Notebook for model training and evaluation
├── Dockerfile            # Dockerfile for containerizing the application
├── requirements.txt      # Python dependencies
├── README.md 


### API Deployment
The FastAPI application in the app directory (main.py) will serve the trained model as a RESTful API. The API can be accessed via http://localhost:8000 after running the application.

### Docker Deployment
To deploy the kidney stone prediction model and API in a Docker container, follow these steps:

Build the Docker image using the provided Dockerfile:

docker build -t kidney-stone-prediction .

Run the Docker container:

docker run -d -p 8000:8000 kidney-stone-prediction

You can now access the API at http://localhost:8000 within the Docker container.
