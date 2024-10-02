from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the model
model = joblib.load("/models/california_model.pkl")

# Initialize the FastAPI app
app = FastAPI()


# Define the input data schema
class HouseData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


# Define the prediction endpoint
@app.post("/predict")
def predict(data: HouseData):
    # Convert the incoming data to the format expected by the model
    input_data = np.array([
        data.MedInc, data.HouseAge, data.AveRooms, data.AveBedrms,
        data.Population, data.AveOccup, data.Latitude, data.Longitude
    ]).reshape(1, -1)

    # Make a prediction using the loaded model
    prediction = model.predict(input_data)

    # Return the predicted house price
    return {"prediction": prediction[0]}
