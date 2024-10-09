for i in range(2, 10001):
    # sum = 0
    # for j in range(1, i):
    #     if i % j == 0:
    #         sum += j
    # if sum == i:
    #     print(i)

    if sum(j for j in range(1, i) if i % j == 0) == i:
        print(i)
