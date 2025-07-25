# ones complement of a binary is found out by flipping the bits 1 to  0 and 0 to 1
# twos complement is obtained by adding 1 to ones complement

# def ones_complement(s):
#     return ''.join('1' if bit == '0' else '0' for bit in s)


# def twos_complement(s):
#     ones = ones_complement(s)
#     result = list(ones)
#     carry = 1

#     for i in range(len(result) - 1, -1, -1):
#         if result[i] == '1' and carry == 1:
#             result[i] = '0'
#             carry = 1
#         elif result[i] == '0' and carry == 1:
#             result[i] = '1'
#             carry = 0
#         else:
#             break  

#     return ''.join(result)

# def find_complements(s):
#     ones = ones_complement(s)
#     twos = twos_complement(s)
#     return ones, twos


#shortcut way of finding the twos complement, copy the number as it is until you get the first 1 and then invert eveything after that
class Twoscomp:
        def twoscomplement(s):
            s = list(s)  # Convert string to list for mutability
            i = len(s) - 1
            onefound = False

            while i >= 0:
                if not onefound:
                    if s[i] == '1':
                        onefound = True
                    i -= 1
                else:
                    if s[i] == '1':
                        s[i] = '0'
                    else:
                        s[i] = '1'
                    i -= 1

            return ''.join(s)  # Convert list back to string


if __name__ == "__main__":
    s = "1001"
    print("Original:", s)
    twos = Twoscomp(s)
    print("2's Complement:", twos)
