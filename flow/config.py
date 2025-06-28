import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LABEL_FILE = os.path.join(BASE_DIR, "template.label")
PRINTER_NAME = "DYMO_LabelWriter"

EXCEL_FILE = os.path.join(BASE_DIR, "barcodes.xlsx")
SHEET_NAME = "Barcodes"
