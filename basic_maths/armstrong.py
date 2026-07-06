n=int(input("enetr a number: "))
sum=0
original=n
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
if original==sum:
    print(True)
else:
    print(False)