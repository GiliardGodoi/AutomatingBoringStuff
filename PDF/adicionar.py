import PyPDF2

fileOne = "BRW7440BBC8587C_000675.pdf"
fileTwo = "Anotacoes.pdf"

fileObjOne = open(fileOne,'rb')
fileObjTwo = open(fileTwo,'rb')

pdfReaderOne = PyPDF2.PdfFileReader(fileOne)
pdfReaderTwo = PyPDF2.PdfFileReader(fileTwo)

pdfWriter = PyPDF2.PdfFileWriter()

pdfWriter.appendPagesFromReader(pdfReaderOne)
pdfWriter.appendPagesFromReader(pdfReaderTwo)

outputFile = open('Output.pdf','wb')

pdfWriter.write(outputFile)
