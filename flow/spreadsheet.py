import os
from datetime import datetime
import pandas as pd

from flow.config import SHEET_NAME


def append_to_spreadsheet(entries, base_filename="barcodes"):
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
    os.makedirs(data_dir, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    excel_filename = f"{base_filename}_{date_str}.xlsx"
    excel_path = os.path.join(data_dir, excel_filename)
    columns = ['asset_tag', 'serial_num', 'po_num', 'timestamp']
    if os.path.exists(excel_path):
        df_existing = pd.read_excel(excel_path, sheet_name=SHEET_NAME)
    else:
        df_existing = pd.DataFrame(columns=columns)
    df_new = pd.DataFrame(entries)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    df_combined.drop_duplicates(subset=columns, inplace=True)
    with pd.ExcelWriter(excel_path, engine='openpyxl', mode='w') as writer:
        df_combined.to_excel(writer, sheet_name=SHEET_NAME, index=False)
    print(f"Appended {len(entries)} entries to {excel_path}")
