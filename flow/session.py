from datetime import datetime

from flow.label_print import print_labels
from flow.spreadsheet import append_to_spreadsheet


def prompt_po_and_starting_asset():
    po_number = input("Enter PO Number: ").strip()
    while not po_number:
        po_number = input("PO Number cannot be empty. Enter PO Number: ").strip()

    start_asset_tag = input("Enter starting Asset Tag Number: ").strip()
    while not start_asset_tag.isdigit():
        start_asset_tag = input("Invalid. Enter a numeric starting Asset Tag Number: ").strip()

    return po_number, int(start_asset_tag)

def get_next_asset_entry(asset_tag, po_number):
    serial_num = input(f"  Scan Serial Number for Asset Tag {asset_tag}: ").strip()
    if serial_num.lower() == 'exit':
        return None
    if not serial_num:
        print("  ⚠️  Serial number cannot be empty.")
        return get_next_asset_entry(asset_tag, po_number)

    return {
        'asset_tag': str(asset_tag),
        'serial_num': serial_num,
        'po_num': po_number,
        'timestamp': datetime.now().isoformat(timespec='seconds')
    }

def run_asset_tagging_session():
    print("==== EPISD Asset Tagging ====")
    po_number, asset_tag = prompt_po_and_starting_asset()

    entries = []
    print("\nType 'exit' at any serial number prompt to finish.\n")
    count = 1
    while True:
        print(f"\nDevice [{count}]:")
        entry = get_next_asset_entry(asset_tag, po_number)
        if entry is None:
            break

        entries.append(entry)
        print(f"✅ Recorded: Asset Tag={asset_tag}, Serial={entry['serial_num']}, PO={po_number}")
        print_labels([entry, entry])

        asset_tag += 1
        count += 1

    if entries:
        append_to_spreadsheet(entries)
        print(f"✅ {len(entries)} assets logged and exported to Excel.")
    else:
        print("No assets entered.")
