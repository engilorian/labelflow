from datetime import datetime


def scan_barcodes():
    print("Scan barcodes. Press Enter after each. Type 'exit' to finish.")
    entries = []
    while True:
        barcode = input("Scan: ").strip()
        if barcode.lower() == 'exit':
            break
        timestamp = datetime.now().isoformat(timespec='seconds')
        entries.append({'barcode': barcode, 'timestamp': timestamp})
        print(f"Recorded: {barcode} at {timestamp}")
    return entries
