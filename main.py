from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")