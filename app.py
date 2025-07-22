from flask import Flask, render_template, request
from checking_account import CheckingAccount

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # still fine for now

account = CheckingAccount("Anisah", 1000)

@app.route('/', methods = ["GET", "POST"])
def home():
    global account

    # Handle deposit
    if request.method == "POST":
        action = request.form.get("action")
        amount = float(request.form.get("amount", 0))

        if action == "deposit":
            account.deposit(amount)
        elif action == "withdraw":
            account.withdraw(amount)

    return render_template(
        "index.html",
        name=account.name,
        balance=account.balance
    )

if __name__ == "__main__":
    app.run(debug=True)