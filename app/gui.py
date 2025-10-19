import dash
from dash import html, dcc, Output, Input
from flask import Flask
import logging

server = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = dash.Dash(__name__, assets_folder="assets", server=server)
app.layout = html.Div([
    html.H3("Selecciona un punto de recarga:"),
    dcc.Input(placeholder="ID del CP", id="cp_input"),
    html.Button("Solicitar suministro", disabled=True, id="request_button")
], id="main-div")

@app.callback(
    Output("request_button", "disabled"),
    Input("cp_input", "value")
)
def unlock_request_button(value):
    return value is None

def run():
    app.run("0.0.0.0", port=8000)