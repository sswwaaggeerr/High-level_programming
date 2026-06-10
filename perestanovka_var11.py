def proverit_perestanovku(spisok):
    n = len(spisok)
    for i in range(1, n + 1):
        naydeno = False
        for element in spisok:
            if element == i:
                naydeno = True
                break
        if not naydeno:
            print("Число", i, "не найдено в списке")
            return False
    return True
massiv1 = [3, 1, 2, 5, 4]
print("Массив 1:", massiv1)
if proverit_perestanovku(massiv1):
    print("Результат: Это правильная перестановка")
else:
    print("Результат: Это НЕ перестановка")

print()
massiv2 = [1, 2, 2, 4]
print("Массив 2:", massiv2)
if proverit_perestanovku(massiv2):
    print("Результат: Это правильная перестановка")
else:
    print("Результат: Это НЕ перестановка")
