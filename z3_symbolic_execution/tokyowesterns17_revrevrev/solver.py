from z3 import *

alt_flag = [42, 234, 194, 42, 98, 222, 142, 14, 94, 150, 206, 158, 34, 118, 70, 182, 70, 246, 94, 236, 108, 246, 230, 54, 30, 14, 94, 154, 38, 214, 190]

def solve(alt_flag):
    zolv = Solver()
    inp = []
    for i in range(0, len(alt_flag)):
        b = BitVec("%d" % i, 16)
        inp.append(b)
    for i in range(0, len(alt_flag)):
        x = (2 * (inp[i] & 0x55)) | ((inp[i] >> 1) & 0x55)
        y = (4 * (x & 0x33)) | ((x >> 2) & 0x33)
        z = (16 * y) | (y >> 4)
        z = z & 0xff
        zolv.add(z == alt_flag[i])
    if zolv.check() == sat:
        print("The condition is satisfied, would still recommend crying: " + str(zolv.check()))
        solution = zolv.model()
        flag = ""
        for i in range(0, len(alt_flag)):
            flag += chr(int(str(solution[inp[i]])))
        print(flag)
    if zolv.check() == unsat:
        print("The condition is not satisfied, would recommend crying: " + str(zolv.check()))

solve(alt_flag)
