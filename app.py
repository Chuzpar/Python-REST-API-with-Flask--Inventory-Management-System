from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)