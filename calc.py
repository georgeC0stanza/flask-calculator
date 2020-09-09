import binaryAdder
import DefineConstants

ADDER = binaryAdder.BinaryAdder()

def addBytes(byteA, ByteB):
    ADDER.load(byteA, ByteB)
    ADDER.add()
    return ADDER.total
        
def negateByte(byte):
    byte = [not i for i in byte]
    return byte

def numberToByte(number):
    isNeg = False

    if int(number) < 0:
        number = -number
        isNeg = True

    byte = [int(x) for x in bin(number)[2:]]

    while len(byte) < DefineConstants.BYTESIZE:
        byte.insert(0, False)

    if isNeg:
        byte = addBytes(negateByte(byte), DefineConstants.BYTEONE)

    return byte

def ByteToNumber(binaryNumber):
    #TODO
    return binaryNumber

def addition(A, B):
    binaryA = numberToByte(A)
    binaryB = numberToByte(B)

    binaryTotal = addBytes(binaryA, binaryB)
    baseTenTotal = ByteToNumber(binaryTotal)
    return (baseTenTotal, binaryTotal)