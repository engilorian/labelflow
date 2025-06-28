import win32com.client
from flow.config import LABEL_FILE, PRINTER_NAME


def print_labels(entries):
    dymo = win32com.client.Dispatch("Dymo.DymoAddIn")
    label = win32com.client.Dispatch("Dymo.DymoLabels")

    if not dymo.Open(LABEL_FILE):
        raise Exception(f"Could not open label file at {LABEL_FILE}")

    for entry in entries:
        code = entry["barcode"]
        label.SetField("Barcode", code)
        label.SetField("Text", code)
        dymo.SelectPrinter(PRINTER_NAME)
        dymo.Print(1, False)
        print(f"Printed: {code}")

    print("All labels printed.")
