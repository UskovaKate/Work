import random

N = random.randint(1,100)
arr=[random.randint(-10,10) for i in range(N)]
print(arr)

for i in range(N):
    if arr[i] < 0:
        arr.insert( i+1 , arr[i]**2)
if arr[-1] < 0:
    arr.append(arr[-1]**2)

print(arr)
