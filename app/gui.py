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
    dcc.Input(placeholder="ID del CP")
], id="main-div")

def run():
    app.run("0.0.0.0", port=8000)