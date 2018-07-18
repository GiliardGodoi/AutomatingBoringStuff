import PyPDF2

def exemplo_01():
    fileName = 'exemplo.pdf'
    fileNameOutput = 'saida.pdf'
    pdfFileObj = open(fileName,'rb')

    ## cria um reader para leitura
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    ## Cria um objeto write
    pdfWriter = PyPDF2.PdfFileWriter()

    print(pdfReader.getNumPages())

    ## rotacionar páginas
    for num in range(pdfReader.numPages):
        rotation = 90
        if num % 2 == 0:
            rotation = rotation * -1
        page = pdfReader.getPage(num)
        page.rotateClockwise(rotation)
        pdfWriter.addPage(page)

    ## escreve o arquivo de saida
    fileOutput = open(fileNameOutput,'wb')
    pdfWriter.write(fileOutput)

    print('fim do exemplo 01')

def exemplo_02():
    fileNameInput = 'exemplo.pdf'
    fileNameOutput = 'saida.pdf'
    fileWaterMark = 'watermark.pdf'
    
    ## abre os arquivos no modo read binary
    pdfFileObj = open(fileNameInput,'rb')
    pdfWaterMarkFile = open(fileWaterMark,'rb')

    ## cria um reader para leitura
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfWaterMark = PyPDF2.PdfFileReader(pdfWaterMarkFile)
    
    waterMarkPage = pdfWaterMark.getPage(0)


    ## Cria um objeto write
    pdfWriter = PyPDF2.PdfFileWriter()
    
    ## rotacionar páginas
    for num in range(pdfReader.numPages):
        page = pdfReader.getPage(num)
        page.mergePage(waterMarkPage)
        pdfWriter.addPage(page)

    outputFile = open(fileNameOutput,'wb')
    pdfWriter.write(outputFile)

    outputFile.close()
    pdfFileObj.close()
    pdfWaterMarkFile.close()


if __name__ == "__main__":
    exemplo_02()
