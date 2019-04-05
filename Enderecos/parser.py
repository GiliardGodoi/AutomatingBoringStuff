# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 09:14:05 2019

@author: Giliard A Godoi
"""
import os
from bs4 import BeautifulSoup as bsp
import re
import csv

arquivo = os.path.join('pagina-web','Resultado Pesquisa — Portal da Câmara dos Deputados.html')
html_doc = open(arquivo,'r',encoding='utf-8').read() # iso-8859-1 latin-1
soup = bsp(html_doc,'html.parser')
print(soup.title)

links = soup.find_all('a',href=True)

deputados = [ a['href'] for a in links if ( '/deputado/Dep_Detalhe.asp?id' in a['href'] ) ]

links = soup.find_all('ul',class_='visualNoMarker')

print(len(links))

regex = re.compile('\n+\t+')

def get_data_from(ul):
    elem = ul.find_all('li')
    
    text = elem[0].text.strip()
    texts = [ t.strip().replace(' - ',',') for t in regex.split(text)]
    texts = sum([ t.split(',') for t in texts ],[])
    
    return texts

def limpar_attr_partidoUF(atributo):
    return atributo.replace('Partido/UF:','').strip()

dados = list()

for ul in links:
    line = get_data_from(ul)
    line[1] = limpar_attr_partidoUF(line[1])
    dados.append(line)

outputfile = 'deputados-federais.csv'

with open(outputfile,'w',newline='\n') as csvfile:
    fieldnames = ['Nome','Partido/UF','Gabinete','Anexo','Telefone','Fax','Email']
    csvWriter = csv.writer(csvfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    
    for line in dados:
        csvWriter.writerow(line)
    
    csvfile.close()