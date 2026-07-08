"""n=int(input("enter the array size: "))
arr=list(map(int,input().split()))
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print(largest)"""

n=int(input("enter the array size: "))
arr=list(map(int,input().split()))
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        secondlargest=largest
        largest=arr[i]
print(secondlargest)

