from flask import Flask, render_template, request, jsonify
from datetime import datetime
 
app = Flask(__name__)
 
# --------- Fake in-memory "database" ---------
accounts = {
    "1001": {
        "name": "Everyday Checking",
        "currency": "CAD",
        "balance": 1500.00,
        "transactions": [
            {
                "type": "Deposit",
                "amount": 1500.00,
                "description": "Initial funding",
                "time": "2025-01-01 10:00:00"
            }
        ],
    },
    "2001": {
        "name": "Savings Plus",
        "currency": "CAD",
        "balance": 3200.50,
        "transactions": [
            {
                "type": "Deposit",
                "amount": 3200.50,
                "description": "Savings transfer",
                "time": "2025-01-05 09:30:00"
            }
        ],
    },
    "3001": {
        "name": "USD Travel Account",
        "currency": "USD",
        "balance": 800.00,
        "transactions": [
            {
                "type": "Deposit",
                "amount": 800.00,
                "description": "Vacation money",
                "time": "2025-02-10 14:15:00"
            }
        ],
    },
}
 
 
# --------- Routes ---------
 
@app.route("/")
def index():
    # just renders the HTML, JS will call the APIs
    return render_template("index.html")
 
 
@app.route("/api/accounts", methods=["GET"])
def list_accounts():
    """Return basic info for all accounts (for sidebar)."""
    result = []
    for acc_id, data in accounts.items():
        result.append({
            "id": acc_id,
            "name": data["name"],
            "currency": data["currency"],
            "balance": data["balance"],
        })
    return jsonify(result)
 
 
@app.route("/api/accounts/<account_id>", methods=["GET"])
def get_account(account_id):
    acc = accounts.get(account_id)
    if not acc:
        return jsonify({"error": "Account not found"}), 404
    return jsonify({
        "id": account_id,
        "name": acc["name"],
        "currency": acc["currency"],
        "balance": acc["balance"],
        "transactions": acc["transactions"],
    })
 
 
@app.route("/api/accounts/<account_id>/deposit", methods=["POST"])
def deposit(account_id):
    acc = accounts.get(account_id)
    if not acc:
        return jsonify({"error": "Account not found"}), 404
 
    data = request.get_json(force=True)
    amount = float(data.get("amount", 0))
    description = data.get("description", "Deposit")
 
    if amount <= 0:
        return jsonify({"error": "Amount must be positive"}), 400
 
    acc["balance"] += amount
    acc["transactions"].insert(0, {
        "type": "Deposit",
        "amount": amount,
        "description": description,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })
 
    return jsonify({
        "id": account_id,
        "balance": acc["balance"],
        "transactions": acc["transactions"],
    })
 
 
@app.route("/api/accounts/<account_id>/withdraw", methods=["POST"])
def withdraw(account_id):
    acc = accounts.get(account_id)
    if not acc:
        return jsonify({"error": "Account not found"}), 404
 
    data = request.get_json(force=True)
    amount = float(data.get("amount", 0))
    description = data.get("description", "Withdrawal")
 
    if amount <= 0:
        return jsonify({"error": "Amount must be positive"}), 400
    if amount > acc["balance"]:
        return jsonify({"error": "Insufficient funds"}), 400
 
    acc["balance"] -= amount
    acc["transactions"].insert(0, {
        "type": "Withdrawal",
        "amount": amount,
        "description": description,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })
 
    return jsonify({
        "id": account_id,
        "balance": acc["balance"],
        "transactions": acc["transactions"],
    })
 
 
if __name__ == "__main__":
    app.run(debug=True)