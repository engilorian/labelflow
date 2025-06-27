import os
import win32print
import win32api

from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import code128
from reportlab.graphics.shapes import Drawing
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import inch


LABEL_WIDTH = 2.25 * inch
LABEL_HEIGHT = 1.25 * inch
PRINTER_NAME = "Dymo_Label_Writer"

def create_label_pdf(barcode_value, filename='label.pdf'):
    c = canvas.Canvas(filename, pagesize=(LABEL_WIDTH, LABEL_HEIGHT))
    barcode = code128.Code128(barcode_value, barHeight=0.5 * inch, barWidth=1.0)
    barcode.drawOn(c, 10, LABEL_HEIGHT / 2)
    c.setFont("Helvetica", 8)
    c.drawString(10, 10, barcode_value)
    c.save()

def print_pdf(filename):
    win32api.ShellExecute(
        0,
        "printto",
        os.path.abspath(filename),
        f'"{PRINTER_NAME}"',
        ".",
        0
    )

def print_labels(entries):
    for entry in entries:
        value = entry['barcode']
        create_label_pdf(value, filename='label.pdf')
        print_pdf('label.pdf')
        print(f"Sent label for: {value}")
