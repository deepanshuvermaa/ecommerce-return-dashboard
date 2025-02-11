
# E-commerce Return Prediction Dashboard 📊

This project is a web-based dashboard built using Dash and Plotly to analyze e-commerce return patterns and user-specific behaviors. The dashboard provides valuable insights into return rates by category, top users with the highest returns, and detailed user-specific behavior analysis.

## Features 🚀
- **Category-wise Return Analysis:** Visualize return rates across different product categories.
- **Top Users Analysis:** Identify users with the highest number of returns.
- **User-Specific Analysis:** View personalized statistics for individual users, including total orders, total returns, and return rates.
- **CSV Download:** Export the dataset for further analysis.

## Installation 🔧
1. Clone the repository:
    ```bash
    git clone https://github.com/deepanshuvermaa/ecommerce-return-dashboard.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ecommerce-return-dashboard
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the dashboard:
    ```bash
    python dashboard.py
    ```

## Dataset 📂
The dashboard uses `large_dataset.csv`, which contains e-commerce transaction data, including:
- `User_ID`: Unique identifier for each user
- `Category`: Product category
- `Return_Status`: Indicates if the product was returned (1 for return, 0 otherwise)
- `Order_Date`: Date of the order

## How to Use 📋
- **Category Analysis:** Visualize overall return rates by category.
- **Top Users:** Find out which users have the most returns.
- **User-Specific Behavior:** Select a user from the dropdown to see personalized insights.
- **Export Data:** Click the "Download CSV" button to export the data.

## Technologies Used 🛠️
- Python
- Dash
- Plotly
- Pandas

## Contributing 🤝
Contributions are welcome! Please fork the repository and create a pull request.

## License 📜
This project is licensed under the MIT License.
