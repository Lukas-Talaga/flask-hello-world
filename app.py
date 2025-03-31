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

# Tests and verifies PostgreSQL database connection success
@app.route('/db_test')
def test_db_conn():
    conn = psycopg2.connect("postgresql://lukas_talaga_cspb_3308_lab_10_postgresql_user:EVJVGUJi7oBvBRLjnN7km0zZmVBzwrDv@dpg-cvldj32dbo4c73dai8d0-a/lukas_talaga_cspb_3308_lab_10_postgresql") # connects to the PostgreSQL database
    conn.close() # closes the connection
    return "Database Connection Successful" # Displayed on the browser to show confirmation that this function ran and connected to the db

# Creates and returns verification of an example table with Basketball information
@app.route('/db_create')
def create_db_table():
    conn = psycopg2.connect('postgresql://lukas_talaga_cspb_3308_lab_10_postgresql_user:EVJVGUJi7oBvBRLjnN7km0zZmVBzwrDv@dpg-cvldj32dbo4c73dai8d0-a/lukas_talaga_cspb_3308_lab_10_postgresql') # connects to the PostgreSQL database
    cur = conn.cursor() # create a cursor to interact with database data
    # uses SQL to create sample table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit() # Makes the database changes remain after closing connection
    conn.close() # Close the database
    return "Basketball Table Successfully Created" # Display verification in browser that function ran

# Inserts data into the example Basketball table and displays verification
@app.route('/db_insert')
def insert_into_db():
    conn = psycopg2.connect('postgresql://lukas_talaga_cspb_3308_lab_10_postgresql_user:EVJVGUJi7oBvBRLjnN7km0zZmVBzwrDv@dpg-cvldj32dbo4c73dai8d0-a/lukas_talaga_cspb_3308_lab_10_postgresql') # connects to the PostgreSQL database
    cur = conn.cursor() # create a cursor to interact with database data
    # uses SQL to create sample table
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit() # commits changes to the db
    conn.close() # close the db connection
    return "Basketball Table Successfully Populated" # return verification that the function ran

# Displays all the data currently in the database table "Basketball"
@app.route('/db_select')
def select_from_db():
    conn = psycopg2.connect('postgresql://lukas_talaga_cspb_3308_lab_10_postgresql_user:EVJVGUJi7oBvBRLjnN7km0zZmVBzwrDv@dpg-cvldj32dbo4c73dai8d0-a/lukas_talaga_cspb_3308_lab_10_postgresql') # connects to the PostgreSQL database
    cur = conn.cursor() # create a cursor to interact with database data
    # uses SQL to create sample table
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    cursor_response = cur.fetchall()
    conn.close() # close the db connection
    table_data = ""
    table_data += "<table>" # add table HTML tag before data to be able to display on browser
    for row in cursor_response:
        table_data += "<tr>" # prepend each row in db with table row tag
        for attribute in row:
            table_data += "<td>{}</td>".format(attribute)
        table_data += "</tr>" # append each row in db with table row tag
    table_data += "</table>" # close the table tag
    return table_data # display the table data

# Drops the Basketball table from the PostgreSQL database
@app.route('/db_drop')
def drop_from_db():
    conn = psycopg2.connect('postgresql://lukas_talaga_cspb_3308_lab_10_postgresql_user:EVJVGUJi7oBvBRLjnN7km0zZmVBzwrDv@dpg-cvldj32dbo4c73dai8d0-a/lukas_talaga_cspb_3308_lab_10_postgresql') # connects to the PostgreSQL database
    cur = conn.cursor() # create a cursor to interact with database data
    # uses SQL to create sample table
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit() # commits changes to the db
    conn.close() # close the db connection
    return "Basketball Table Successfully Dropped" # return verification that the function ran