# restoring division
from nbitadd import *
from logic import *
def restoringDivision(dividend, divisor, n):
    # Initial setup
    A = "0" * n
    Q = dividend.zfill(n)
    M = divisor.zfill(n)
    neg_M = twosCompliment(M, n)
    adder = NBitAdder(n)

    for _ in range(n):
        combined = A + Q
        shifted = customLeftShift(combined, 2 * n)
        A = shifted[:n]
        Q = shifted[n:]
        A_sub, _ = adder.add(A, neg_M)

        #  Check sign
        if A_sub[0] == '0':
            # If A >= 0, set Q₀ = 1 (last bit of Q)
            Q = Q[:-1] + '1'
            A = A_sub
        else:
            # If A < 0, restore A and set Q₀ = 0
            A, _ = adder.add(A_sub, M)
            Q = Q[:-1] + '0'

    # Final result
    quotient = Q
    remainder = A
    return quotient, remainder


if __name__ == "__main__":
    dividend = "00001111"
    divisor = "00000111"
    print(restoringDivision(dividend,divisor,8))