import random

N = random.randint(1,100)
arr = [random.randint(-10,10) for i in range(N)]
print(arr)

for i in range(N):
    if arr[i] == 0:
        t = arr[i-1] + arr[i-2] 
        arr[i] = t
print(arr)
