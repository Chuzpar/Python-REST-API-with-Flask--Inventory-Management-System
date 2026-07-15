from unittest.mock import patch
from openfoodfacts import get_product_by_barcode


@patch("openfoodfacts.requests.get")
def test_get_product_by_barcode(mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Organic Almond Milk",
            "brands": "Silk",
            "ingredients_text": "Filtered water, almonds"
        }
    }

    product = get_product_by_barcode("123456")

    assert product["product_name"] == "Organic Almond Milk"

    assert product["brands"] == "Silk"