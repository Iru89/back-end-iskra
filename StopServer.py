class StopServer(Exception):
    def __init__(self,):
        self.message = '[*] Connection close and stop server'
        #print('[*] Connection close and stop server')
