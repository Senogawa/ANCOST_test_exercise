"""
Module for creating graphs
"""

import pandas as pd
import plotly.express as px
import plotly
import plotly.graph_objects as pgo
from plotly.subplots import make_subplots
from database_methods.DB_and_PD_creating import DatabaseData


def operators_shift_pies(dataframe: pd.DataFrame) -> plotly.graph_objs._figure.Figure:
    """
    Creating and returning px pie figure
    """

    operators = list(set(dataframe["operator"].values)) #getting unique values

    specs = [[{'type':'domain'} for _ in range(len(operators))]]

    fig = make_subplots(1, len(operators), specs = specs)
    annotations = []

    col = 1
    x_start = 0.1
    for operator in operators:
        fig.add_trace(pgo.Pie(labels = dataframe["reason"], values = dataframe[dataframe["operator"] == operator]["duration_min"], name = operator), row = 1, col = col)
        annotations.append(dict(text = f"Shift {operator}", x = x_start, y = 1, font_size = 20))
        x_start += 0.25
        col += 1

    fig.update_layout(
        title_text = "Diagrams work perfoming in minute duration on operators shift",
        annotations = annotations,
        title_font_size=20
    )

    return fig
    

def all_dataframe_data(dataframe: pd.DataFrame) -> plotly.graph_objs._figure.Figure:
    """
    Create all database information diagram
    """

    ...

if __name__ == "__main__":
    data = DatabaseData("./testDB.db")
    datafrafe = data.get_pandas_dataframe()
    data.close_connection()
    #pie(datafrafe)