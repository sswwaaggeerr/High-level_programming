class Uzol:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DvusvyaznySpisok:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dlina = 0
    def dobavit_v_konets(self, data):
        novy_uzol = Uzol(data)
        if self.head is None:
            self.head = novy_uzol
            self.tail = novy_uzol
        else:
            self.tail.next = novy_uzol
            novy_uzol.prev = self.tail
            self.tail = novy_uzol
        self.dlina = self.dlina + 1
    def dobavit_v_nachalo(self, data):
        novy_uzol = Uzol(data)
        if self.head is None:
            self.head = novy_uzol
            self.tail = novy_uzol
        else:
            novy_uzol.next = self.head
            self.head.prev = novy_uzol
            self.head = novy_uzol
        self.dlina = self.dlina + 1
    def get_s_konca(self, index):
        if index < 1 or index > self.dlina:
            return None
        current = self.tail
        for i in range(index - 1):
            current = current.prev
        return current.data
    def get_po_indexu(self, index):
        if index < 0 or index >= self.dlina:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
    def udalit_po_indexu(self, index):
        if index < 0 or index >= self.dlina:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            current = self.head
            for i in range(index):
                current = current.next
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            if current == self.tail:
                self.tail = current.prev
        self.dlina = self.dlina - 1
        return True
    def vyvesti_spisok(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result
    def vyvesti_s_konca(self):
        current = self.tail
        result = []
        while current:
            result.append(current.data)
            current = current.prev
        return result
spisok = DvusvyaznySpisok()
print("Добавляем элементы в конец: 10, 20, 30, 40, 50")
spisok.dobavit_v_konets(10)
spisok.dobavit_v_konets(20)
spisok.dobavit_v_konets(30)
spisok.dobavit_v_konets(40)
spisok.dobavit_v_konets(50)
print("Список:", spisok.vyvesti_spisok())
print("Длина:", spisok.dlina)
print()
print("Получение элементов с конца:")
for i in range(1, spisok.dlina + 1):
    znachenie = spisok.get_s_konca(i)
    print("Элемент с конца #", i, " = ", znachenie, sep="")
print()
print("Получение элементов по индексу (с начала):")
for i in range(spisok.dlina):
    znachenie = spisok.get_po_indexu(i)
    print("Элемент по индексу ", i, " = ", znachenie, sep="")
print()
print("Удаляем элемент по индексу 2:")
spisok.udalit_po_indexu(2)
print("Список после удаления:", spisok.vyvesti_spisok())
print()
print("Список с конца:", spisok.vyvesti_s_konca())
