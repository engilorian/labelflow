from flow.barcode_logger import scan_barcodes
from flow.spreadsheet import append_to_spreadsheet
from flow.label_print import print_labels


def main():
    print("Choose printing mode:")
    print("1 - Print label immediately after each scan")
    print("2 - Scan all barcodes first, then print all labels")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        entries = scan_barcodes(print_immediately=True, print_callback=print_labels)
        if entries:
            append_to_spreadsheet(entries)
        print("Done.")
    elif choice == '2':
        entries = scan_barcodes()
        if entries:
            append_to_spreadsheet(entries)
            print_labels(entries)
        print("Done.")
    else:
        print("Invalid choice. Exiting.")

if __name__ == '__main__':
    main()
