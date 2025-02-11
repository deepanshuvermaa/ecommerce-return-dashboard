import pandas as pd
import numpy as np

def generate_large_dataset(rows=10000):
    categories = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
    data = {
        'User_ID': np.random.randint(1000, 9999, size=rows),
        'Product_ID': [f'P{np.random.randint(100, 999)}' for _ in range(rows)],
        'Category': np.random.choice(categories, size=rows),
        'Price': np.random.randint(100, 5000, size=rows),
        'Wishlist_Count': np.random.randint(0, 50, size=rows),
        'Return_History': np.random.randint(0, 2, size=rows),
        'Days_to_Return': np.random.randint(-1, 30, size=rows),
        'Product_Rating': np.round(np.random.uniform(1, 5, size=rows), 1),
        'Return_Status': np.random.randint(0, 2, size=rows)
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    large_dataset = generate_large_dataset()
    print("Sample Large Dataset:")
    print(large_dataset.head())

    # Save the dataset as a CSV file
    large_dataset.to_csv("large_dataset.csv", index=False)
    print("Dataset saved as large_dataset.csv")
