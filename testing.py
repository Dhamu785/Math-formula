import PyDMath
a = input()
try:
    b = a.split(',')
    print(b)
except:
    print('123')
print(PyDMath.lcm(b))