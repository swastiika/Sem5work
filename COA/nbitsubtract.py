from logic import *
from nbitadd import NBitAdder
from scomp import Twoscomp
class FullSubtractor:
    def compute_difference(self, a, b, borrow_in):
        return XOR(XOR(a, b), borrow_in)

    def compute_borrow(self, a, b, borrow_in):
    
        part1 = AND(NOT(a), b)
        part2 = AND(OR(NOT(a), b), borrow_in)
        return OR(part1, part2)

class NBitSubtractor:
    def __init__(self, n):
        self.n = n
        self.subtractor = FullSubtractor()

    def subtract(self, bin1, bin2):

        bin1 = bin1.zfill(self.n)[::-1]
        bin2 = bin2.zfill(self.n)[::-1]

        borrow = 0
        result = ""

        for i in range(self.n):
            a = int(bin1[i])
            b = int(bin2[i])
            diff = self.subtractor.compute_difference(a, b, borrow)
            borrow = self.subtractor.compute_borrow(a, b, borrow)
            result = str(diff) + result

        return result, borrow
if __name__ == "__main__":
    n = 8
    subtractor = NBitSubtractor(n)

    bin1 = "0000"
    bin2 = "1111"

    result, borrow_out = subtractor.subtract(bin1, bin2)
    print(f"Difference: {result}, Borrow Out: {borrow_out}")
# class nBitsubtract:
#     @staticmethod
#     def subtract(bin1, bin2, n):
#         bin1 = bin1.zfill(n)
#         bin2 = bin2.zfill(n)

#         bin2_complement = Twoscomp.twoscomplement(bin2)
#         add = NBitAdder(n)
#         diff, carry = add.add(bin1, bin2_complement)

#         # Only keep n bits
#         diff = diff[-n:]

#         return diff, carry


# # Test code
# if __name__ == "__main__":
#     n = 8
#     bin1 = "0000"
#     bin2 = "1111"
#     print(nBitsubtract.subtract(bin1, bin2, n))
