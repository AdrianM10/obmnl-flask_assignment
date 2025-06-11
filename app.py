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


@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    """Update transaction(s)"""

    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Extract the updated values from the form fields
        date = request.form["date"]
        amount = float(request.form["amount"])

        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transaction["date"] == date
                transaction["amount"] == amount
                break

        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transaction"))
    
    # If the request method is GET, find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)
        
    # If the transaction with the specified ID is not found, handle this case (optional)
    return {"message": "Transaction not found"}, 404


@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    """Delete transaction"""

    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            break

    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))

# Run the Flask app
