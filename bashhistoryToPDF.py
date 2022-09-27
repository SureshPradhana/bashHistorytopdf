 
import fpdf

pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=14)

for history in open('.bash_history'):
    pdf.write(8,history)

pdf.output("bash.pdf")