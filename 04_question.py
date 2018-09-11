def q1(n):
    # 1부터 n까지의 합 재귀 호출
    if n == 1:
        return 1
    return n + q1(n-1)


print(q1(10))
print(q1(100))
