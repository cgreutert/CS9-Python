'''
H03
'''
def computePower(base, power):
    if power == 0:
        return 1
    else:
        return base * computePower(base, power-1)
assert computePower(3,0) == 1
assert computePower(3,3) == 27
assert computePower(-2,3) == -8
assert computePower(0,3) == 0
print("stfu u baddie")
