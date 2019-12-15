import socket
import threading
import time

from Controller import Controller
from Repository import Repository

def every_10_seg(numbers_list):
    while run_server:
        time.sleep(10)
        print(numbers_list)

global run_server
run_server = True
hostname = socket.gethostname()
port = 4000
BUFFER_SIZE = 20
global repository
repository = Repository()
controller = Controller(hostname, port, BUFFER_SIZE, repository, run_server)
print_thread = threading.Thread(target=every_10_seg, args=(repository.numbers_list, ),  daemon=True)
print_thread.start()
controller.listen_to_requests()
