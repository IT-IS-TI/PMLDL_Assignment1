import streamlit as st
import requests

# Streamlit app layout
st.title("California House Price Prediction App")

# Input fields for the user to enter the data
MedInc = st.number_input("Median Income (in $10,000s)")
HouseAge = st.number_input("House Age (years)")
AveRooms = st.number_input("Average Rooms per House")
AveBedrms = st.number_input("Average Bedrooms per House")
Population = st.number_input("Population")
AveOccup = st.number_input("Average Occupancy")
Latitude = st.number_input("Latitude")
Longitude = st.number_input("Longitude")

# Button to trigger the prediction
if st.button("Predict"):
    # Data for the prediction request
    input_data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }

    # Send the data to the FastAPI backend
    response = requests.post("http://api:8000/predict", json=input_data)

    # Show the prediction result
    if response.status_code == 200:
        result = response.json()["prediction"]
        st.success(f"Predicted House Price: ${result:.2f}")
    else:
        st.error("Error: Could not get prediction from the API")
