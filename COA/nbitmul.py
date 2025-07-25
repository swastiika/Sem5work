# this is a program to multiply the two numbers in binary format , where we will be using the basic algorithm, 
# if multiplier is 0 then we only do the right shift 
# if multiplier bit is 1 then we add the numbers to the left part and do the shifting

from nbitadd import *


def nBitMultiply(multiplicand, multiplier, n):
    multiplicand = multiplicand.zfill(n)
    multiplier = multiplier.zfill(n)
    accumulator = list("0" * (2 * n))
    adder = NBitAdder(n)  
    for i in range(n):
        if multiplier[n-1-i] == '1':
            left_sum, carry = adder.add(''.join(accumulator[:n]), multiplicand)
            accumulator[:n] = list(left_sum)
        if i < n:
            accumulator = ['0'] + accumulator[:-1]
    
    return ''.join(accumulator)

if __name__ == "__main__":
    multiplicand = "000010"
    multiplier = "00000011"
    print(nBitMultiply(multiplicand, multiplier, 8))
