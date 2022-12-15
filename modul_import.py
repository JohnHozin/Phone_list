def get_number():
    print("Для выхода введите в поле Фамилия: exit или 0")
    phones = []
    while (True):
        family = input('Фамилия = ')
        if family == "exit" or family == "0":
            break
        name = input('Имя = ')
        phone = input('Телефон = ')
        note = input('Описание = ')
        phones.append((family, name, phone, note))
    return phones


def get_number_line():
    print("пример: Иванов; Иван; 89172858585; сотовый")
    phones = []
    while (True):
        phones_data = input()
        if phones_data == "exit" or phones_data == "0" or phones_data.count(";") != 3:
            break
        family, name, phone, note = phones_data.split(";")
        family = family.replace(" ", "")
        name = name.replace(" ", "")
        phone = phone.replace(" ", "")
        note = note.replace(" ", "")
        phones.append((family, name, phone, note))
    return phones




# sfdgsdf; sdfgsd; dsfgsd; sdfgsdfg
# sdfgsdfg;sdfgsdfg;sdfgsdf;sdfgsdfg
# dfsgsdfg ; dfsgdfg ; dsfgsdfg ; dfsgsdfg



