
n=int(input("enter the array size: "))
arr=list(map(int,input().split()))
count=0
for i in range (len(arr)):
    for j in range (i+1,len(arr)):
         count+=1
print(count)
        

n=int(input("enter the array size: "))
arr=list(map(int,input().split()))
for i in range (len(arr)):
    for j in range (i+1,len(arr)):
        print(arr[i],arr[j])


n=int(input("enter the array size: "))
arr=list(map(int,input().split()))
k=int(input("enter a number: "))
for i in range (len(arr)):
    for j in range (i+1,len(arr)):
        sum=arr[i]+arr[j]
        if sum==k:
            print(arr[i],arr[j])
    

    
n=int(input("enter the array size: "))
arr=list(map(int,input().split()))
maximum=arr[0]+arr[1]
for i in range (len(arr)):
    for j in range (i+1,len(arr)):
        
        if (arr[i]+arr[j]>maximum):
             maximum=arr[i]+arr[j]
print(maximum)     


