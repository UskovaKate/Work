import random
M = random.randint(1,100)
arr = [random.randint(1,10) for i in range(M)]
m = 0

for i in range(M):
    arr[i] = input()

for i in range(M):
    m = 0
    for n in range(len(arr[i])):
        S = arr[i]
        if S[n] == "а" or S[n] == "е" or S[n] == "ё" or S[n] == "и" or S[n] == "о" or S[n] == "у" or S[n] == "ы" or S[n] == "э" or S[n] == "ю" or S[n] == "я":
            m += 1

    print("Количество глассных букв в слове " + "\"" + str(arr[i])+ "\"" + " равно "  + str(m))
