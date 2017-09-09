def to_list(filepath):
    words = []

    with open(filepath, 'r') as f:
        for line in f:
            for word in line.split():
                words.append(word)

    print words

to_list('receipt.txt')
