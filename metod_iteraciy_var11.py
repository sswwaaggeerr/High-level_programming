import math
x0 = 0.5
tochnost = 0.0001
max_iter = 100
x = x0
iter_count = 0
for i in range(max_iter):
    x_new = math.exp(-x)
    iter_count = iter_count + 1
    if abs(x_new - x) < tochnost:
        break
    x = x_new
print("Корень уравнения: x =", round(x_new, 5))
print("Количество итераций:", iter_count)
result = math.exp(-x_new) - x_new
print("f(", round(x_new, 5), ") = ", round(result, 6), sep="")
