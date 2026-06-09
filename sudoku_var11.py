import time

pole = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

shag = 0

def vyvesti_pole(p):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        stroka = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                stroka += " | "
            if p[i][j] == 0:
                stroka += " . "
            else:
                stroka += " " + str(p[i][j]) + " "
        print(stroka)

def nayti_pustuyu(p):
    for i in range(9):
        for j in range(9):
            if p[i][j] == 0:
                return (i, j)
    return None

def proverit(p, chislo, pos):
    x, y = pos
    for i in range(9):
        if p[x][i] == chislo and i != y:
            return False
    for i in range(9):
        if p[i][y] == chislo and i != x:
            return False
    x_kv = x // 3
    y_kv = y // 3
    for i in range(x_kv * 3, x_kv * 3 + 3):
        for j in range(y_kv * 3, y_kv * 3 + 3):
            if p[i][j] == chislo and (i, j) != pos:
                return False
    return True

def reshit(p):
    global shag
    naydena = nayti_pustuyu(p)
    if not naydena:
        return True
    else:
        x, y = naydena
    
    for chislo in range(1, 10):
        if proverit(p, chislo, (x, y)):
            p[x][y] = chislo
            shag = shag + 1
            
            if shag <= 50:
                print("Шаг", shag, ": ставим", chislo, "в позицию (", x, ",", y, ")")
            
            if reshit(p):
                return True
            
            p[x][y] = 0
    
    return False

print("Исходное поле:")
vyvesti_pole(pole)
print()
print("Решение:")
print()

if reshit(pole):
    print()
    print("Решено!")
    print("Всего шагов:", shag)
    print()
    print("Решённое поле:")
    vyvesti_pole(pole)
else:
    print("Решения не существует")
