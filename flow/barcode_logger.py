from datetime import datetime


def scan_barcodes(print_immediately=False, print_callback=None):
    print("✅ Ready: Scan barcodes now.")
    print("ℹ️  Type 'done' and press Enter to finish.\n")

    entries = []

    while True:
        barcode = input("Scan: ").strip()
        if barcode.lower() == 'done':
            break
        if not barcode:
            print("⚠️ Empty scan detected. Try again.")
            continue

        timestamp = datetime.now().isoformat(timespec='seconds')
        entries.append({'barcode': barcode, 'timestamp': timestamp})
        print(f"✅ Recorded: {barcode} at {timestamp}")

        if print_immediately and print_callback:
            try:
                print_callback([{'barcode': barcode, 'timestamp': timestamp}])
            except Exception as e:
                print(f"⚠️ Error printing label: {e}")

    return entries
