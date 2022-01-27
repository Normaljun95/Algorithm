T = list(input())
N = []
for i in T:
    N.append(str(ord(i)-64))
print(' '.join(N))