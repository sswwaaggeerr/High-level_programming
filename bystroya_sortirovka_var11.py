import random
massiv = [95, 85, 75, 65, 55, 45, 35, 25, 15]
sposob = "middle"
count = 0
def vybor_opori(arr, left, right, tip):
    if tip == "first":
        return left
    if tip == "last":
        return right
    if tip == "middle":
        return (left + right) // 2
    if tip == "random":
        return random.randint(left, right)
    if tip == "median":
        m = (left + right) // 2
        a, b, c = arr[left], arr[m], arr[right]
        if (a <= b <= c) or (c <= b <= a):
            return m
        if (b <= a <= c) or (c <= a <= b):
            return left
        return right
def razdelenie(arr, left, right, tip):
    global count
    count = count + 1
    opora_idx = vybor_opori(arr, left, right, tip)
    oporniy = arr[opora_idx]
    print("Разделение номер:", count)
    print("Опорный элемент:", oporniy)
    print("Массив до перестановки:", arr)
    temp = arr[opora_idx]
    arr[opora_idx] = arr[right]
    arr[right] = temp
    i = left
    for j in range(left, right):
        print("Проверяем индексы: i =", i, ", j =", j)
        if arr[j] <= oporniy:
            print("Число", arr[j], "<=", oporniy, "- меняем местами с", arr[i])
            vremennaya = arr[i]
            arr[i] = arr[j]
            arr[j] = vremennaya
            i = i + 1
            print("Массив сейчас:", arr)
        else:
            print("Число", arr[j], ">", oporniy, "- ничего не делаем")
    vremennaya2 = arr[i]
    arr[i] = arr[right]
    arr[right] = vremennaya2
    print("Опорный встал на место:", arr)
    print("")
    return i
def quick_sort(arr, left, right, tip):
    if left < right:
        granica = razdelenie(arr, left, right, tip)
        quick_sort(arr, left, granica - 1, tip)
        quick_sort(arr, granica + 1, right, tip)
print("Начальный массив:", massiv)
quick_sort(massiv, 0, len(massiv) - 1, sposob)
print("---")
print("Итоговый массив:", massiv)
print("Сколько раз делили:", count)
