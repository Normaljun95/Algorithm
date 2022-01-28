T = int(input())
for test_case in range(1, T + 1):
    data = input()
    if data == data[::-1]:
        print('#'+str(test_case), '1')
    else:
        print('#'+str(test_case), '0')