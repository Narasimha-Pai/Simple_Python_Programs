nterm = int(input("Enter the number of terms needed: "))
if nterm <= 0:
    nterm = int(input("Enter the positive number of terms needed: "))
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(2, nterm):
    fibo = n1 + n2
    n1 = n2
    n2 = fibo
    print(fibo)