import os
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
print(colored(name, "blue"))

# Encrypted extensions
encrypted_ext = ('') # enter extension(s) of encrypted file(s) in the bracket separate with ,

# Grab all files from the machine
file_paths = []

for root, dirs, files in os.walk('C:'):
    for file in files:
        if file.endswith(encrypted_ext):
            file_paths.append(os.path.join(root, file))
for f in file_paths:
    print(f)
print('successfully located all files')

key = input('Enter decryption key: ')




# encrypting files


def decrypt(key):
    while not q.empty():
        try:
            file_ = q.get()
            cipher = Fernet(key)
            with open(file_, 'rb') as original_file:
                original_data = original_file.read()

                decrypted_data = cipher.decrypt(original_data)

            with open(file_, "wb") as encrypted_file:
                encrypted_file.write(decrypted_data)
                print(f'{file_} decrypted successfully!')

        except:
            print(f'failed to decrypt {file_}')
            q.task_done()


q = Queue()
for file in file_paths:
    q.put(file)
for i in range(30):
    thread = Thread(target=decrypt, args=(key,), daemon=True)
    thread.start()

q.join()
