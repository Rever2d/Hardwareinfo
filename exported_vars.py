import os
import sys
import subprocess

import subprocess

# Path to your Ansible playbook
playbook_path = "playbook.yml"

# Run the playbook using subprocess
try:
    result = subprocess.run(
        ['ansible-playbook', playbook_path],
        capture_output=True,  
        text=True,            
        check=True            
    )
    print("Playbook Output:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error running playbook: {e}")
    print(f"Standard Error: {e.stderr}")

file = open('output.txt')
info=[]
for words in file:
    if words.strip():
        info.append(words.strip())
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