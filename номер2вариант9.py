def find_birthdays(classmates, month):
    birthdays = []
    for name, birthday in classmates.items():
        if birthday[1].lower() == month.lower():
            birthdays.append((name, birthday[0]))
    return birthdays

classmates = {
    "Иван": ("15", "Январь"),
    "Мария": ("25", "Февраль"),
    "Алексей": ("10", "Январь"),
    "Елена": ("5", "Март"),
    "Петр": ("20", "Апрель"),
    "Ольга": ("30", "Май"),
    "Дмитрий": ("12", "Июнь"),
    "Анна": ("8", "Июль"),
    "Сергей": ("18", "Август"),
    "Наталья": ("22", "Сентябрь"),
    "Иван": ("15", "Январь"),
    "Мария": ("25", "Февраль"),
    "Алексей": ("10", "Январь"),
    "Елена": ("5", "Март"),
    "Петр": ("20", "Апрель"),
    "Ольга": ("30", "Май"),
    "Даниил": ("26", "Июль"),
    "Ника": ("9", "Июль"),
    "Елена": ("12", "Август"),
    "Ульяна": ("32", "Сентябрь")
}

query_month = input("Введите месяц запроса: ")

result = find_birthdays(classmates, query_month)

if result:
    for name, day in result:
        print(name, day)
else:
    print()
