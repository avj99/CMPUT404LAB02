import socket

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):

    with conn:
        print(f"Connected by: {addr}")

        while True:

            data = conn.recv(BYTES_TO_READ)
            if not data:
                print("hi")
                break
            print(data)
            conn.sendall(data)

def start_server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #re-use socket address and 1 means true 

        s.listen()

        conn, addr = s.accept()
        handle_connection(conn, addr)

# Start multithreaded echo server
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))

        '''
        setsockopt(level, option, value)
        https://manpages.debian.org/bullseye/manpages-dev/setsockopt.2.en.html
        '''
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2) # Allow backlog of up to 2 connections
        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

start_server()
#start_threaded_server()
start_server()