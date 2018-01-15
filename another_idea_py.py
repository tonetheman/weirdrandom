

import threading

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
        import threading

        s = threading.Semaphore()
        COUNT = 1000
        def t1():
            for i in range(COUNT):
                s.acquire()            
                self.mix(1)
                s.release()
        def t2():
            for i in range(COUNT):
                s.acquire()
                self.mix(2)
                s.release()
        def t3():
            for i in range(COUNT):
                s.acquire()
                self.mix(3)
                s.release()
            
        thread1 = threading.Thread(target=t1)
        thread2 = threading.Thread(target=t2)
        thread3 = threading.Thread(target=t3)
        thread1.start()
        thread2.start()
        thread3.start()
        thread1.join()
        thread2.join()
        thread3.join()

        print("done got this in r",self.r)


g = Gen()
g.gen()
