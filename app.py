from flask import Flask, render_template, request
from checking_account import CheckingAccount

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # still fine for now

account = CheckingAccount("Anisah", 500)

@app.route('/', methods = ["GET", "POST"])
def home():
    global account
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

    return render_template(
        "index.html",
        name=account.name,
        balance=account.balance,
        message = message
    )

if __name__ == "__main__":
    app.run(debug=True)