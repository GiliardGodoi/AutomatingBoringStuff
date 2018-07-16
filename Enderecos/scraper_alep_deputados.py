from bs4 import BeautifulSoup
import requests as req
import json
import re

def obter_link_perfil_deputados():
    PRINCIPAL = 'http://www.alep.pr.gov.br/deputados'
    html = req.get(PRINCIPAL)
    soup = BeautifulSoup(html.content,'html.parser')
    links = soup.find_all(href=re.compile('perfil'))
    links = map(lambda item: item.get('href'), links)
    deputados = set(links)
    return deputados

def obter_dados_deputados(link):
    print(link)
    html = req.get(link)
    soup = BeautifulSoup(html.content, 'html.parser')
    registro = obter_nome_deputado(soup)
    registro['site'] = link
    registro['endereco'] = obter_endereco()
    registro['cargo'] = 'Deputado Estadual'

    contato = obter_informacoes_contato(soup)

    if contato != {} :
        if 'Localização do Gabinete' in contato :
            registro['endereco']['complemento'] = contato['Localização do Gabinete']
            del contato['Localização do Gabinete']
        registro.update(contato)        

    return registro


def obter_nome_deputado(soup):
    divNome = soup.find('p', attrs={'class': 'nome'})
    nome = divNome.text
    span = divNome.find('span')
    funcao = ''
    if span:
        funcao = span.text.strip('\n').strip()
    resultado = dict()
    resultado['nome'] = re.sub(funcao,'',nome).strip()
    if funcao != '':
        resultado['funcao'] = funcao

    return resultado

def obter_informacoes_contato(soup):
    divDados = soup.find('div', attrs={'class': 'redes'})
    lstContato = divDados.text.strip('\n').split('\n')
    resultado = dict()
    for item in lstContato:
        index = item.find(':')
        if index and index >= 0:
            key,value = item.split(':')
            key = key.strip(' ').strip('\n')
            value = value.strip(' ').strip('\n')
            resultado[key] = value

    return resultado

def obter_endereco():
    endereco = dict()
    endereco['municipio'] = 'Curitiba'
    endereco['estado'] = 'Paraná'
    endereco['UF'] = 'PR'
    endereco['cep'] = '80.530-911'
    endereco['logradouro'] = 'Praça Nossa Senhora de Salete'
    endereco['numero'] = 's/n'
    endereco['instituicao'] = 'Assembléia Legislativa do Estado do Paraná'

    return endereco

#file.write(json.dumps(dep,ensure_ascii=False,indent=2))
if __name__ == '__main__':
    print("stating process...")
    links = obter_link_perfil_deputados()
    resultado = []    
    for link in links:
        tmp = obter_dados_deputados(link)
        resultado.append(tmp)

    print("saving..")
    with open('teste.json','w') as arquivo:
        arquivo.write(json.dumps(resultado,ensure_ascii=False,indent=2))
    print('exit!')