import random

massiv = [95, 85, 75, 65, 55, 45, 35, 25, 15]
sposob = "median"  # "first", "last", "middle", "median", "random"
razdelenie_count = 0

def vybor_opornogo(arr, left, right, sposob):
    if sposob == "first":
        return left
    elif sposob == "last":
        return right
    elif sposob == "middle":
        return (left + right) // 2
    elif sposob == "random":
        return random.randint(left, right)
    elif sposob == "median":
        mid = (left + right) // 2
        a = arr[left]
        b = arr[mid]
        c = arr[right]
        if a <= b <= c or c <= b <= a:
            return mid
        elif b <= a <= c or c <= a <= b:
            return left
        else:
            return right
    return right

def razdelenie(arr, left, right, sposob):
    global razdelenie_count
    razdelenie_count = razdelenie_count + 1
    
    op_index = vybor_opornogo(arr, left, right, sposob)
    oporniy = arr[op_index]
    
    print("Разделение", razdelenie_count, ":")
    print("  Опорный элемент (", sposob, "):", oporniy)
    print("  Массив до:", arr)
    
    arr[op_index], arr[right] = arr[right], arr[op_index]
    
    i = left
    for j in range(left, right):
        print("  Индексы: i=", i, ", j=", j, sep="")
        if arr[j] <= oporniy:
            print("  Сравнение", arr[j], "<=", oporniy, "? Да, меняем с элементом [", i, "]", sep="")
            arr[i], arr[j] = arr[j], arr[i]
            print("  Массив:", arr)
            i = i + 1
        else:
            print("  Сравнение", arr[j], ">", oporniy, "? Да, пропускаем")
    
    arr[i], arr[right] = arr[right], arr[i]
    print("  Ставим опорный элемент на место: меняем [", i, "] и [", right, "]", sep="")
    print("  Массив после:", arr)
    print()
    
    return i

def quick_sort(arr, left, right, sposob):
    if left < right:
        p = razdelenie(arr, left, right, sposob)
        quick_sort(arr, left, p - 1, sposob)
        quick_sort(arr, p + 1, right, sposob)

print("Исходный массив:", massiv)
print("Способ выбора опорного:", sposob)
print()

quick_sort(massiv, 0, len(massiv) - 1, sposob)

print("Отсортированный массив:", massiv)
print("Количество итераций разделения:", razdelenie_count)
