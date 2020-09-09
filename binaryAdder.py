import DefineConstants

class BinaryAdder:
    def __init__(self, inputOne = None, inputTwo = None):
        self.inputOne = inputOne
        self.inputTwo = inputTwo

    inputOne = DefineConstants.BYTE
    inputTwo = DefineConstants.BYTE
    total = DefineConstants.BYTE
    overFlowBit = False

    def load(self, inputOne, inputTwo):
        self.inputOne = inputOne
        self.inputTwo = inputTwo
        
    def add(self):
        for x in reversed(range(DefineConstants.BYTESIZE)):
            self.total[x] = self.fullAdder(self.inputOne[x], self.inputTwo[x], self.overFlowBit)

    def fullAdder(self, a, b, carry):
        AxB = a ^ b
        AnB = a & b
        ABC = AxB & carry
        self.overFlowBit = AnB | ABC
        return AxB ^ carry
