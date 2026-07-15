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



while True:

    menu()

    choice = input("Choose an option: ")

    if choice == "1":

          view_inventory()

    elif choice == "6":

        print("Goodbye!")

    break
    if choice == "6":

        print("Goodbye!")

        break