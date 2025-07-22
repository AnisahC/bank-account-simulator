from flask import Flask, render_template, request, session, redirect, url_for
from checking_account import CheckingAccount

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # still fine for now

@app.route('/', methods = ["GET", "POST"])
def home():
    if "name" not in session:
        return redirect(url_for("setup"))
    
    account = CheckingAccount(session["name"], session["balance"])

    message = None

    # Handle deposit
    if request.method == "POST":
        action = request.form.get("action")
        amount = float(request.form.get("amount", 0))

        if action == "deposit":
            account.deposit(amount)
            message = f"Deposited ${amount:.2f} successfully!"
        elif action == "withdraw":
            old_balance = account.balance
            account.withdraw(amount)
            if amount > old_balance:
                message = f"You're broke, you only have ${old_balance:.2f} lol. Go ask your mom for money."
            else:
                message = f"You withdrew ${amount:.2f} and now have a balance of ${account.balance:.2f}"
        session["balance"] = account.balance

    return render_template(
        "index.html",
        name=account.name,
        balance=account.balance,
        message = message
    )

@app.route("/setup", methods=["GET", "POST"])
def setup():
    if request.method == "POST":
        # Get user input
        name = request.form.get("name")
        balance = float(request.form.get("balance", 0))

        # Save in session
        session["name"] = name
        session["balance"] = balance

        return redirect(url_for("home"))

    return render_template("setup.html")

@app.route("/reset")
def reset():
    # Clear session (start over)
    session.clear()
    return redirect(url_for("setup"))

if __name__ == "__main__":
    app.run(debug=True)