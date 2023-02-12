from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

pdfwriter = PdfFileWriter()
pdf = PdfFileReader('home.pdf')

for i in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[i])

password = getpass(prompt='Введите пороль: ')
pdfwriter.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)
