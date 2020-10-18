
import random


a=random.randint(1, 50)

while True:
    b=random.randint(1, 50)
    if b!=a:
        break

while True:
    c=random.randint(1, 50)
    if c!=a and c!=b:
        break

while True:
    d=random.randint(1, 50)
    if d!=a and d!=b and d!=c:
        break

while True:
    e=random.randint(1, 50)
    if e!=a and e!=b and e!=c and e!=d:
        break

while True:
    f=random.randint(1, 50)
    if f!=a and f!=b and f!=c and f!=d and f!=e:
        break
 
print(a, b ,c ,d ,e ,f)

while True:
    print('PODAJ PIERWSZA LiCZBE 1-50')
    x1=int(input())
    print('PODAJ DRUGA LiCZBE 1-50')
    x2=int(input()) 
    print('PODAJ TRZECIA LiCZBE 1-50')
    x3=int(input()) 
    print('PODAJ CZWARTA LiCZBE 1-50')
    x4=int(input()) 
    print('PODAJ PIATA LiCZBE 1-50')
    x5=int(input()) 
    print('PODAJ SZOSTA LiCZBE 1-50')
    x6=int(input()) 
    if x1==a and x2==b and x3==c and x4==d and x5==e and x6==f:
         print('super!!!!')
         break
    else:
         print('slabo....')

