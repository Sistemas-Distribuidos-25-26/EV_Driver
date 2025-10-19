import dash
from dash import html, dcc, Output, Input, State
from flask import Flask
import logging
#from kafka_producer import make_request

server = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = dash.Dash(__name__, assets_folder="assets", server=server)
app.layout = html.Div([
    html.H3("Selecciona un punto de recarga"),
    html.P("Tendrás que solicitar permiso a la central. Una vez validada tu solicitud, podrás recargar tu vehículo"),
    dcc.Input(placeholder="ID del CP", id="cp_input"),
    html.Button("Solicitar suministro", disabled=True, id="request_button", n_clicks=0),
    html.Button("Recargar", disabled=True, id="charge_button", n_clicks=0)

], id="main-div")

@app.callback(
    Input("request_button", "n_clicks"),
    State("cp_input", "value")
)
def request(n, value):
    print(f"[App] Mandando solicitud de recarga en {value}...")
    #make_request(value)

@app.callback(
    Output("request_button", "disabled"),
    Input("cp_input", "value")
)
def unlock_request_button(value):
    return value is None

def run():
    app.run("0.0.0.0", port=8000)