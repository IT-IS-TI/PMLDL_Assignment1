# PMLDL_Assignment1

Setup Guide
1. Clone the Repository

First, clone the repository to your local machine:

<pre>
  git clone https://github.com/IT-IS-TI/PMLDL_Assignment1.git
</pre>

2. Train the Machine Learning Model

For this example, we are using the California Housing dataset. Run the training script:

<pre>
  python train_model.py
</pre>

This will save the trained model in the models folder.

3. Build and Run Docker-Compose

Docker-Compose is used to set up the FastAPI backend and the Streamlit frontend in separate containers. Make sure you have Docker installed before proceeding.

Run the following command in your project directory to build both the API and web app containers:

<pre>
  docker-compose build
</pre>

Once the build is complete, run the containers:

<pre>
  docker-compose up
</pre>

The FastAPI service will be available at http://localhost:8000.

The Streamlit web app will be available at http://localhost:8501.

4. Test the app

<pre>{
  "MedInc": 8.5,
  "HouseAge": 25.0,
  "AveRooms": 5.0,
  "AveBedrms": 1.0,
  "Population": 1200,
  "AveOccup": 3.0,
  "Latitude": 34.05,
  "Longitude": -118.25
}
</pre>

