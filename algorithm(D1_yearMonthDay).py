T = int(input())
day31 = ['01', '03', '05', '07', '08', '10', '12']
day30 = ['04', '06', '09', '11']
for test_case in range(1, T + 1):
    num = input()
    year = num[:4]
    month = num[4:6]
    day = num[6:]
    for i in range(1):
        if month in day31:
            if (int(day) <= 31) and (int(day) >= 1):
                print('#'+str(test_case), year+'/'+month+'/'+day)
            else:
                print('#'+str(test_case), '-1')
        elif month in day30:
            if (int(day) <= 30) and (int(day) >= 1):
                print('#'+str(test_case), year+'/'+month+'/'+day)
            else:
                print('#'+str(test_case), '-1')
        elif month == '02':
            if (int(day) <= 28) and (int(day) >= 1):
                print('#'+str(test_case), year+'/'+month+'/'+day)
            else:
                print('#'+str(test_case), '-1')
        else:
            print('#'+str(test_case), '-1')