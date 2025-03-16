def sendAddition(x):
    return x & 0xffffffff
def sendAddition2(x):
    return (x & 0xffffffff00000000) >> 32

print(sendAddition(0x400488))
print(sendAddition2(0x400488))
print(hex(sendAddition(0x1111111100400488)))
print(hex(sendAddition2(0x1111111100400488)))
