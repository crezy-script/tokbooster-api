from flask import Flask, request, jsonify

app = Flask(__name__)

# Simule une base de données de clés valides
clefs_valides = {"ABC123", "XYZ789", "UNLOCKME"}

# Liste fictive des utilisateurs ayant payé
users_paid = {
    "user1@example.com": {"paid": True, "permanent_unlock": False},
    "user2@example.com": {"paid": False, "permanent_unlock": False}
}

@app.route("/")
def index():
    return "API TokBooster en ligne !"

@app.route("/unlock")
def unlock():
    key = request.args.get("key")
    if key in clefs_valides:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

@app.route('/check_payment', methods=['POST'])
def check_payment():
    data = request.get_json()  # On attend des données JSON
    email = data.get("email")  # Récupère l'email de l'utilisateur

    # Vérification de paiement
    if email in users_paid:
        user = users_paid[email]
        return jsonify({"paid": user["paid"], "permanent_unlock": user["permanent_unlock"]})
    else:
        return jsonify({"error": "Utilisateur non trouvé"}), 404

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/register_payment")
def register_payment():
    email = request.args.get("email")
    if not email:
        return jsonify({"success": False, "error": "Email manquant"})

    users_paid[email] = {"paid": True, "permanent_unlock": False}
    return jsonify({"success": True, "message": f"Paiement enregistré pour {email}"})
