import socket

HOST = ''
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:

        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            filename = conn.recv(1024).decode()
            print(f"Receiving file: {filename}")

            with open(filename, 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print(f"File {filename} is received and saved.")
