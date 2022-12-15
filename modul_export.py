def write_in_txt(data):
    with open('file.txt', 'a') as file:
        for i in data:
            file.write('; '.join(str(s) for s in i) + '\n')


def write_in_csv(data):
    with open('file.csv', 'a') as file:
        for i in data:
            file.write('; '.join(str(s) for s in i) + '\n')


def print_from_txt():
    with open('file.txt', 'r') as file:
        for i in file:
            print(i, end="")
