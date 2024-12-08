import socket

HOST = '127.0.0.1'
PORT = 50007

filename = 'task3.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(filename.encode())

    with open(filename, 'rb') as f:
        while chunk := f.read(1024):
            s.sendall(chunk)

    print(f"File {filename} is sent to server.")
