from flask import Flask, render_template, request, url_for, flash, redirect, jsonify, make_response
from ConnectionManager import getConnection, closeConnection

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

# This allows the table to get the departments from the DB.
# It has the ability to get single departments, or multiple using "all" or by separating the deptnos with commas.
@app.route("/get/<string:deptno>", methods = ["POST"])
def get(deptno):
    # Removing spaces from deptno
    deptno = "".join(deptno.split(" "))

    # Gets the connection and cursor, and also as creates the data variable.
    conn = getConnection()
    cursor = conn.cursor()
    data = []

    # Checks if deptno is "all", in which case it collects all the data.
    if deptno == "all":
        cursor.execute("SELECT * FROM dept;")
        data.append(cursor.fetchall())
    # If deptno is not "all", only the departments that have their deptno in the string are collected.
    else:
        for dptno in deptno.split(","):
            cursor.execute("SELECT * FROM dept WHERE deptno = %s".encode(), dptno)
            data.append(cursor.fetchall())
    
    # Closes the cursor and returns the data
    cursor.close()
    return jsonify(data)

@app.route("/create", methods=["POST"])
def create():
    return "create: " + request.json.deptno

@app.route("/edit", methods=["POST"])
def edit():
    return "edit: " + request.json.deptno

@app.route("/delete", methods=["POST"])
def delete():
    return "delete: " + request.json.deptno

if __name__ == "__main__":
    app.run(port=80, host="localhost")