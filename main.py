from fileinput import filename
from pathlib import Path

import pandas as pd
import glob
from fpdf import FPDF

filepaths = glob.glob("invoice/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name='Sheet 1')
    pdf = FPDF(orientation="p",unit="mm",format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", size=16,style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")
    #ggdgfg gfgd gfgd fgdf