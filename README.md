# Label Flow

A simple tool to scan barcodes, save them in an Excel file, and prepare for label printing.

## How it works

Scan barcodes using your scanner — it acts like a keyboard.  
Each scan is saved with a timestamp.  
Data is stored in an Excel file (`barcodes.xlsx`).  
Type `exit` to stop scanning.

## How to set up

Fork or clone the repository:

```bash
git clone https://github.com/engilorian/labelflow.git
```

Change into the project directory:

```bash
cd labelflow
```

(Recommended) Create and activate a virtual environment:

```bash
python -m venv env

. env/Scripts/activate
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

## How to use

Run the program:

```bash
python main.py
```

- Scan barcodes (press Enter after each).
- Type exit and press Enter to finish.
- Your data will be saved in barcodes.xlsx.