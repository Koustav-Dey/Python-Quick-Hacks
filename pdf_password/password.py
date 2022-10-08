from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass

pdfwriter = PdfFileWriter()
pdf = PdfFileReader('pdf_password//Python Book.pdf')
for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))
password = getpass.getpass(prompt = 'Enter Password : ')
pdfwriter.encrypt(password)

with open('pdf_password//Python Book.pdf','wb') as f:
    pdfwriter.write(f)
    
print("Now the file is password protected")