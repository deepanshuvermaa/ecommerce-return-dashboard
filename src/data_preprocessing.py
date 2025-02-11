import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(data):
    # Handle missing values using .loc to avoid chained assignment warning
    data.loc[data['Days_to_Return'] == -1, 'Days_to_Return'] = 0
    
    # Encode categorical data
    label_encoder = LabelEncoder()
    data['Category'] = label_encoder.fit_transform(data['Category'])
    
    # Normalize numeric features (if needed)
    data['Price'] = data['Price'] / data['Price'].max()
    data['Wishlist_Count'] = data['Wishlist_Count'] / data['Wishlist_Count'].max()
    data['Days_to_Return'] = data['Days_to_Return'] / data['Days_to_Return'].max()
    
    return data
