#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

if __name__ == '__main__':
    # El client a de tenir les mateixes especificacions que el server
    host = socket.gethostname()
    port = 4000
    BUFFER_SIZE = 1024
    MESSAGE = input('Introdueix un numero de 9 xifres: ')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
        socket_tcp.connect((host, port))
        # Convertimos str a bytes
        socket_tcp.send(MESSAGE.encode('utf-8'))
        data = socket_tcp.recv(BUFFER_SIZE)