def NOT(a):
    if a == 0:
        print(bool(1))
    elif a == 1:
        print(bool(0))
    else:
        print("This type is not in the database")


def AND(a, b):
    if a == 1 and b == 1:
        print(bool(1))
    else:
        print(bool(0))


def OR(a, b):
    if a == 0 and b == 0:
        print(bool(0))
    else:
        print(bool(1))


# Nor gate is when we first use an or gate then use that output for a NOT gate
def NOR(a, b):
    if a == 0 and b == 0:

        print(bool(1))
    else:
        print(bool(0))


def NAND(a, b):
    if a == 1 and b == 1:
        print(bool(0))
    else:
        print(bool(1))


# AND   |   OR   |   NOT  |   NOR

# To convert bin to int
def bint(n):
    print(int(n))


#  To convert int to bin

def dbin(n):
    print(bin(n))

def XNOR(a, b):
    if a == 0 and b == 0 or a == 1 and b == 1:
        print(bool(1))
    else:
        print(bool(0))

def XOR(a, b):
    if a == 1 and b == 1:
        return bool(0)
    elif a == 0 and b == 0:
        print(bool(0))
    else:
        print(bool(1))


XOR(0, 0)