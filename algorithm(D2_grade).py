T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    student = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for n in range(N):
        mid, fin, hw = map(int, input().split())
        sum = mid * 0.35 + fin * 0.45 + hw * 0.2
        student.append(sum)
    k_score = student[K-1]
    student.sort(reverse=True)
    result = student.index(k_score) // (N//10)
    k_grade = grade[result]
    print('#{} {}'.format(t, k_grade))