with open("book.txt", "r") as f:
    for line in f.readlines():
        book = list(line.split())
        encoder = [item[0] for item in book]
        title = ''
        for x in encoder:
            title += x
        print(title)