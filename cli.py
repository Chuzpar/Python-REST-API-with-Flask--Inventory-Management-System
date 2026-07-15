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


while True:

    menu()

    choice = input("Choose an option: ")

    print("You chose:", choice)

    if choice == "6":

        print("Goodbye!")

        break