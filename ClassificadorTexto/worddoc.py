data = open('ata.doc','r',encoding='ISO-8859-1').read()

print(type(data))


from docx import Document

doc = Document('ata.doc')

import re

regex = re.compile(r'[\w\s\\/,ºª°?!()\.\:\- ]+')

regex.findall(data)

data.find('PROPOSIÇÕES')
data.find('PEQUENO EXPEDIENTE')
re.compile(r'Requerimento [\w\(\)\\ºª°/\. ]+')