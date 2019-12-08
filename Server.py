import socket
import re
import LogFile
import time
import threading
from _thread import *

hostname = socket.gethostname() #Aquesta funcio ens retornara el nom de la maquina
ipHost = socket.gethostbyname(hostname) #Aquesta funcio ens retorna la ip de la nostra maquina
port = 4000
BUFFER_SIZE = 1024 #Utilitzem un numero petit per tenir una resposta rapida, 9 digits en pythons es un int = 32bits

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


def every_10_seg():
    print(list_numbers)
    time.sleep(10)


#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp: # Creamos un objeto socket tipo TCP
#def Main():
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.bind((hostname, port))
socket_tcp.listen(5) #Esperem la conexión del client, el 5 representa les conexions en espera abans de refusar una connexio de un client.
# start_new_thread(every_10_seg)
while True:
    conn, addr = socket_tcp.accept()

    print('[*] Conexión establerta')
    data_bytes = conn.recv(BUFFER_SIZE)
    data_str = data_bytes.decode('utf-8')

    if data_str == 'terminate':
        print('[*] Close connection')
        break
    elif check_9_digits(data_str):
        save_number(data_str)
        conn.close()
    else:
        print('[*] Not a valid number: %s' % data_str)
        conn.close()

socket_tcp.close()
