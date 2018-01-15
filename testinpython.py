
class Gen:
    def __init__(self,seed=0):
        self.r = seed # start with a seed if passed
    def rand(self,v):
        mx = int(self.r>>31) & int(0xa8888eef)
        self.r = int(int(self.r<<1) ^ mx)
        return self.r
    def mix(self,v):
        self.r = (int(self.r<<5)+int(self.r)) + int(v)
    def gen(self):
        import socket
        import struct
        def server_target():
            SERVER_HOST =""
            SERVER_PORT = 16777
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((SERVER_HOST,SERVER_PORT))
            server.listen(2)
            for i in range(100):
                conn,addr = server.accept()
                data=conn.recv(1)
                print("got",data)
                # this completely obvious CRAP code
                # is for python 3
                data = struct.unpack("B",data)[0]
                self.mix(data)
                conn.close()
        import threading
        t =threading.Thread(target=server_target)
        t.start()
        def client_target(id):
            print("starting target with id",id)
            H = "localhost"
            P = 16777
            # s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # s.connect()
            # s.close()
            for i in range(50):
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((H,P))
                # changed this python3
                s.send(struct.pack("B",id))
                s.close()
        t1 = threading.Thread(target=client_target,args=(1,))
        t2 = threading.Thread(target=client_target,args=(2,))
        t1.start()
        t2.start()        

        t1.join()
        t2.join()
        print("done got this in r",self.r)

g = Gen()
g.gen()
