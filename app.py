from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = [
    {
        "id": 1,
        "product_name": "Organic Almond Milk",
        "brands": "silk",
        "ingredients_text": "Filtered water, almonds, cane sugar",
        "price": 4.99,
        "stock": 12
    },
    {
        "id": 2,
        "product_name": "Peanut Butter",
        "brands": "Skippy",
        "ingredients_text": "Peanuts, sugar, vegetable oils",
        "price": 3.49,
        "stock": 20
    }
]

@app.route("/")
def home():
    return "Inventory API is running!"

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):

    for item in inventory:

        if item["id"] == item_id:
            return jsonify(item), 200
        
    return jsonify({"error": "Item not found"}), 404

@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "product_name": data.get("product_name"),
        "brands": data.get("brands"),
        "ingredients_text": data.get("ingredients_text"),
        "price": data.get("price"),
        "stock": data.get("stock")   
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

if __name__ == "__main__":
    app.run(debug=True)