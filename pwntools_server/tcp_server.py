import socket
import subprocess
import threading

HOST = '127.0.0.1'
PORT = 65432
BINARY_PATH = '/home/kiki/git/nightmare_binexp_re/pwntools_server/beleaf'

def handle_client(conn, addr):
    print("Connected by", addr)
    try:
        process = subprocess.Popen(
            BINARY_PATH,
            stdin=conn,
            stdout=conn,
            stderr=subprocess.PIPE
        )
        process.wait()
        if process.return_code != 0:
            print(f"Binary exited with non-zero code: {process.return_code}")
            stderr_output = process.stderr.read().decode()
            print(f"Stderr output:\n{stderr_output}")
    except Exception as e:
        print(f"Error running binary: {e}")
    finally:
        conn.close()
        print('Connection closed')

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            # handle_connection(conn, addr)
            client_thread.start()

if __name__ == "__main__":
    start_server()
