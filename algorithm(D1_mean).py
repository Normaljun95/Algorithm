T = int(input())
for test_case in range(1, T+1):
    num = map(int, input().split())
    sum = 0
    for i in range(len(num)):
        sum += num[i]
    print('#'+str(test_case), str(round(sum/len(num))))