# Label Flow

A user-friendly tool for scanning barcodes, automatically saving them in an Excel file, and instantly printing barcode labels using your DYMO LabelWriter.


## Features

Scan barcodes (your scanner acts like a keyboard)
Instantly print a label for each scanned barcode
Data is automatically saved in barcodes.xlsx (timestamped log)
No technical knowledge required after setup

## Prerequisites
1. DYMO LabelWriter printer (set up and connected to your computer)
2. DYMO Label Software v8 installed
    - Download from: DYMO Official Support
3. Python 3.10+ installed
    - Download from: python.org
4. Barcode scanner (acts as keyboard input — e.g. Tera D5100)


## One-Time Setup

1. Install DYMO Label Software v8
    - Download and install DYMO Label Software v8 (NOT DYMO Connect)
    - Plug in and set up your DYMO LabelWriter printer as described in the DYMO instructions
    - Print a test label using DYMO Label Software to confirm your printer works

2. Install Python & Project Dependencies
    - Download and install Python 3.10+ from python.org
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

3. Start scanning barcodes:
    - Scan one barcode, then press Enter
    - Repeat for each item
    - Type exit and press Enter when done


## Where to Find Your Data
- All scanned barcodes are saved in:
    ```bash
    barcodes.xlsx
    ```
- Each row: barcode, timestamp

## Troubleshooting
- Printer not printing?
    - Make sure DYMO Label Software v8 is installed
    - Printer shows as “DYMO_LabelWriter” in Devices & Printers
    - Print a test label using DYMO Label Software

- Barcode not printing as label?
    - Ensure the barcode scanner is connected and functioning
    - Reboot the printer and computer if needed

--

Label Flow: Scan. Print. Log. Done.





