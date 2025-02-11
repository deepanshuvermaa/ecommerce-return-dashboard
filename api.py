from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from src.data_preprocessing import preprocess_data
from src.model_training import train_model
from src.prediction import make_prediction

app = FastAPI()

# Load and preprocess the dataset
data = pd.read_csv("large_dataset.csv")
processed_data = preprocess_data(data)
model, accuracy = train_model(processed_data)

class UserInput(BaseModel):
    Category: str
    Price: float
    Wishlist_Count: int
    Return_History: int
    Days_to_Return: int
    Product_Rating: float

@app.post("/predict/")
def predict_return(user_input: UserInput):
    input_data = pd.DataFrame([user_input.dict()])
    input_data['Category'] = input_data['Category'].map({'Electronics': 0, 'Fashion': 1, 'Home': 2, 'Beauty': 3, 'Sports': 4})
    prediction = make_prediction(model, input_data)
    return {"return_prediction": int(prediction[0])}
