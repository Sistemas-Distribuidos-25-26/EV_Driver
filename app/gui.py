import dash
from dash import html, dcc, Output, Input, State
from flask import Flask
import logging
from kafka_producer import make_request, order
import config


server = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = dash.Dash(__name__, assets_folder="assets", server=server)
app.layout = html.Div([
    html.H3("Selecciona un punto de recarga"),
    html.P("Tendrás que solicitar permiso a la central."),
    html.P("Una vez validada tu solicitud, podrás recargar tu vehículo"),
    dcc.Input(placeholder="ID del CP", id="cp_input"),
    html.P("", id="error_label"),
    html.P("", id="notification_label"),
    html.Button("Solicitar suministro", disabled=True, id="request_button", n_clicks=0),
    dcc.Interval(interval=1000, n_intervals=0, id="interval_component")
], id="main-div")

@app.callback(
    [Output("notification_label", "children"),
     Output("error_label", "children")],
    Input("interval_component", "n_intervals")
)
def set_labels(n):
    return config.notification_text, config.error_text


@app.callback(
    Input("request_button", "n_clicks"),
    State("cp_input", "value")
)
def request(n, value):
    print(f"[App] Mandando solicitud de recarga en {value}...")
    make_request(value)

@app.callback(
    Output("request_button", "disabled"),
    Input("cp_input", "value")
)
def unlock_request_button(value):
    return value is None

def run():
    app.run("0.0.0.0", port=8001)