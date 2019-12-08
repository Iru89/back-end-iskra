#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import re
import LogFile
import time
import threading

hostname = socket.gethostname() #Aquesta funcio ens retornara el nom de la maquina
ipHost = socket.gethostbyname(hostname) #Aquesta funcio ens retorna la ip de la nostra maquina
port = 4000
BUFFER_SIZE = 1024 #Utilitzem un numero petit per tenir una resposta rapida, 9 digits en pythons es un int = 32bits
server_on = True  # type: bool

lock = threading.Lock()
list_numbers = []

''''Los objetos socket soportan el context manager type
así que podemos usarlo con una sentencia with, no hay necesidad
de llamar a socket_close()
'''

def check_9_digits(num):
    patron = re.compile('[0-9]{1,9}$')
    check = patron.match(num)
    if check:
        return True
    else:
        return False

def save_number(number):
    if number in list_numbers:
        print('[*] Repeated number: %s' % number)
    else:
        list_numbers.append(number)
        print('[*] New number: %s' % number)
        LogFile.writeNewNumber(number)


def every_10_seg(server_on):
    while server_on:
        #print(list_numbers)
        time.sleep(10)


def add_0(data_str):
    longitud = len(data_str)
    num_of_0 = 9 -longitud
    str_result = ''
    for i in range(num_of_0):
        str_result = str_result.__add__('0')
    return str_result.__add__(data_str)

def listen_to_clinet(conn, addr):

    #print('[*] Conexión establerta')
    data_bytes = conn.recv(BUFFER_SIZE)
    data_str = add_0(data_bytes.decode('utf-8'))

    if data_str == 'terminate':
        print('[*] Close connection')
    elif check_9_digits(data_str):
        save_number(data_str)
    else:
        print('[*] Not a valid number: %s' % data_str)
    conn.close()



#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp: # Creamos un objeto socket tipo TCP
#def Main():
print_thread = threading.Thread(target=every_10_seg, args=(server_on,))
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.bind((hostname, port))
socket_tcp.listen(5) #Esperem la conexión del client, el 5 representa les conexions en espera abans de refusar una connexio de un client.

while True:

    conn, addr = socket_tcp.accept()
    print(list_numbers)
    client_thread_1 = threading.Thread(target=listen_to_clinet, args=(conn, addr,)).start()


    # client_thread_2 = threading.Thread(target=listen_to_clinet, args=(conn, addr,)).start()
    # client_thread_3 = threading.Thread(target=listen_to_clinet, args=(conn, addr,)).start()
    # client_thread_4 = threading.Thread(target=listen_to_clinet, args=(conn, addr,)).start()
    # client_thread_5 = threading.Thread(target=listen_to_clinet, args=(conn, addr,)).start()

socket_tcp.close()
