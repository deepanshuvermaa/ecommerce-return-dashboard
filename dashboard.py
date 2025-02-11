import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Initialize Dash app with external Bootstrap stylesheet
external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Load dataset
print("Loading large dataset...")
data = pd.read_csv("large_dataset.csv")

# Ensure 'Order_Date' is in datetime format (if present)
if 'Order_Date' in data.columns:
    data['Order_Date'] = pd.to_datetime(data['Order_Date'])

# Calculate category return rate
category_return_rate = (
    data.groupby('Category')['Return_Status']
    .mean()
    .reset_index()
    .rename(columns={"Return_Status": "Return_Rate"})
)

# Create category-wise return rate bar chart
category_fig = px.bar(
    category_return_rate,
    x='Category',
    y='Return_Rate',
    title='Category-wise Return Rate',
    template='plotly_dark',
    hover_data={'Return_Rate': ':.2f'},
    labels={"Return_Rate": "Return Rate (%)"}
)
category_fig.update_layout(height=400, margin=dict(l=50, r=50, t=50, b=50), title_x=0.5)

# Calculate top 10 users with the highest return counts
top_users = (
    data.groupby('User_ID')['Return_Status']
    .sum()
    .reset_index()
    .rename(columns={"Return_Status": "Total_Returns"})
    .sort_values(by='Total_Returns', ascending=False)
    .head(10)
)

# Create top 10 users bar chart
top_users_fig = px.bar(
    top_users,
    x='User_ID',
    y='Total_Returns',
    title='Top 10 Users with Highest Returns',
    template='plotly_dark',
    text='Total_Returns',
    labels={"User_ID": "User ID", "Total_Returns": "Number of Returns"}
)
top_users_fig.update_layout(height=400, margin=dict(l=50, r=50, t=50, b=50), title_x=0.5)
top_users_fig.update_traces(textposition='outside')

# Dashboard layout
app.layout = html.Div([
    html.H1(
        "E-commerce Return Prediction Dashboard",
        className="text-center text-light",
        style={"margin-bottom": "30px", "margin-top": "20px", "font-size": "3rem"}
    ),

    # Category Return Rate Section
    html.Div([
        html.H2("Category-wise Return Rate", className="text-center text-light mb-3"),
        dcc.Graph(id='category-return-rate-graph', figure=category_fig)
    ], className="card bg-dark text-white p-4 mb-4 mx-auto", style={"max-width": "800px"}),

    # Top 10 Users Section
    html.Div([
        html.H2("Top 10 Users with Highest Returns", className="text-center text-light mb-3"),
        dcc.Graph(id='top-users-graph', figure=top_users_fig)
    ], className="card bg-dark text-white p-4 mb-4 mx-auto", style={"max-width": "800px"}),

    # User-Specific Behavior Analysis Section
    html.Div([
        html.H2("User-Specific Behavior Analysis", className="text-center text-light mb-3"),
        dcc.Dropdown(
            id='user-dropdown',
            options=[{'label': f'User {user_id}', 'value': user_id} for user_id in data['User_ID'].unique()],
            placeholder="Select a User ID",
            className="mb-3"
        ),
        html.Div(id='user-analysis-output', className="text-light")
    ], className="card bg-dark text-white p-4 mb-4 mx-auto", style={"max-width": "800px"}),

    # CSV Download Section
    html.Div([
        html.H2("Download Data as CSV", className="text-center text-light mb-3"),
        html.Div(
            html.Button("Download CSV", id="download-button", className="btn btn-primary"),
            className="d-flex justify-content-center"
        ),
        dcc.Download(id="download-dataframe-csv")
    ], className="card bg-dark text-white p-4 mx-auto", style={"max-width": "800px"})
], className="container mt-4")

# Callback for CSV download
@app.callback(
    Output("download-dataframe-csv", "data"),
    [Input("download-button", "n_clicks")],
    prevent_initial_call=True
)
def download_csv(n_clicks):
    csv_string = data.to_csv(index=False, encoding='utf-8')
    return dcc.send_string(csv_string, filename="return_prediction_data.csv")

# Callback for User-Specific Behavior Analysis
@app.callback(
    Output("user-analysis-output", "children"),
    [Input("user-dropdown", "value")]
)
def update_user_analysis(user_id):
    if user_id is None:
        return ""
    
    user_data = data[data['User_ID'] == user_id]
    total_orders = len(user_data)
    total_returns = user_data['Return_Status'].sum()
    return_rate = (total_returns / total_orders) * 100 if total_orders > 0 else 0

    category_distribution = (
        user_data.groupby('Category')['Return_Status']
        .sum()
        .reset_index()
        .rename(columns={"Return_Status": "Returns"})
    )

    category_fig = px.pie(
        category_distribution,
        names='Category',
        values='Returns',
        title=f'Returns by Category for User {user_id}',
        template='plotly_dark'
    )

    return html.Div([
        html.P(f"Total Orders: {total_orders}", className="mb-1"),
        html.P(f"Total Returns: {total_returns}", className="mb-1"),
        html.P(f"Return Rate: {return_rate:.2f}%", className="mb-1"),
        dcc.Graph(figure=category_fig)
    ])

if __name__ == "__main__":
    app.run_server(debug=True)

#"http://127.0.0.1:8050/"