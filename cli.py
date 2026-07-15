import requests

BASE_URL = "http://127.0.0.1:5000"


def menu():

    print("\n===== Inventory Management =====")

    print("1. View Inventory")

    print("2. Add Item")

    print("3. Update Item")

    print("4. Delete Item")

    print("5. Search OpenFoodFacts")

    print("6. Exit")

def view_inventory():

    response = requests.get(BASE_URL + "/inventory")

    if response.status_code == 200:

        inventory = response.json()

        print("\nCurrent Inventory\n")

        for item in inventory:

            print(f"ID: {item['id']}")
            print(f"Product: {item['product_name']}")
            print(f"Brand: {item['brands']}")
            print(f"Price: ${item['price']}")
            print(f"Stock: {item['stock']}")
            print("--------------------------")

    else:

        print("Unable to retrieve inventory.")

def add_item():

    print("\nAdd New Item")

    product_name = input("Product Name: ")
    brands = input("Brand: ")
    ingredients = input("Ingredients: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    new_item = {
        "product_name": product_name,
        "brands": brands,
        "ingredients_text": ingredients,
        "price": price,
        "stock": stock
    }

    response = requests.post(BASE_URL + "/inventory", json=new_item)

    if response.status_code == 201:

        print("\nItem added successfully!")

    else:

        print("\nFailed to add item.")

def update_item():

    print("\nUpdate Inventory Item")

    item_id = input("Enter Item ID: ")

    price = float(input("New Price: "))

    stock = int(input("New Stock: "))

    updated_item = {
        "price": price,
        "stock": stock
    }

    response = requests.patch(
        BASE_URL + "/inventory/" + item_id,
        json=updated_item
    )

    if response.status_code == 200:

        print("\nItem updated successfully!")

    else:

        print("\nItem not found.")

def delete_item():

    print("\nDelete Inventory Item")

    item_id = input("Enter Item ID: ")

    response = requests.delete(BASE_URL + "/inventory/" + item_id)

    if response.status_code == 200:

        print("\nItem deleted successfully!")

    else:

        print("\nItem not found.")

def search_product():

    print("\nSearch OpenFoodFacts")

    barcode = input("Enter barcode: ")

    response = requests.get(BASE_URL + "/search/" + barcode)

    if response.status_code == 200:

        product = response.json()

        print("\nProduct Found\n")

        print("Product Name:", product.get("product_name"))

        print("Brand:", product.get("brands"))

        print("Ingredients:", product.get("ingredients_text"))

    else:

        print("Product not found.")

while True:

    menu()

    choice = input("Choose an option: ")

    if choice == "1":

        view_inventory()

    elif choice == "2":

        add_item()

    elif choice == "3":
        
        update_item()
    
    elif choice == "4":

        delete_item()

    elif choice == "5":

        search_product()

    elif choice == "6":

        print("Goodbye!")

        break

    print("\nAdd New Item")

    product_name = input("Product Name: ")
    brands = input("Brand: ")
    ingredients = input("Ingredients: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    new_item = {
        "product_name": product_name,
        "brands": brands,
        "ingredients_text": ingredients,
        "price": price,
        "stock": stock
    }

    response = requests.post(BASE_URL + "/inventory", json=new_item)

    if response.status_code == 201:

        print("\nItem added successfully!")

    else:

        print("\nFailed to add item.")

    break
    if choice == "6":

        print("Goodbye!")

        break