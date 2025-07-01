from datetime import datetime


def prompt_input(field_name):
    """Prompt user for input and handle 'exit' command."""
    value = input(f"  Scan or enter {field_name}: ").strip()
    if value.lower() == 'exit':
        return None
    if not value:
        print(f"⚠️ {field_name} cannot be empty. Please enter a value.")
        return prompt_input(field_name)
    return value

def record_asset(count, print_immediately=False, print_callback=None):
    """Prompt for one asset's data, optionally print, and return entry dict."""
    print(f"\nAsset [{count}]:")
    
    asset_tag = prompt_input("Asset Tag Number")
    if asset_tag is None:
        return None

    serial_num = prompt_input("Serial Number")
    if serial_num is None:
        return None

    po_num = prompt_input("PO Number")
    if po_num is None:
        return None

    timestamp = datetime.now().isoformat(timespec='seconds')
    entry = {
        'asset_tag': asset_tag,
        'serial_num': serial_num,
        'po_num': po_num,
        'timestamp': timestamp
    }
    print(f"✅ Recorded asset: Asset Tag={asset_tag}, Serial={serial_num}, PO={po_num} at {timestamp}")

    if print_immediately and print_callback:
        try:
            print_callback([entry])
            print(f"🖨️ Printed label for Asset Tag: {asset_tag}")
        except Exception as e:
            print(f"⚠️ Error printing label: {e}")

    return entry

def scan_assets(print_immediately=False, print_callback=None):
    print("✅ Ready: Enter asset data for each label.")
    print("ℹ️  Type 'exit' at any prompt to finish.\n")

    entries = []
    count = 1

    while True:
        entry = record_asset(count, print_immediately, print_callback)
        if entry is None:
            break
        entries.append(entry)
        count += 1

    print(f"\n🎯 Data entry complete. Total assets entered: {len(entries)}")
    return entries
