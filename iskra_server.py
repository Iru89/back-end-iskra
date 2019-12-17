#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import time

from Controller import Controller
from Repository import Repository

def every_10_seg(repository):
    signal_total = 0

    while run_server:
        last_duplicate_count = repository.duplicated_numbers
        time.sleep(10)

        unique_numbers = len(repository.numbers_list) - signal_total
        count_new_duplicates = repository.duplicated_numbers - last_duplicate_count
        signal_total = len(repository.numbers_list)

        #print(repository.numbers_list)
        print(str(unique_numbers) + ' unique numbers, ' + str(count_new_duplicates) + ' duplicated received. Signal total: ' + str(signal_total))



global run_server
run_server = True
hostname = socket.gethostname()
port = 4000
BUFFER_SIZE = 20
global repository
repository = Repository()
controller = Controller(hostname, port, BUFFER_SIZE, repository, run_server)
try:
    print_thread = threading.Thread(target=every_10_seg, args=(repository, ),  daemon=True)
    print_thread.start()
    controller.listen_to_requests()
except KeyboardInterrupt:
    controller.server_socket.close()
