import dash
from html_set.html_structure_creating import create_html_dash_structure


def main():
    app = dash.Dash()
    create_html_dash_structure(app)
    app.run_server(debug = True)


if __name__ == "__main__":
    main()



















