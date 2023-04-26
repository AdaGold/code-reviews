def twoSum(num, t):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[j] == t - num[i]:
                return [i, j]
