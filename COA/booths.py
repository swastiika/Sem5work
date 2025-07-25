from logic import *
from nbitadd import *

def nbitMul(multiplicand, multiplier, n):
    adder = NBitAdder(n)
    twos = twosCompliment(multiplicand, n)
    Q = '0'
    multiplicand = multiplicand.zfill(n)
    multiplier = multiplier.zfill(n)
    accumulator = '0' * n + multiplier  # Fixed: use '0' * n instead of ''.zfill(n)
    
    for i in range(n):
        if Q == '0' and accumulator[-1] == '1':
            partial_sum, _ = adder.add(accumulator[:n], twos)
            accumulator = partial_sum + accumulator[n:]  # Fixed: use accumulator[n:] and update accumulator
        elif Q == '1' and accumulator[-1] == '0':
            partial_sum, _ = adder.add(accumulator[:n], multiplicand)  # Fixed: add accumulator[:n], not multiplicand,n
            accumulator = partial_sum + accumulator[n:]  # Fixed: use accumulator[n:] and update accumulator
        
        Q = accumulator[-1]  # Fixed: update Q before shifting
        accumulator = rightShiftSimple(accumulator, 2*n)
        
    return accumulator

if __name__=="__main__":
    print(nbitMul("101","011",4))
    