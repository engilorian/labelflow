# Label Flow

A user-friendly tool for scanning asset tags, serial numbers, and PO numbers — automatically saving the data in timestamped Excel files and instantly printing barcode labels.


## Features

- Plug-and-scan: Your barcode scanner acts like a keyboard — just scan and go.
- Multi-field labels: Prints Asset Tag, Serial Number, and PO Number on each label.
- Instant printing or batch mode: Print labels immediately or after scanning all items.
- Automatic logging: Scanned data saved to daily Excel files (e.g., barcodes_2025-06-27.xlsx) inside the data/ folder.
- Timestamped records: Every entry includes the exact date and time scanned.
- No duplicates: Prevents duplicate entries based on all scanned fields plus timestamp.


## Prerequisites
1. DYMO LabelWriter printer (set up and connected to your computer)

2. DYMO Label Software v8 installed
    - Download from: [DYMO Official Support](https://www.dymo.com/support?cfid=dymo-compatibility-chart)

3. Python 3.10 installed
    - Download from: [python.org](https://www.python.org/downloads/release/python-3100/)]

4. Barcode scanner (acts as keyboard input — e.g. Tera D5100)


## One-Time Setup

1. Install DYMO Label Software v8
    - Download and install DYMO [Label Software v8](https://www.dymo.com/support?cfid=dymo-compatibility-chart) (NOT DYMO Connect)
    - Plug in and set up your DYMO LabelWriter printer as described in the DYMO instructions
    - Print a test label using DYMO Label Software to confirm your printer works

2. Install Python & Project Dependencies
    - Download and install Python 3.10 from [python.org](https://www.python.org/downloads/release/python-3100/)

    - Open Command Prompt and change to the project directory:

    ```bash
    cd path\to\labelflow
    ```
    - (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv env
    . env\Scripts\activate
    ```

    - Install Python requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. Check your hardware
    - Plug in your barcode scanner (no special setup needed if it works as a keyboard)
    - Plug in your DYMO LabelWriter and make sure it's recognized in Devices & Printers as DYMO_LabelWriter


## How to Use
1. Open Command Prompt and navigate to your project folder.

2. Run the tool:
    ```bash
    python main.py
    ```

3. Choose a printing mode:
    - 1 — Print each label immediately after scanning an asset
    - 2 — Scan all assets first, then print labels in batch

4. Enter data as prompted:
    - Input PO Number once at start
    - Input starting Asset Tag Number
    - Type exit at any prompt to end scanning

5. The program prints labels and saves all scanned data.


## Where to Find Your Data
- All scanned barcodes are saved automatically in the data/ folder in your project.

- A new Excel file is created each day with a name like:
    ```bash
    data/barcodes_2025-06-27.xlsx
    ```

- Columns stored per row:
    - asset_tag
    - serial_num
    - po_num
    - timestamp (ISO format date/time)

- New scans append to the existing daily file, no duplicate rows saved.

## Troubleshooting
- Printer not printing?
    - Make sure DYMO Label Software v8 is installed
    - Printer shows as “DYMO_LabelWriter” in Devices & Printers
    - Print a test label using DYMO Label Software

- Barcode not printing as label?
    - Ensure the barcode scanner is connected and functioning
    - Reboot the printer and computer if needed

- Scanner issues?
    - Confirm barcode scanner acts as keyboard input.
    - Test typing barcodes manually if needed.

--

Label Flow: Scan. Print. Log. Done.





