#
#
#
# Author: Lukas Talaga
# CUID: Luta2112
# GitHub: Lukas-Talaga
# 
# Purpose: This is the file used by Render to host a basic flask app web service.
#          The application uses PostgreSQL to store, manipulate, and retrieve data displayed by the browser.
#
#
#

import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Lukas Talaga in 3308'

# Testing PostgreSQL database connection success
@app.route('db_test')
def testing():
    conn = psycopg2.("https://lukas-talaga-cspb-3308-lab-10.onrender.com") # connects to the PostgreSQL database
    conn.close() # closes the connection
    return "Database Connection Successful" # Displayed on the browser to show confirmation that this function ran and connected to the db