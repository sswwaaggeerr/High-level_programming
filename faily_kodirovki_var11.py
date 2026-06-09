text = "Привет мир! Это тестовый текст с русскими буквами."

codirovki = ["utf-8", "cp1251", "latin-1", "ascii"]

for kod in codirovki:
    try:
        imya_fayla = "text_" + kod + ".txt"
        f = open(imya_fayla, "w", encoding=kod)
        f.write(text)
        f.close()
        print("Запись в", imya_fayla, "(кодировка", kod, "): УСПЕШНО")
    except Exception as e:
        print("Запись в (кодировка", kod, "): ОШИБКА -", e)

print()
print("Чтение файлов:")
for kod in codirovki:
    try:
        imya_fayla = "text_" + kod + ".txt"
        f = open(imya_fayla, "r", encoding=kod)
        soderzhimoe = f.read()
        f.close()
        print(imya_fayla + ":", soderzhimoe)
    except Exception as e:
        print(imya_fayla + ": ОШИБКА ЧТЕНИЯ -", e)
