from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Datos mockeados - simulando BSS
MOCK_USERS = {
    "12345": {
        "id": "12345",
        "name": "Juan Pérez",
        "plan": "Premium",
        "balance": 45.50,
        "data_limit_gb": 50,
        "minutes_limit": 1000,
        "data_consumed_gb": 32.5,
        "minutes_consumed": 450,
        "last_updated": datetime.now().isoformat()
    },
    "67890": {
        "id": "67890", 
        "name": "María García",
        "plan": "Basic",
        "balance": 12.30,
        "data_limit_gb": 20,
        "minutes_limit": 500,
        "data_consumed_gb": 8.2,
        "minutes_consumed": 120,
        "last_updated": datetime.now().isoformat()
    }
}

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/api/customer/<customer_id>/consumption', methods=['GET'])
def get_customer_consumption(customer_id):
    try:
        if customer_id not in MOCK_USERS:
            return jsonify({"error": "Customer not found"}), 404
        
        user = MOCK_USERS[customer_id]
        
        # Simular consumo en tiempo real con pequeñas variaciones
        current_data = user["data_consumed_gb"] + random.uniform(0, 0.5)
        current_minutes = user["minutes_consumed"] + random.randint(0, 10)
        
        response = {
            "customer_id": user["id"],
            "customer_name": user["name"],
            "plan": user["plan"],
            "balance": user["balance"],
            "data": {
                "consumed_gb": round(current_data, 2),
                "limit_gb": user["data_limit_gb"],
                "remaining_gb": round(user["data_limit_gb"] - current_data, 2),
                "usage_percentage": round((current_data / user["data_limit_gb"]) * 100, 1)
            },
            "minutes": {
                "consumed": current_minutes,
                "limit": user["minutes_limit"],
                "remaining": user["minutes_limit"] - current_minutes,
                "usage_percentage": round((current_minutes / user["minutes_limit"]) * 100, 1)
            },
            "last_updated": datetime.now().isoformat()
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500

@app.route('/api/customers', methods=['GET'])
def get_customers():
    """Endpoint para obtener lista de clientes disponibles"""
    customers = []
    for user_id, user_data in MOCK_USERS.items():
        customers.append({
            "id": user_data["id"],
            "name": user_data["name"],
            "plan": user_data["plan"]
        })
    return jsonify(customers)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)