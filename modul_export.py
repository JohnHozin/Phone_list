def write_in_txt(data):
    with open('file.txt', 'a') as file:
        for i in data:
            print(i, file=file)
            # line.append(i)
