class Receipt:

    def __init__(self, filepath):
        self.filepath = filepath

    def to_list(self):
        with open(self.filepath) as f:
            self.words = [line.split() for line in f]

    def find_phone(self):                       # Finds phone number
        for x in range(0, len(self.words)):
            for y in range(0, len(self.words[x])-1):
                if any((c in self.words[x][y].lower()) for c in ["tel", "ph", "cont"]):
                    try:                    # Test to see if entry is a number
                        word = self.words[x][y+1]
                        new_word = int(word[:1])
                        if "-" in word or "." in word:      # Niceties
                            self.words[x][y+1] = word.replace(".","-")
                        else:
                            if len(self.words[x][y+1]) == 10:
                                self.words[x][y+1] = word[:3] + "-" + word[3:6] + "-" + word[6:]
                        return self.words[x][y+1]
                        break
                    except ValueError:          # If string after tel, ph or cont is actually not an integer
                        continue

    def find_items(self):
        items = []
        for x in range(0, len(self.words)):
            temp_cost=0
            word = self.words[x]
            if word[len(word)-3] == ".":


receipt = Receipt("receipt.txt")
receipt.to_list()
print receipt.find_phone()