import random
N=random.randint(1,10)
arr=[random.randint(1,10) for i in range(N)]
print(arr)

for i in range(len(arr)//2):
    t=arr[i]
    arr[i]=arr[len(arr)//2+i]
    arr[len(arr)//2+i]=t
print(arr)
