def main(x):
    A = (int(x) & 0b00000000000000000000000001111111) << 25
    B = ((int(x) >> 7) & 0b00000000000001111111111111) 
    C = ((int(x) >> 20)) << 13
    return A | B | C
print(hex(main(0x7e758766)))
