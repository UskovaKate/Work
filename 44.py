import random
N = random.randint(1,100)
arr = [random.randint(-10,10) for i in range(N)]
print(arr)
plus = 0
minus = 0

for i in range(N):
    if arr[i] >0:
        plus+=1
    elif arr[i] <0:
        minus+=1
if plus > minus:
    for i in range(minus , plus):
        arr.append(random.randint(-100,-1))
elif plus < minus:
    for i in range(plus , minus):
        arr.append(random.randint(1,10))

print("Nomber plus: " + str(plus))
print("Nomber minus: " + str(minus))
print(arr)
