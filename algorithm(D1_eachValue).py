T = int(input())
sum = 0
for i in range(T-1, -1, -1):
    num = T//(10**i)
    sum += num
    T = T-num*(10**i)
print(sum)