


class Mixer:
    def __init__(self,seed=0):
        self.r = seed
    def mix(self,v):
        self.r = (self.r<<5) + self.r + int(v)
    def rand(self):
        mx = (int(r>>31))  & 0xa8888eef
        self.r = self.r<<1 ^ mx
        return self.r
m = Mixer()
m.mix(10)
print(m.r)