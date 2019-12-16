import socket
import threading

from Service import Service

class Controller(object):
    def __init__(self, host, port, buffer_size, repository, run_server):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.run_server = run_server
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.repository = repository
        self.service = Service(self.buffer_size, self.server_socket, self.run_server)

    def listen_to_requests(self):
        while True:
            try:
                client_socket, client_ip = self.server_socket.accept()
                new_thread = threading.Thread(target=self.service.listen_to_client, args=(client_socket, self.repository, ), daemon=True)
                new_thread.start()
                if not self.run_server:
                    break
            except ConnectionAbortedError as ex:
                print('A connection establish request was performed on a closed socket')
