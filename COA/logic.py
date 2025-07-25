
def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def XOR(a, b):
    return a ^ b

def NOT(a):
    return 1 - a

def twosCompliment(s, n):
    oneFound = False
    s = list(s.zfill(n))  # Ensure s is exactly n bits
    for i in range(n-1, -1, -1):
        if not oneFound:
            if s[i] == '1':
                oneFound = True
        else:
            if s[i] == '1':
                s[i] = '0'
            else:
                s[i] = '1'
    return ''.join(s)

def rightShiftSimple(s, n):
    s = s.zfill(n)
    return s[0] + s[:-1]

def customLeftShift(s, n):
    s = s.zfill(n)
    shifted = s[1:]  # Remove first bit (shifting left)
    return shifted + s[-1]  # Append original last bit

