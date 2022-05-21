from flask import Flask, flash, redirect, render_template, request, session
from helpers import apology
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
