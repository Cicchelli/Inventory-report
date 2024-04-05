"""Function printing python version."""

from typing import List

from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.product import Product
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    products = load_products_from_files(file_paths)
    total_inventory = Inventory(products)
    return generate_report(total_inventory, report_type)


def load_products_from_files(file_paths: List[str]) -> List[Product]:
    """Function printing python version."""

    products = []
    for file in file_paths:
        importer = get_importer(file)
        if importer:
            products += importer.import_data()
    return products


def get_importer(file_path: str):
    """Function printing python version."""
    if file_path.endswith(".json"):
        return JsonImporter(file_path)
    elif file_path.endswith(".csv"):
        return CsvImporter(file_path)
    return None


def generate_report(inventory: Inventory, report_type: str) -> str:
    """Function printing python version."""
    report = create_report(report_type)
    report.add_inventory(inventory)
    return report.generate()


def create_report(report_type: str):
    """Function printing python version."""
    if report_type == "simple":
        return SimpleReport()
    elif report_type == "complete":
        return CompleteReport()
    raise ValueError("Report type is invalid.")
