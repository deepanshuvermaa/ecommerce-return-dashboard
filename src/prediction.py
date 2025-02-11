# ecommerce_return_prediction/src/prediction.py
def make_prediction(model, input_data):
    # Predict the return status for the given input data
    prediction = model.predict(input_data)
    return prediction
