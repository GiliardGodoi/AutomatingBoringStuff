
import speech_recognition as sr
import time
import os
import json
import re


def transcripty_audio(file_path):

    recognizer = sr.Recognizer()
    sample = sr.AudioFile(file_path)

    with sample as source:
        audio = recognizer.record(source)
        inicio = time.time()
        texto = recognizer.recognize_google(audio,language="pt-BR")
        fim = time.time()

        return texto, (fim - inicio)

def salvar_saida(content, filename):
    def save(obj,file):
        if isinstance(obj,dict):
                json.dump(obj,file)
        if isinstance(obj,str):
                file.write(obj)
        if isinstance(obj,list):
                save(obj[0],file)


    with open(filename,'w') as file:
        save(content,file)

    return True
                    

                    

if __name__ == "__main__":
    diretorio_dados = 'audios'
    audios = os.listdir(diretorio_dados)
    print(audios, end='\n\n')
    for a in audios:
        print(f'Arquivo: {os.path.join(diretorio_dados,a)}. . .',end='\r')
        texto, tempo = transcripty_audio(os.path.join(diretorio_dados,a))
        print(f'Arquivo: {a} \tTempo: {tempo}',end='\n')
        output_name = re.sub('.wav','.txt',a)
        salvar_saida(texto,output_name)
            
            