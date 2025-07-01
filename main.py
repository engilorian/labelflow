from flow.barcode_logger import scan_barcodes
from flow.spreadsheet import append_to_spreadsheet
from flow.label_print import print_labels


def run_immediate_mode():
    entries = scan_barcodes(print_immediately=True, print_callback=print_labels)
    if entries:
        append_to_spreadsheet(entries)

def run_batch_mode():
    entries = scan_barcodes()
    if entries:
        append_to_spreadsheet(entries)
        print_labels(entries)


def main():
    print("Choose printing mode:")
    print("1 - Print label after each scan")
    print("2 - Scan barcodes first, then print labels")
    choice = input("Enter option 1 or 2: ").strip()

    if choice == '1':
        run_immediate_mode()
    elif choice == '2':
        run_batch_mode()
    else:
        print("Invalid choice. Exiting.")

if __name__ == '__main__':
    main()
