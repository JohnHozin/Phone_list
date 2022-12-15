def get_number():
    print("Для выхода введите: exit или 0")
    family = ""
    phones = []
    while (True):
        family = input('family = ')
        if family == "exit" or family == "0":
            break
        name = input('name = ')
        phone = input('phone = ')
        note = input('note = ')
        phones.append((family, name, phone, note))
    return phones


def get_number_line():
    return input()


def get_number_line_example():
    return print("пример: Иванов; Иван; 89172858585; сотовый")

