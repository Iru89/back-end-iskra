#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import re
import LogFile
import time
import threading

def check_9_digits(num):
    patron = re.compile('[0-9]{1,9}$')
    check = patron.match(num)
    if check:
        return True
    else:
        return False


def save_number(number):
    lock.acquire()
    if number not in list_numbers:
        list_numbers.append(number)
        LogFile.writeNewNumber(number)
    lock.release()


def every_10_seg():
    while server_on:
        time.sleep(10)
        print(list_numbers)


def nine_digits_format(data_str):
    longitud = len(data_str)
    num_of_0 = 9 - longitud
    str_result = ''
    for i in range(num_of_0):
        str_result = str_result.__add__('0')
    return str_result.__add__(data_str)



def listen_to_clinet(conn, ):
    conn.set
    data_bytes = conn.recv(BUFFER_SIZE)
    conn.close()
    data_str = nine_digits_format(data_bytes.decode('utf-8'))

    if not data_str:
        data_str = 'not data'

    if data_str == 'terminate':
        lock.acquire()
        global server_on
        server_on = False
        print('[*] Connection close')
        lock.release()
    elif check_9_digits(data_str):
        save_number(data_str)


hostname = socket.gethostname()  # Aquesta funcio ens retornara el nom de la maquina
ipHost = socket.gethostbyname(hostname)  # Aquesta funcio ens retorna la ip de la nostra maquina
port = 4000
BUFFER_SIZE = 20  # Utilitzem un numero petit per tenir una resposta rapida, 9 digits en pythons es un int = 32bits

server_on = True
lock = threading.Lock()
list_numbers = []
threads = []

print_thread = threading.Thread(target=every_10_seg, daemon=True)
print_thread.start()
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.bind((hostname, port))

while True:
    socket_tcp.listen(5)
    conn, addr = socket_tcp.accept()

    new_thread = threading.Thread(target=listen_to_clinet, args=(conn,), daemon=True)
    new_thread.start()
    threads.append(new_thread)

    if not server_on:
        socket_tcp.close()
        break
