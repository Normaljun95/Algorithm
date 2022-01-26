T = int(input())
for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    maxValue = num[0]
    for i in range(len(num)):
        if maxValue < num[i]:
            maxValue = num[i]
        else:
            continue
    print('#'+str(test_case), str(maxValue))