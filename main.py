from flow.barcode_logger import scan_barcodes
from flow.spreadsheet import append_to_spreadsheet
from flow.label_print import print_labels


def main():
    entries = scan_barcodes()
    if entries:
        append_to_spreadsheet(entries)
        print_labels(entries) 

if __name__ == '__main__':
    main()
