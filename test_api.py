from openfoodfacts import get_product_by_barcode

product = get_product_by_barcode("5449000000996")

if product:
    print("Product Name:", product.get("product_name"))
    print("Brand:", product.get("brands"))
else:
    print("Product not found")
