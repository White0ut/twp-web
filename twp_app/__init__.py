from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from service import TwpService

# Define the application
app = Flask(__name__)

# Config file in root of the project
app.config.from_object('config')

twp_service = TwpService();

@app.before_first_request
def check_location_on_startup():
  print 'Assert that the environment we are in will allow us to work'

import twp_app.controllers
