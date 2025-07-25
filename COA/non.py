from nbitadd import *
from logic import *
def nonRestoringDivision(dividend, divisor, n):
    A = "0" * n
    Q = dividend.zfill(n)
    M = divisor.zfill(n)
    neg_M = twosCompliment(M, n)
    adder = NBitAdder(n)

    for _ in range(n):
        # Left shift [A | Q]
        combined = A + Q
        shifted = customLeftShift(combined, 2 * n)
        A = shifted[:n]
        Q = shifted[n:]

        # Conditional operation
        if A[0] == '0':  # A was positive , subtract M
            A, _ = adder.add(A, neg_M)
        else:           # A was negative ,add M
            A, _ = adder.add(A, M)

        # Set Q₀ based on new A
        if A[0] == '0':
            Q = Q[:-1] + '1'
        else:
            Q = Q[:-1] + '0'

    # Final correction if A < 0
    if A[0] == '1':
        A, _ = adder.add(A, M)

    quotient = Q
    remainder = A
    return quotient, remainder

if __name__ == "__main__":
    dividend = "00001111"
    divisor = "00000111"
    print(nonRestoringDivision(dividend,divisor,8))