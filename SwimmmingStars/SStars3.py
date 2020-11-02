import time


STARS_NUM = 50
a = "x" * STARS_NUM

def stars(x):

    b = " " * x
    print(b+a)

def space(j):

    if j >= 0:
        n = 1
    else:
        n = STARS_NUM - 1

    while n <= STARS_NUM and n >= 0:
        stars(n)
        n += j
        time.sleep(0.1)

while True:
    space(1)
    space(-1)
