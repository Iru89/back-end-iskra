from StopServer import StopServer
import socket
import threading
import re

class Service(object):
    def __init__(self, buffer_size, server_socket, run_server):
        self.buffer_size = buffer_size
        self.server_socket = server_socket
        self.run_server = run_server
        self.lock = threading.Lock()

    def nine_digits_format(self, data_str):
        length = len(data_str)
        num_of_0 = 9 - length
        str_result = ''
        for i in range(num_of_0):
            str_result = str_result.__add__('0')    #afegim els 0 que falten
        return str_result.__add__(data_str)         #afegim el numero rebut

    @staticmethod
    def check_9_digits(num):
        patron = re.compile('[0-9]{1,9}$')
        check = patron.match(num)
        if check:
            return True
        else:
            return False

    def listen_to_client(self, client_socket, repository):
        data_bytes = client_socket.recv(self.buffer_size)
        client_socket.close()
        data_str = self.nine_digits_format(data_bytes.decode('utf-8'))

        if not data_str:
            data_str = 'not data'   #per evitar transformar en tot 0s

        if data_str == 'terminate':
            # self.server_socket.shutdown(socket.SHUT_RDWR)
            self.run_server = False
            self.server_socket.close()
            # raise KeyboardInterrupt
            # print('raise StopServer')
        elif self.check_9_digits(data_str):
            self.lock.acquire()
            repository.save_number(data_str)
            self.lock.release()
