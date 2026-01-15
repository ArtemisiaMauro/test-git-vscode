# Program to check if a number is prime or not
# To take input from the user
num = int(input("Entrez un nombre: "))
# define a flag variable
flag = False
if num == 1:
    print(num, "n'est pas un nombre premier")
elif num > 1:
# check for factors
    for i in range(2, num):
        if (num % i) == 0:
# if factor is found, set flag to True
            flag = True
# break out of loop
            break
# check if flag is True
if flag:
    print(num, "n'est pas un nombre premier")
else:
    print(num, "est un nombre premier")