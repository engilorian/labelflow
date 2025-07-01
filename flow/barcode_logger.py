from datetime import datetime


def scan_barcodes():
    print("✅ Scanner Ready: Scan barcodes now.")
    print("ℹ️  Type 'exit' and hit Enter to stop scanning.\n")

    entries = []
    while True:
        barcode = input("Scan: ").strip()
        if barcode.lower() == 'exit':
            break
        if not barcode:
            print("⚠️  Empty scan detected. Try again.")
            continue
        timestamp = datetime.now().isoformat(timespec='seconds')
        entries.append({'barcode': barcode, 'timestamp': timestamp})
        print(f"✅ Recorded: {barcode} at {timestamp}")
    return entries