class Receipt:

    def __init__(self, filepath):
        self.filepath = filepath

    def to_list(self):
        with open(self.filepath) as f:
            self.words = [line.split() for line in f]

    def find_phone(self):                       # Finds phone number
        for x in range(0, len(self.words)):
            for y in range(0, len(self.words[x])):
                if self.words[x][y][0].isdigit():
                    word = self.words[x][y]
                    if "-" in word or "." in word:      # Niceties
                        self.words[x][y] = word.replace(".", "-")
                    else:
                        if len(self.words[x][y]) == 10:
                            self.words[x][y] = word[:3] + "-" + word[3:6] + "-" + word[6:]
                    temp = self.words[x][y]
                    self.words[x][y] = " "
                    return temp

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
                        if word[0] == "$":
                            word = word[1:]
                        costs.append(float(word))
                        self.words[x].remove(word)
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
    
    def find_date(self):
        for x in range(0, len(self.words)):
            for y in range(0, len(self.words[x])):
                word = self.words[x][y]
                if word[0].isdigit():
                    if any((c in word) for c in ["/", "-"]):
                        if word.count("/") == 2 or word.count("-") == 2:
                            return word

    def list_word(self):
        word_list = []
        for x in range(0, len(self.words)):
            if self.words[x][0][0] == "\"":
                continue
            for y in range(0, len(self.words[x])):
                word_list.append(self.words[x][y])
        return word_list

receipt = Receipt("receipt.txt")
receipt.to_list()
print receipt.find_phone()
print receipt.find_price()
print receipt.find_date()
print receipt.list_word()


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
