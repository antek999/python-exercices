
import random

verbose=True
maxx=10



a=random.randint(1, maxx)

while True:
    b=random.randint(1, maxx)
    if b!=a:
        break

while True:
    c=random.randint(1, maxx)
    if c!=a and c!=b:
        break

while True:
    d=random.randint(1, maxx)
    if d!=a and d!=b and d!=c:
        break

while True:
    e=random.randint(1, maxx)
    if e!=a and e!=b and e!=c and e!=d:
        break

while True:
    f=random.randint(1, maxx)
    if f!=a and f!=b and f!=c and f!=d and f!=e:
        break

proba_nr=0

while True:

    proba_nr=proba_nr + 1

    if verbose==True and proba_nr%100==0:
        print(proba_nr)

    x1=random.randint(1, maxx)
    x2=random.randint(1, maxx)
    x3=random.randint(1, maxx)
    x4=random.randint(1, maxx)
    x5=random.randint(1, maxx)
    x6=random.randint(1, maxx)
    if x1==a and x2==b and x3==c and x4==d and x5==e and x6==f:
         print('super!!!!')
         break

print(a, b ,c ,d ,e ,f)
print('udalo sie za {0} razem'.format(proba_nr))
