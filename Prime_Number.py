flag = False
n = int(input("Enter the input: "))
for i in range(2,n):
    if (n % i == 0):
        flag = True
        break
if flag:                                     #if flag == True
    print(n, "is not a Prime Number")
else:
    print(n, "is a Prime Number")