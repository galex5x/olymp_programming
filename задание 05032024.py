def find(name, filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            fio, phone = line.strip().split(',')
            if fio == name:
                return phone
    return "Телефон не найден"
filename = 'num.csv'
name = input("Введите ФИО: ")
phone = find(name, filename)
print("Телефон:", phone)
