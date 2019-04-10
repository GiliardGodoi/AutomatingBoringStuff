# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:34:29 2019

@author: User
"""

# Utilizando pathlib

#from pathlib import Path
#
#entries = Path('./')

#for entry in entries.iterdir():
#    print(entry.name)

#for entry in entries.iterdir():
#    if entry.is_file():
#        print(entry.name)
        

#entries = (entry for entry in entries.iterdir() if entry.is_dir())
#for entry in entries:
#    print(entry.name)


#import os
#
#basepath = '/.'
#
#print('LISTANDO TODOS OS ARQUIVOS E DIRETORIOS')
#with os.scandir(basepath) as entries:
#    for entry in entries:
#        print(entry.name)
#        
#print('\nLISTANDO APENAS ARQUIVOS')
#with os.scandir(basepath) as entries:
#    for entry in entries:
#        if entry.is_file():
#            print(entry.name)
#            
## Obter informação dos objetos .stat()
#with os.scandir(basepath) as entries:
#    for entry in entries:
#        info = entry.stat()
#        print(entry.name, info.st_mtime)



#from pathlib import Path
#
#current_dir = Path('/.')
#
#for path in current_dir.iterdir():
#    info = path.stat()
#    print(path.name, info.st_mtime)


#import os
#import fnmatch
#
#for file_name in os.listdir('./'):
#    if fnmatch.fnmatch(file_name,'*.txt'):
#        print(file_name)




import glob
import os

print(os.listdir())
print('\n\n')
print(glob.glob('*.py'))
