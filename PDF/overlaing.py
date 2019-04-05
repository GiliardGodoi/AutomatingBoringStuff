import PyPDF2

mainFile = "BALANCO_PATRIMONIAL_2018.pdf"
overlayFile = "assinaturas.pdf"

fileObj = open(mainFile,"rb")
pdfReader = PyPDF2.PdfFileReader(fileObj)

pdfWatermarkReader = PyPDF2.PdfFileReader(open(overlayFile,"rb"))

page = pdfReader.getPage(4)

page.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(0,pdfReader.numPages - 1):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.addPage(page)

outputFile = open("BALANCO_PATRIMONIAL_2018_ASSINADO.pdf",'wb')

pdfWriter.write(outputFile)
fileObj.close()
outputFile.close()
