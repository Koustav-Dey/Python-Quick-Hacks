from pdf2docx import Converter

pdf = 'Python Book.pdf'
doc = 'sample.docx'
cv = Converter(pdf)
cv.convert(doc)
cv.close()
