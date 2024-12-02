import os
import sys


file = open('output.txt')
info=[]
for words in file:
    if words.strip():
        info.append(words.strip())
appleart=('''
                   'c.
                 ,xNMM.          --------------------------------
               .OMMMMo           OS:{0}
               OMMM0,            Architecture:{1}
     .;loddo:' loolloddol;.      Processor:{2}
   cKMMMMMMMMMMNWMMMMMMMMMM0:    Cores:{3}
 .KMMMMMMMMMMMMMMMMMMMMMMMWd.    Vcores:{4}
 XMMMMMMMMMMMMMMMMMMMMMMMX.      Memory:{6} / {5}
;MMMMMMMMMMMMMMMMMMMMMMMM:       --------------------------------
:MMMMMMMMMMMMMMMMMMMMMMMM:       
.MMMMMMMMMMMMMMMMMMMMMMMMX.      
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.    
 .XMMMMMMMMMMMMMMMMMMMMMMMMMMk   
  .XMMMMMMMMMMMMMMMMMMMMMMMMK.   
    kMMMMMMMMMMMMMMMMMMMMMMd     
     ;KMMMMMMMWXXWMMMMMMMk.      
       .cooc,.    .,coo:. 
''').format(*info)
print(appleart)
