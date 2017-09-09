words = []

def to_list(filepath):

    with open(filepath, 'r') as f:
        for line in f:
            for word in line.split():
                if word != (":" or "."):
                    words.append(word)

to_list('receipt.txt')

phone_number = 0

def find_phone():                       # Finds phone number
    phone_ind = 0
    for x in range(0, len(words)):
        if "tel" or "ph" or "cont" in words[x].lower():
            try:                        # Test to see if entry is a number
                word = words[x+1]
                new_word = int(word[:1])
                if "-" in word or "." in word:      # Niceties
                    words[x+1] = word.replace(".","-")
                else:
                    if len(words[x+1]) == 10:
                        words[x+1] = word[:3] + "-" + word[3:6] + "-" + word[6:]
                phone_ind = x+1
                break
            except ValueError:
                continue
    global phone_number = words[phone_ind]

