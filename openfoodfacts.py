import requests

def get_product_by_barcode(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") == 1:
        return data["product"]

    return None