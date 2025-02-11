import pandas as pd
from src.data_preprocessing import preprocess_data
from src.model_training import train_model
from src.prediction import make_prediction

def load_data():
    data = pd.DataFrame({
        'User_ID': [101, 102, 103, 104, 105],
        'Product_ID': ['P123', 'P456', 'P789', 'P101', 'P202'],
        'Category': ['Electronics', 'Fashion', 'Home', 'Electronics', 'Fashion'],
        'Price': [500, 1000, 300, 1500, 700],
        'Wishlist_Count': [10, 5, 2, 7, 8],
        'Return_History': [1, 0, 0, 1, 1],
        'Days_to_Return': [7, -1, -1, 10, 15],
        'Product_Rating': [4.5, 3.9, 4.2, 4.8, 4.0],
        'Return_Status': [1, 0, 0, 1, 1]
    })
    return data

if __name__ == "__main__":
    # Load and preprocess data
    data = load_data()
    print("Sample Data:\n", data.head())
    processed_data = preprocess_data(data)

    # Train the model
    model, accuracy = train_model(processed_data)
    print(f"Model trained with accuracy: {accuracy:.2f}")

    # Prepare input for prediction (exclude User_ID and Product_ID)
    sample_input = processed_data.drop(columns=['Return_Status', 'User_ID', 'Product_ID']).iloc[0:1]
    
    # Make a sample prediction
    prediction = make_prediction(model, sample_input)
    print(f"Sample Prediction (Return_Status): {prediction[0]}")
