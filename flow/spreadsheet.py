import pandas as pd
from flow.config import EXCEL_FILE, SHEET_NAME


def append_to_spreadsheet(entries):
    try:
        df_existing = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
    except FileNotFoundError:
        df_existing = pd.DataFrame(columns=['barcode', 'timestamp'])

    df_new = pd.DataFrame(entries)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    df_combined.drop_duplicates(subset=['barcode', 'timestamp'], inplace=True)

    with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl', mode='w') as writer:
        df_combined.to_excel(writer, sheet_name=SHEET_NAME, index=False)

    print(f"Appended {len(entries)} entries to {EXCEL_FILE}")
