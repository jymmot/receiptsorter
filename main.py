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

    def find_price(self):
        change = False
        amt_change = 1
        costs = []
        for x in range(0, len(self.words)):
            for y in range(0, len(self.words[x])):
                word = self.words[x][y]
                if "change" in self.words[x][y].lower():
                    change = True
                    continue
                try:
                    if len(word) >= 3 and word[len(word)-3] == ".":
                        if word[0:1] == "$":
                            word = word[1:]
                        costs.append(float(word))

                except ValueError:
                    continue
        
        if not change:
            max_cost = str(max(costs))
            while len(max_cost) - max_cost.index(".") < 3:
                max_cost += "0"
            return max_cost

        else:
            cost2 = costs[:costs.index(max(costs))]
            max_cost = str(max(cost2))
            while len(max_cost) - max_cost.index(".") < 3:
                max_cost += "0"
            return max_cost

receipt = Receipt("receipt.txt")
receipt.to_list()
print receipt.find_phone()
print receipt.find_price()



''' def find_items(self):                       # Finds items with corresponding prices
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
        return items'''
