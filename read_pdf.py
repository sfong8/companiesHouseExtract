# importing all the required modules
import PyPDF2

# creating an object
file = open('application-pdf.pdf', 'rb')

# creating a pdf reader object
# fileReader = PyPDF2.PdfFileReader(file ,strict = False)

# print the number of pages in pdf file
# print(fileReader.numPages)
import os
# import pikepdf
#
# pdf = pikepdf.Pdf.open(file)

from io import StringIO
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.high_level import extract_text


text = extract_text('application-pdf.pdf')