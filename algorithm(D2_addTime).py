T = int(input())
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2
    if h > 12:
        h -= 12
    if m > 59:
        m -= 60
        h += 1        
    print('#{} {} {}'.format(test_case, h, m))