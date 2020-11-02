import time

a = "x" *8

def stars(x):

    b = " " * x
    print(b+a)

def space(n):

    while n <= 8:

        n = n + 1
        stars(n)
        time.sleep(0.1)

def space1(m):

    while m != 0:

        m = m - 1
        stars(m)
        time.sleep(0.1)

while True:
    space(0)
    space1(8)
