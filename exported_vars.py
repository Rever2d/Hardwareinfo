import os
import sys
import subprocess
hardwareinfo =('''\033[33m
 _    _               _                        
| |  | |             | |                       
| |__| | __ _ _ __ __| |_      ____ _ _ __ ___ 
|  __  |/ _` | '__/ _` \ \ /\ / / _` | '__/ _ \\
| |  | | (_| | | | (_| |\ V  V / (_| | | |  __/
|_|  |_|\__,_|_|  \__,_| \_/\_/ \__,_|_|  \___|                                               
 _        __      
(_)      / _|     
 _ _ __ | |_ ___  
| | '_ \|  _/ _ \ 
| | | | | || (_) |
|_|_| |_|_| \___/ 
                                               
\033[0m''')
              
print(hardwareinfo)

try:
    result = subprocess.run(
        ['ansible-playbook', 'playbook.yml'],
        capture_output=True,  
        text=True,            
        check=True            
    )
except subprocess.CalledProcessError as e:
    print(f"Error running playbook: {e}")
    print(f"Standard Error: {e.stderr}")

file = open('output.txt')
info=[]
for words in file:
    if words.strip():
        info.append(words.strip())

if info[0] =='MacOSX':
    appleart = ('''
\033[34m                   'c.
                 ,xNMM.          \033[33m--------------------------------\033[34m
               .OMMMMo           \033[33mOS: \033[0m{0}\033[34m
               OMMM0,            \033[33mArchitecture: \033[0m{1}\033[34m
     .;loddo:' loolloddol;.      \033[33mProcessor: \033[0m{2}\033[34m
   cKMMMMMMMMMMNWMMMMMMMMMM0:    \033[33mCores: \033[0m{3}\033[34m
 .KMMMMMMMMMMMMMMMMMMMMMMMWd.    \033[33mVcores: \033[0m{4}\033[34m
 XMMMMMMMMMMMMMMMMMMMMMMMX.      \033[33mMemory: \033[0m{6} / {5}\033[34m
;MMMMMMMMMMMMMMMMMMMMMMMM:       \033[33mUptime: \033[0m{7}\033[34m
:MMMMMMMMMMMMMMMMMMMMMMMM:       \033[33m-------------------------------\033[34m
.MMMMMMMMMMMMMMMMMMMMMMMMX.      
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.    
 .XMMMMMMMMMMMMMMMMMMMMMMMMMMk   
  .XMMMMMMMMMMMMMMMMMMMMMMMMK.   
    kMMMMMMMMMMMMMMMMMMMMMMd     
     ;KMMMMMMMWXXWMMMMMMMk.      
       .cooc,.    .,coo:. \033[0m
''').format(*info)
    print(appleart)
if info[0] == 'Linux':
    # maybe not linux will need to test
    linuxart = (r'''
         _nnnn_
        dGGGGMMb            -------------------------------- 
       @p~qp~~qMb           OS: {0}
       M|@||@) M|           Architecture: {1}
       @,----.JM|           Processor: {2}
      JS^\__/  qKL          Cores: {3}
     dZP        qKRb        Vcores: {4}
    dZP          qKKb       Memory: {6} / {5}
   fZP            SMMb      Uptime: {7}
   HZM            MMMM      --------------------------------
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' hjm
                ''').format(*info)
    print(linuxart)
