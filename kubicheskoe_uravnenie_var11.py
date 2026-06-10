a = 2
b = 3
c = -11
d = -6
korni = []
shag = 0.001
nachalo = -10
konets = 10
x = nachalo
while x <= konets:
    result = a * x**3 + b * x**2 + c * x + d
    if abs(result) < 0.01:
        isNew = True
        for k in korni:
            if abs(k - x) < 0.5:
                isNew = False
                break
        if isNew:
            korni.append(x)
    x += shag
print("Корни уравнения:")
for i in range(len(korni)):
    print("x", i+1, " = ", round(korni[i], 1), sep="")
print("Проверка:")
for i in range(len(korni)):
    x_proverka = korni[i]
    result = a * x_proverka**3 + b * x_proverka**2 + c * x_proverka + d
    print("f(", round(x_proverka, 1), ") = ", round(result, 1), sep="")
