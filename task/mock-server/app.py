from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Load data from JSON file
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'customers.json')

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)['customers']

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/customers', methods=['GET'])
def get_customers():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    
    customers = load_data()
    total = len(customers)
    
    start = (page - 1) * limit
    end = start + limit
    
    paginated_customers = customers[start:end]
    
    return jsonify({
        "data": paginated_customers,
        "total": total,
        "page": page,
        "limit": limit
    }), 200

@app.route('/api/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    customers = load_data()
    customer = next((c for c in customers if c['customer_id'] == customer_id), None)
    
    if customer:
        return jsonify(customer), 200
    else:
        return jsonify({"error": "Customer not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
