T = int(input())
for test_case in range(1, T + 1):
    width = int(input())
    arr = [[0]*width for j in range(width)]
    print('#'+str(test_case))
    for j in range(width):
        for i in range(j+1):
            if j ==0 or j == i:
            	arr[j][i] = 1
            else:
            	arr[j][i] = arr[j-1][i-1] + arr[j-1][i]
    for u in range(width):
        for v in range(width):
            if arr[u][v] == 0:
                print("", end='')
            else:
                print(str(arr[u][v]) + " ", end='')
        print()