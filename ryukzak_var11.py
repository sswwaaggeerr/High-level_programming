W = 40
ves = [2, 5, 8, 11, 14]
stoimost = [3, 6, 9, 12, 15]
n = len(ves)
dp = []
for i in range(n + 1):
    row = []
    for w in range(W + 1):
        row.append(0)
    dp.append(row)
for i in range(1, n + 1):
    for w in range(W + 1):
        dp[i][w] = dp[i - 1][w]
        if ves[i - 1] <= w:
            new_stoimost = dp[i - 1][w - ves[i - 1]] + stoimost[i - 1]
            if new_stoimost > dp[i][w]:
                dp[i][w] = new_stoimost
max_stoimost = dp[n][W]
print("Максимальная стоимость:", max_stoimost)
vzyatye = []
w = W
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        vzyatye.append(i - 1)
        w = w - ves[i - 1]
vzyatye.reverse()
print("Взяты предметы (номера):", vzyatye)
print("Взятые предметы:")
sum_ves = 0
sum_stoimost = 0
for nomer in vzyatye:
    print("  Предмет", nomer + 1, ": вес =", ves[nomer], ", стоимость =", stoimost[nomer])
    sum_ves = sum_ves + ves[nomer]
    sum_stoimost = sum_stoimost + stoimost[nomer]
print("Общий вес:", sum_ves)
print("Общая стоимость:", sum_stoimost)
