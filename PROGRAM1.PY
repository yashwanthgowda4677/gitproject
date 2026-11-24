from flask import Flask, request, jsonify
app = Flask(__name__)

# Store orders temporarily.
orders = []


# Add a new order.
@app.route('/addOrder', methods=['POST'])
def add_order():
	data = request.get_json()
	if not data or not data.get('customer'):
		return jsonify({
			"success": False,
			"message": "Customer name is required"
		}), 400

	if not data.get('product'):
		return jsonify({
			"success": False,
			"message": "Product name is required"
		}), 400

	order = {
		"id": len(orders) + 1,
		"customer": data['customer'],
		"product": data['product'],
		"quantity": data.get('quantity', 1)
	}
	orders.append(order)
	return jsonify({
		"success": True,
		"message": "Order added successfully",
		"order": order
	}), 201


# Display all orders.
@app.route('/showOrders', methods=['GET'])
def show_orders():
	return jsonify({
		"success": True,
		"total_orders": len(orders),
		"orders": orders
	})


if __name__ == '__main__':
	app.run(debug=True)