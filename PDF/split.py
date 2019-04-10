import PyPDF2


def create_file_from(original,paginas=[],outputfile='teste.pdf'):

    with open(outputfile,'wb') as file:
        pdfWriter = PyPDF2.PdfFileWriter()

        for pg in paginas:
            page = original.getPage(pg)
            pdfWriter.addPage(page)

        pdfWriter.write(file)


if __name__ == "__main__":
    
    inputfile = 'requerimentos.pdf'
    pdfFile = open(inputfile,'rb')
    protocolo_nro = 335

    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    for indice in range(1,61,2):
        filename = f'{protocolo_nro}-2019.pdf'
        paginas = [indice-1,indice]
        create_file_from(pdfReader,paginas,outputfile=filename)
        protocolo_nro += 1