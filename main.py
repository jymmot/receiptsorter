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
                        temp = self.words[x][y+1]   # Ensures phone number doesn't mess with future operations
                        self.words[x].pop(y+1)
                        return temp
                    except ValueError:          # If string after tel, ph or cont is actually not an integer
                        continue

    def find_items(self):                       # Finds items with corresponding prices
        items = []
        temp_cost = None
        temp_name = None
        for x in range(0, len(self.words)):
            for y in range(0, len(self.words[x])):
                word = self.words[x][y]
                try:
                    if len(word) >= 3 and word[len(word)-3] == ".":
                        temp_cost = float(word)
                        temp_name = " ".join(self.words[x][:-1])
                        
                        if not any((c in temp_name.lower()) for c in \
                        ["total", "tax", "cash", "change", "tip", "balance"]):
                            items.append({temp_name: temp_cost})
                except ValueError:
                    continue

                if len(items) > 0:
                    if len(self.words[x]) == 0 and any((c in self.words[x+1].lower()) for c in \
                    ["total", "tax", "cash", "change", "tip", "balance"]):
                        return items

        return items

receipt = Receipt("images/1.txt")
receipt.to_list()
print receipt.find_phone()
print receipt.find_items()
