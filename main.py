class Receipt:

    def __init__(self, filepath):
        self.filepath = filepath

WORDS = []

def to_list(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            for word in line.split():
                if word != (":" or "."):
                    WORDS.append(word)

def find_phone():                       # Finds phone number
    for x in range(0, len(WORDS)):
        if "tel" or "ph" or "cont" in WORDS[x].lower():
            try:                        # Test to see if entry is a number
                word = WORDS[x+1]
                new_word = int(word[:1])
                if "-" in word or "." in word:      # Niceties
                    WORDS[x+1] = word.replace(".","-")
                else:
                    if len(WORDS[x+1]) == 10:
                        WORDS[x+1] = word[:3] + "-" + word[3:6] + "-" + word[6:]
                return WORDS[x+1]
                break
            except ValueError:          # If string after tel, ph or cont is actually not an integer
                continue


