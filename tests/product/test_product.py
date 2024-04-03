from inventory_report.product import Product


def test_create_product() -> None:
    product_data = {
        "id": "1",
        "product_name": "Mouse Gamer",
        "company_name": "Logitech",
        "manufacturing_date": "10/01/2024",
        "expiration_date": "10/01/2033",
        "serial_number": "123456789",
        "storage_instructions": "frágil",
    }

    product = Product(**product_data)

    for key, value in product_data.items():
        assert getattr(product, key) == value
