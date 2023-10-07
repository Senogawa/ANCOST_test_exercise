"""
Module for creating html structure and adding it in app.layout
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from database_methods.DB_and_PD_creating import DatabaseData
from plotly_methods.graphs import operators_shift_pies, all_dataframe_data

def create_html_dash_structure(app: dash.Dash):
    """
    Html code creating for easily refactoring and scaling
    """
    database = DatabaseData("./testDB.db")
    dataframe = database.get_pandas_dataframe()
    database.close_connection()

    operators_pie = operators_shift_pies(dataframe)

    app.layout = html.Div([
        html.H1("Ancost test exercise"),
        html.Div([
            dcc.Graph(id = "test_figure2", figure = all_dataframe_data(dataframe))],
            style = {
                "position": "absolute", 
                "top": "0", 
                "right": "0",
                "border": "1px solid #ccc",
                "border-radius": "5px",
                "padding": "10px",
                "background-color": "#f9f9f9",
                "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                "margin-right": "10px",
                "margin-top": "10px"
                    }
                ),

        html.Div([dcc.Graph(id = "test_figure", figure = operators_pie),], 
        style = {"position": "absolute",
                "top": "60%", 
                "left": "50%", 
                "transform": "translate(-50%, -50%)", 
                "width": "90%",
                "border": "1px solid #ccc",
                "border-radius": "5px",
                "padding": "10px",
                "background-color": "#f9f9f9",
                "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)"
                })
        
        ])




if __name__ == "__main__":
    database = DatabaseData("./testDB.db")
    test_dataframe = database.get_pandas_dataframe()
    data_for_pie = test_dataframe.groupby("state")["duration_min"].sum()
    print(data_for_pie.index)