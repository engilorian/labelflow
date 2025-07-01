import win32com.client

from flow.config import LABEL_FILE, PRINTER_NAME


def print_labels(entries):
    dymo = win32com.client.Dispatch("Dymo.DymoAddIn")
    label = win32com.client.Dispatch("Dymo.DymoLabels")

    if not dymo.Open(LABEL_FILE):
        raise Exception(f"Could not open label file at {LABEL_FILE}")

    dymo.SelectPrinter(PRINTER_NAME)
    for entry in entries:
        label.SetField("ASSET_TAG", entry['asset_tag'])
        label.SetField("SERIAL_NUM", entry['serial_num'])
        label.SetField("PO_NUM", entry['po_num'])
        dymo.Print(1, False)
        print(f"Printed label for Asset Tag: {entry['asset_tag']}")

    print("All labels printed.")
