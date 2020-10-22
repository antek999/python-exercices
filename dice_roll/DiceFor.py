import random

loopcount=6
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0

for x in range(loopcount):
    a=random.randint(1, 6)
    #    print(a)
    if a==1:
        x1 += 1
    if a==2:
        x2 += 1
    if a==3:
        x3 += 1
    if a==4:
        x4 += 1
    if a==5:
        x5 += 1
    if a==6:
        x6 += 1
print("1 got rolled {0}times".format(x1))
print("2 got rolled {0}times".format(x2))
print("3 got rolled {0}times".format(x3))
print("4 got rolled {0}times".format(x4))
print("5 got rolled {0}times".format(x5))
print("6 got rolled {0}times".format(x6))
