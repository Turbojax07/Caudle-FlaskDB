from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get/<string: deptno>", methods=["GET"])
def get(deptno):
    if deptno == "all":
        return "alltables"
    
    return "table"

@app.route("/create/<int: deptno>", methods=["POST"])
def create(deptno):

    return "create"

@app.route("/edit/<int: deptno>", methods=["POST"])
def edit(deptno):

    return "edit"

@app.route("/delete/<int: deptno>", methods=["POST"])
def delete(deptno):

    return "delete"

if __name__ == "__main__":
    app.run(port=80, host="180-9GPR3F3")