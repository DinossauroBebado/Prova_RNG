from PyPDF2 import PdfFileReader


path = r"AV2_2021_1_v2.pdf"

pdf = PdfFileReader(path)

lenPdf = pdf.getNumPages()

x = pdf.getPage(0)

print(x.extractText())
