import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Profolio of clinic"""

    # get user's clinic profolio
    cprofolio = db.execute("SELECT clinic_number, name, service, number_of_room FROM profolio WHERE user_id = :user_id GROUP BY clinic_number",
                        user_id=session["user_id"])

    print(cprofolio)


    # iterate clinic profolio under the user id
    for clinic in cprofolio:
        quote = lookup(str(clinic["clinic_number"]))
        if quote is not None:
             clinic["name"] = quote["name"]
             clinic["service"] = quote["service"]
             clinic["number_of_room"] = quote["number_of_room"]
        else:
            print(f"Lookup failed for clinic number: {clinic['clinic_number']}")


    return render_template("index.html", profolio=cprofolio)


@app.route("/finding", methods=["GET", "POST"])
@login_required
def finding():
    """Inspection findings checked in this inspection"""
    if request.method == "POST":
        clinic_number = request.form.get("clinic_number")
        name = request.form.get("name")
        inspection_finding = request.form.get("inspection_finding")
        regulatory_action = request.form.get("regulatory_action")
        inspection_date = request.form.get("inspection_date")

        print(clinic_number)
        print(name)
        print(inspection_finding)
        print(regulatory_action)
        print(inspection_date)

        if not clinic_number or not name or not inspection_finding or not regulatory_action or not inspection_date:
            return apology("please provide inspection info")

        db.execute("INSERT INTO record (user_id, clinic_number, name, regulatory_action, inspection_finding, inspection_date) VALUES(:user_id, :clinic_number, :name, :regulatory_action, :inspection_finding, :inspection_date)",
           user_id=session["user_id"], clinic_number=clinic_number, name=name, regulatory_action=regulatory_action, inspection_finding=inspection_finding, inspection_date=inspection_date)

        flash(f"Inspection record of clinic number: {clinic_number} {[name]} is added on {inspection_date}")
        return redirect("/")
    else:
        return render_template("buy.html")




@app.route("/history")
@login_required
def history():
    """Inspection finding history"""
    chistory = db.execute("SELECT * FROM record WHERE user_id =:user_id ORDER BY inspection_date DESC", user_id=session["user_id"])

    print(chistory)

    # iterate clinic profolio under the user id
    for crecord in chistory:
        quote = lookup(str(crecord["clinic_number"]))
        if quote is not None:
             crecord["name"] = quote["name"]
             crecord["inspection_finding"] = quote["inspection_finding"]
             crecord["regulatory_action"] = quote["regulatory_action"]
             crecord["inspection_date"] = quote["inspection_date"]
        else:
            print(f"Lookup failed for clinic number: {crecord['clinic_number']}")

    return render_template("history.html", history=chistory)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Inspector Log in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Quote Clinic info"""
    if request.method == "POST":
        clinic_number = request.form.get("clinic_number")
        quote = lookup(clinic_number)
        if not quote:
            return apology("invalid info", 400)
        return render_template("quote.html", quote=quote)
    else:
        return render_template("quote.html")




@app.route("/register", methods=["GET", "POST"])
def register():
    """Register new inspector account"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via GET)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username, 400")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password, 400")

        # Ensure password was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm password, 400")

        # Ensure password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match, 400")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username does not already exist
        if len(rows) != 0:
            return apology("username already exists, 400")

        # insert new user into database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                   request.form.get("username"), generate_password_hash(request.form.get("password")))

        # Query database for newly added user
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to login form
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/reply", methods=["GET", "POST"])
@login_required
def reply():
    """Follow-up reply from the clinic"""
    if request.method == "GET":
        user_id = session["user_id"]
        symbols_user = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", user_id)
        return render_template("sell.html", symbols=[row["symbol"] for row in symbols_user])
    else:
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        if not symbol:
                return apology("Must Give Symbol")

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol Does Not Exist")

        if shares < 0:
            return apology("Share Not Allowed")

        transaction_value = shares * stock["price"]

        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_cash = user_cash_db[0]["cash"]

        user_shares = db.execute("SELECT shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol", user_id, symbol)
        user_shares_real = user_shares[0]["shares"]

        if shares > user_shares_real:
            return apology("You Do Not Have This Amount Od Shares")

        uptd_cash = user_cash + transaction_value

        db.execute("UPDATE users SET cash = ? WHERE id = ?", uptd_cash, user_id)

        date = datetime.datetime.now()

        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)", user_id, stock["symbol"], (-1)*shares, stock["price"], date)

        flash("Sold!")

        return redirect("/")
