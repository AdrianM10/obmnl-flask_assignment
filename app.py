from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {"id": 1, "date": "2023-06-01", "amount": 100},
    {"id": 2, "date": "2023-06-02", "amount": -200},
    {"id": 3, "date": "2023-06-03", "amount": 300},
]

@app.route("/")
def get_transactions():
    """Retrieve all transactions"""
    return render_template("transactions.html", transactions=transactions)

@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    """Add new transaction(s)"""

    # Check if the request method is POST (form submission)
    if request.method == "POST":
        transaction = {
            "id": len(transactions) + 1,
            "date": request.form["date"],
            "amount": float(request.form["amount"])
        }

        # Append new transaction to the transaction list
        transactions.append(transaction)

        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))
    
    # If the request method is GET, render the form template to display the add transaction form
    return render_template("form.html")

# Update operation

# Delete operation

# Run the Flask app

