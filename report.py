import webbrowser

from fpdf import FPDF

import os



class PdfReport:
    """
    Creates a Pdf file that contains data about the
    flatmates such  as their names, their due amounts,
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        #Add icon
        pdf.image("files/house.png", w=50, h=50)

        # Add Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        #Insert Bill period  and value
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=120, h=40, txt="Period: ", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Due amount for Flatmate1
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=120, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)

        # Due amount for Flatmate2
        pdf.cell(w=120, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate2.pays(bill, flatmate1)), border=0, ln=1)

        os.chdir("files")
        pdf.output(self.filename)

        webbrowser.open(self.filename)