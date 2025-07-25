
# booths algorthm for multiplication
from logic import *
from nbitadd import *

def boothsMul(multiplicand, multiplier, n):
    adder = NBitAdder(n)
    M = multiplicand.zfill(n)
    negM = twosCompliment(M, n)
    A = '0' * n
    Q = multiplier.zfill(n)
    Q_1 = '0'
    
    for _ in range(n):
        # Check Q0 and Q-1 bits
        if Q[-1] == '1' and Q_1 == '0':
            A, _ = adder.add(A, negM)  
        elif Q[-1] == '0' and Q_1 == '1':
            A, _ = adder.add(A, M)   
        combined = A + Q + Q_1
        
        sign_bit = A[0]
        shifted = sign_bit + combined[:-1]  
  
        A = shifted[:n]
        Q = shifted[n:n*2]
        Q_1 = shifted[-1]
    
    return A + Q 

if __name__=="__main__":
   
    multiplicand = '0010' 
    multiplier = '0010'   
    result = boothsMul(multiplicand, multiplier, 4)
    print("Product: ", result)
  
