import pandas as pd
import plotly.graph_objects as go

# Load the prices data
df = pd.read_csv("prices_round_1_day_0.csv", sep=";")

# Get the unique products available in the dataset
products = df["product"].unique()

# Loop through each product and create a separate graph
for product in products:
    product_df = df[df["product"] == product]

    # Initialize a new figure for the product
    fig = go.Figure()

    # Add a scatter trace for Ask Prices in red (100% opaque, larger size)
    fig.add_trace(
        go.Scatter(
            x=product_df["timestamp"],
            y=product_df["ask_price_1"],
            mode="markers",
            marker=dict(color="red", size=8, opacity=1.0),
            name="Ask Price 1",
        )
    )

    # Add a scatter trace for Bid Prices in blue (100% opaque, larger size)
    fig.add_trace(
        go.Scatter(
            x=product_df["timestamp"],
            y=product_df["bid_price_1"],
            mode="markers",
            marker=dict(color="blue", size=8, opacity=1.0),
            name="Bid Price 1",
        )
    )

    # Update layout with titles
    fig.update_layout(
        title=f"Bid and Ask Prices for {product}",
        xaxis_title="Timestamp",
        yaxis_title="Price",
        template="plotly_white",
    )

    # This command renders the plot as an HTML file and opens it in your default browser
    fig.show()
