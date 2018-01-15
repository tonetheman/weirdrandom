


def test1():
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

def shiftLeft5(a):
    tmp = a<<5
    print(hex(tmp))
    return tmp
def shiftRight31(a):
    return a>>31
def shiftRight31WithAnd(a):
    tmp = (a>>31) & 0xa8888eef
    print(hex(tmp))
    return tmp

i = int(600)
print(shiftLeft5(i))
print(shiftRight31(i))
print(shiftRight31WithAnd(i))