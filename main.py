from flask import Flask, flash, redirect, render_template, request, session
from helpers import apology
import calculations
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/quadratics", methods=["GET", "POST"])
def quadratics():
    if request.method == "POST":
        a = request.form.get("A")
        b = request.form.get("B")
        c = request.form.get("C")

        sol = calculations.solve_quadratic(a,b,c)
        print(sol)
        print(a,b,c)

        return render_template("quadratics.html", sol=sol, len=len(sol), abc=[float(a), float(b), float(c)])

    return render_template("quadratics.html")


@app.route("/quadratics/practice", methods=["GET"])
def quadratic_practice():
    thing = calculations.generate_quadratic()
    sol = thing[0]

    return render_template("quadratics_practice.html", sol=sol, len=len(sol), abc=[float(a) for a in thing[1]])

@app.route('/figures', methods=["GET"])
def figures():
    return render_template("figures.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
   app.run()
