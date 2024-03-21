from flask import Flask, render_template, jsonify, Response, redirect, url_for, request
from flask_cors import CORS, cross_origin
from ConnectionManager import getConnection, closeConnection
from http import HTTPStatus
import json

app = Flask(__name__)

# Regular function that checks a json for the keys in the keys array.  It makes sure that deptno can be a number, and 
def checkData(data, keys, types):
    for i in range(0, len(keys)):
        # Checking if the key exists
        try:
            print(data[keys[i]])
        except KeyError:
            return Response(status=422, message=repr(keys[i] + " not found"))
        
        # Checking if the data types of the data matches up to their intended type in the types array
        type(types[i]) == type(keys)


# Routing to the index page.
# This is the main page that displays all of the existing departments.
@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    # deptInfo = get("all").json[0]

    deptInfo = []
    return render_template("index.html", deptInfo=deptInfo)

# Routing to the create page.
# This page allows users to create new departments and add them to the database.
@app.route("/create", methods=["GET"])
def create():
    return render_template("create.html")

# Routing to the edit page.
# This page allows users to edit existing departments and change them in the database.
@app.route("/edit", methods=["GET"])
def edit():
    return render_template("edit.html")

# Routing to the delete page.
# This page allows users to delete departments and remove them from the database.
@app.route("/delete", methods=["GET"])
def delete():
    return render_template("delete.html")


# The next few routes are all part of the backend API that talks to the database.

# This route gets data from the database.
@app.route("/api/get", methods=["POST"])
@cross_origin()
def apiGet():
    input = request.json["deptno"]

    # Removing spaces from data
    input = "".join(input.split(" "))

    # Gets the connection and cursor, and also as creates the data variable.
    conn = getConnection()
    cursor = conn.cursor()
    input = []

    # Checks if the input is "all", in which case it collects all the data.
    if input == "all":
        cursor.execute("SELECT * FROM dept ORDER BY deptno;")
        input.append(cursor.fetchall())
    # If the input is not "all", only the departments that have their deptno in the string are collected.
    else:
        for deptno in input.split(","):
            cursor.execute("SELECT * FROM dept WHERE deptno = %s ORDER BY deptno".encode(), deptno)
            input.append(cursor.fetchall())
    
    # Closes the cursor and returns the data
    cursor.close()
    return jsonify(input)


# This route adds a new entry to the database.
@app.route("/api/create", methods=["POST"])
def apiCreate():
    # Getting the json data
    data = request.json

    # Validating the json data
    checkData(data, ["deptno", "dname", "location"], [int, str, str])


    try:
        print(data["deptno"])
    except KeyError:
        return Response(status=422, message="deptno not found")
    
    try:
        print(data["dname"])
    except KeyError:
        return Response(status=422, message="dname not found")
    
    try:
        print(data["location"])
    except KeyError:
        return Response(status=422, message="location not found")
    
    # Getting the connection to the database
    conn = getConnection()
    cursor = conn.cursor()

    # Adding the row to the database
    cursor.execute(f"INSERT INTO dept (deptno, dname, location) VALUES ({data["deptno"]}, '{data["deptname"]}', '{data["location"]}');")

    # Closing the cursor and commiting the changes
    cursor.close()
    conn.commit()

    return Response(status=204)

# This route changes an existing entry to the database.
@app.route("/api/edit", methods=["POST"])
def apiEdit():
    return ""

# This route deleted an existing entry to the database.
@app.route("/api/delete", methods=["POST"])
def apiDelete():
    return ""

# @app.route("/edit/<string:deptno>/<string:deptname>/<string:location>", methods=["POST"])
# def edit(deptno, deptname, location):
#     # Getting the connection to the database
#     conn = getConnection()
#     cursor = conn.cursor()

#     # Editing the row in the database
#     cursor.execute(f"UPDATE dept SET deptno = {deptno}, dname = '{deptname}', location = '{location}' WHERE deptno = {deptno};")

#     # Closing the cursor and commiting the changes
#     cursor.close()
#     conn.commit()

#     return redirect(url_for("index"))

# @app.route("/delete/<string:deptno>", methods=["POST"])
# def delete(deptno):
#     # Getting the connection to the database
#     conn = getConnection()
#     cursor = conn.cursor()

#     # Removing the row from the database
#     cursor.execute(f"DELETE FROM dept WHERE deptno = {deptno};")

#     # Closing the cursor and commiting the changes
#     cursor.close()
#     conn.commit()

#     return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=80, host="192.168.1.172")