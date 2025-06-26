from flow.barcode_logger import scan_barcodes
from flow.spreadsheet import append_to_spreadsheet


def main():
    entries = scan_barcodes()
    if entries:
        append_to_spreadsheet(entries)
        # print_labels(entries)  # Uncomment when ready

if __name__ == '__main__':
    main()
