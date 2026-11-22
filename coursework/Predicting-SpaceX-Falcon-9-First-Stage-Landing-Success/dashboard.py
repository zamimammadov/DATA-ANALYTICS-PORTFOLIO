"""Explore the 56 launches in the IBM course's geographical snapshot."""
from pathlib import Path

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

DATA = Path(__file__).parent / "data" / "spacex_launch_geo.csv"
launches = pd.read_csv(DATA)
site = "Launch Site"
mass = "Payload Mass (kg)"
launches["Recorded outcome"] = launches["class"].map({0: "Class 0", 1: "Class 1"})
launches["Booster family"] = launches["Booster Version"].str.replace(r"\s+B\d.*$", "", regex=True).str.strip()
maximum = int(launches[mass].max())

app = Dash(__name__, title="Falcon 9 landing outcomes")
app.layout = html.Main([
    html.H1("Falcon 9 landing outcomes"),
    html.P(f"{len(launches)} launches in the IBM course snapshot. Class 1 marks a successful landing; "
           "class 0 includes other recorded outcomes. Payload values follow the source, including zero."),
    html.Label("Launch site", htmlFor="site-dropdown"),
    dcc.Dropdown(["All sites", *sorted(launches[site].unique())], "All sites",
                 id="site-dropdown", clearable=False),
    html.P("Payload mass (kg)"),
    dcc.RangeSlider(0, maximum, 1, value=[0, maximum], id="payload-slider",
                    marks={n: f"{n:,}" for n in (0, 2000, 4000, 6000, maximum)},
                    tooltip={"placement": "bottom"}),
    html.P(id="selection-count", role="status"),
    dcc.Graph(id="outcomes"), dcc.Graph(id="payload"),
], style={"maxWidth": "960px", "padding": "1em", "margin": "auto", "fontFamily": "system-ui"})


@app.callback(Output("outcomes", "figure"), Output("payload", "figure"), Output("selection-count", "children"),
              Input("site-dropdown", "value"), Input("payload-slider", "value"))
def update_figures(selected_site, payload_range):
    lower, upper = payload_range
    selected = launches.loc[launches[mass].between(lower, upper)]
    if selected_site != "All sites":
        selected = selected.loc[selected[site] == selected_site]
    counts = selected.groupby([site, "Recorded outcome"]).size().reset_index(name="Launches")
    bars = px.bar(counts, x=site, y="Launches", color="Recorded outcome", barmode="group",
                  title="Recorded landing outcomes by site",
                  color_discrete_map={"Class 0": "#a95131", "Class 1": "#156c68"})
    scatter = px.scatter(selected, x=mass, y="Recorded outcome", color="Booster family",
                         hover_data=["Date", site, "Landing Outcome"], title="Payload and landing outcome")
    return bars, scatter, f"{len(selected)} launches in the selection."


if __name__ == "__main__":
    app.run()
