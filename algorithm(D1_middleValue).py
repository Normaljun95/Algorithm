T = int(input())
for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    num.sort()
    p = int(len(num)/2)
    print(num[p])
    break