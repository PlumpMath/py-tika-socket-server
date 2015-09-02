#!/usr/bin/env python
import sys
import socket

class TikaClient(object):

    def __init__(self, host='localhost', port=9999):
        self.host=host
        self.port=port
        self.sock=None

    def extract_text(self, fp):
        try:
            return self.send("\x04{}\n".format(fp))
        except socket.error as e:
            return (False, str(e))

    def server_shutdown(self):
        try:
            return self.send("\x03\n")
        except socket.error as e:
            return (False, str(e))            

    def server_check(self):
        try:
            return self.send("\x02\n")        
        except socket.error as e:
            return (False, str(e))            

    # input fully qualified local file path
    # returns (successful?:Boolean, data:String)
    def send(self, msg):
        try:
            self.sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            self.sock.sendall(msg)
            data = []
            rtn = self.sock.recv(1)
            if ord(rtn) == 0:
                #something went wrong
                print "Failed {}".format(msg)
                return (False, "")
            while 1:
                rcv = self.sock.recv(8192)
                #received end of stream byte \x00
                if rcv.endswith("\x00"):
                    data.append(rcv[:-1])
                    break
                data.append(rcv)
            return (ord(rtn) == 1, "".join(data))
        finally:
            self.sock.close()
