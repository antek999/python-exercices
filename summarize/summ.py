x = int(input("enter a number:"))


sumx = sum(int(digit) for digit in str(x))


print("sum of all digits in {} is {}".format(x,sumx))
