n=int(input("enter a number: "))
reverse=0
dup=n
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if reverse==dup:
    print(True)
else:
    print(False)
