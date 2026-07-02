import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f9",
        "padding": "30px",
        "fontFamily": "Arial"
    },
    children=[
        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }
        ),

        html.Div(
            [
                html.Label(
                    "Select Region:",
                    style={
                        "fontSize": "18px",
                        "fontWeight": "bold"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginTop": "10px"}
                ),
            ],
            style={
                "padding": "20px",
                "backgroundColor": "white",
                "borderRadius": "10px",
                "marginBottom": "20px",
                "boxShadow": "0px 2px 6px lightgray"
            },
        ),

        dcc.Graph(id="sales-chart"),
    ],
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(region):

    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"].str.lower() == region]

    fig = px.line(
        filtered,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Sales"
        },
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)