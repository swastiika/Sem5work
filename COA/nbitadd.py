from logic import *

class FullAdder:
    def compute_sum(self, a, b, carry_in):
        return XOR(XOR(a, b), carry_in)

    def compute_carry(self, a, b, carry_in):
        return OR(OR(AND(a, b), AND(b, carry_in)), AND(a, carry_in))
    

# class NBitAdder:
#     def __init__(self,n):
#         self.n = n
#         self.adder = FullAdder()
#     def add(self, bin1, bin2):
#         bin1 = bin1.zfill(self.n)[::-1]
#         bin2 = bin2.zfill(self.n)[::-1]
#         carry = 0
#         result = ""
#         for i in range(self.n):
#             a = int(bin1[i])
#             b = int(bin2[i])
#             s = self.adder.compute_sum(a,b,carry)
#             carry = self.adder.compute_carry(a,b,carry)
#             result += str(s)
#         return result,carry

class NBitAdder:
    def __init__(self, n):
        self.n = n
        self.adder = FullAdder()

    def add(self, bin1, bin2):
      
        bin1 = bin1.zfill(self.n)[::-1]
        bin2 = bin2.zfill(self.n)[::-1]

        carry = 0
        result = ""

        for i in range(self.n):
            a = int(bin1[i])
            b = int(bin2[i])
            s = self.adder.compute_sum(a, b, carry)
            carry = self.adder.compute_carry(a, b, carry)
            result = str(s) + result

        return result, str(carry)

# if __name__ == "__main__":
#     n = 8
#     adder = NBitAdder(n)

#     bin1 = "00001111"
#     bin2 = "00001111"

#     result, carry_out = adder.add(bin1, bin2)
#     print(f"Sum: {result}, Carry Out: {carry_out}")

if __name__ == "__main__":
    n = 8
    adder = NBitAdder(n)
    bin1 = "1111101"
    bin2 = "1111111"
    print(bin1.zfill(8)[::-1])
    # print(adder.add(bin1,bin2))
