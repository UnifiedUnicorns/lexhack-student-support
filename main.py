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


@app.route('/solids', methods=["GET"])
def solids():
    return render_template("solids.html")


@app.route('/solids/pyramid', methods=["GET", "POST"])
def pyramid():
    if request.method == "POST":
        height = request.form.get("height")
        base = request.form.get("base")
        slant = request.form.get("slant")
        perimeter = request.form.get("perimeter")
        sol = calculations.pyramid_calc(height,base,slant,perimeter)

        return render_template("pyramid.html", sol=sol, pers=[height, base, slant, perimeter])

    return render_template("pyramid.html")


@app.route('/solids/sphere', methods=["GET", "POST"])
def sphere():
    if request.method == "POST":
        radius = request.form.get("radius")
        sol = calculations.sphere_calc(radius)

        return render_template("sphere.html", sol=sol, r=radius)

    return render_template("sphere.html")


@app.route("/solids/cylinder", methods=["GET", "POST"])
def cylinder():
    if request.method == "POST":
        r = request.form.get("r")
        h = request.form.get("h")

        sol = calculations.cyl_calc(r, h)

        return render_template("cylinder.html", sol=sol, pers=[float(r), float(h)])

    return render_template("cylinder.html")


@app.route('/solids/prism', methods=["GET", "POST"])
def prism():
    if request.method == "POST":
        height = request.form.get("height")
        area = request.form.get("area")
        perimeter = request.form.get("perimeter")

        sol = calculations.prism_calc(height,area,perimeter)

        return render_template("prism.html", sol=sol, pers=[height,area,perimeter])

    return render_template("prism.html")


@app.route('/shapes/quadrilateral', methods=["GET", "POST"])
def quadrilaterals():
    if request.method == "POST":
        qtype = request.form.get("type")

        if qtype == "rect":
            b = request.form.get("base")
            h = request.form.get("height")

            sol = calculations.rect_calc(b,h)

            return render_template("quadrilaterals.html", sol=sol, pers=[b,h], type=qtype)
        elif qtype == "trap":
            h = request.form.get("height")
            b1 = request.form.get("base")
            b2 = request.form.get("base_2")
            s1 = request.form.get("side")
            s2 = request.form.get("side_2")

            sol = calculations.trap_calc(h, b1, b2, s1, s2)

            return render_template("quadrilaterals.html", sol=sol, pers=[float(h), float(b1), float(b2), float(s1), float(s2)], type=qtype)
        elif qtype == "rhomb":
            s = request.form.get("side")
            d1 = request.form.get("diag")
            d2 = request.form.get("diag_2")

            sol = calculations.rhomb_calc(s, d1, d2)

            return render_template("quadrilaterals.html", sol=sol, pers=[float(s), float(d1), float(d2)], type=qtype)

    return render_template("quadrilaterals.html")


@app.route('/shapes', methods=["GET"])
def shapes():
    return render_template("shapes.html")


@app.route('/shapes/circle', methods=["GET", "POST"])
def circle():
    if request.method == "POST":
        radius = request.form.get("radius")
        sol = calculations.circle_calc(radius)

        return render_template("circle.html", sol=sol, radius=radius)

    return render_template("circle.html")


@app.route('/shapes/triangle', methods=["GET", "POST"])
def triangle():
    if request.method == "POST":
        s1 = request.form.get("s1")
        s2 = request.form.get("s2")
        s3 = request.form.get("s3")
        sol = calculations.triangle_calc(s1,s2,s3)

        return render_template("triangle.html", sol=sol, pers=[float(s1),float(s2),float(s3)])

    return render_template("triangle.html")


@app.route("/shapes/regularpolygons", methods=["GET", "POST"])
def regular_polygons():
    if request.method == "POST":
        s = request.form.get("s")
        l = request.form.get("l")

        sol = calculations.calc_reg_polygon(s, l)

        return render_template("polygon.html", sol=sol, pers=[float(s), float(l)])

    return render_template("polygon.html")


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
