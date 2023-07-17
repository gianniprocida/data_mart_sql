import socket

def check_connection(host,port):
    try:
        socket_obj = socket.create_connection((host,port),timeout=5)
        print(f"Connection to the {host} container was successfully established")
        return socket_obj
    except Exception as e:
        print(f"Connection failed: {e}")