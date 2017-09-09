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
                    if "/" in word:
                        continue
                    if "-" in word or "." in word and len(self.words[x][y]) == 12:      # Niceties
                        self.words[x][y] = word.replace(".", "-")
                    else:
                        if len(self.words[x][y]) == 10:
                            self.words[x][y] = word[:3] + "-" + word[3:6] + "-" + word[6:]
                        else:
                            continue
                    temp = self.words[x][y]
                    self.words[x][y] = " "
                    return temp

    def find_price(self):
        change = False
        amt_change = 1
        costs = []
        for x in range(3, len(self.words)):
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
            if len(self.words[x]) > 0 and self.words[x][0][0] == "\"":
                continue
            for y in range(0, len(self.words[x])):
                word_list.append(self.words[x][y])
        return word_list

    def switch(self,x):
        return {
            0: "Food",
            1: "Grocery",
            2: "Utilities",
            3: "Entertainment",
            4: "Medical"
        }.get(x, "Personal")

    def categorizer(self, a):
        cats = [0,0,0,0,0,0]
        word_list = a
        for i in range(0, len(word_list)):
            for x in range(0, len(categories)):
                for y in range(0, len(categories[x])):
                    if word_list[i].lower() == categories[x][y]:
                        cats[x] += 1
        return self.switch(cats.index(max(cats)))

categories = [["restaurant", "grill", "poach", "steamed", "neighborhood", "cafe", "fine dining", 
"baghaar", "bake", "caramelize", "claypot", "roasted", "pan fried", "sear", "puree", "blanche"], 
["fruit", "apples", "avocados", "bananas", "berries", "cherries", "citrus", "orange", "lemons", 
"nuts", "flowers", "juice", "grapes", "melons", "pears", "snack packs", "asparagus", "avocados", 
"beans", "peas", "broccoli", "cauliflower", "brussels sprouts", "carrot", "celery", "corn", 
"cucumbers", "eggplant", "herb", "green salad", "lettuce", "mushrooms", "onions", "garlic", 
"peppers", "potatoes", "snack", "spinach", "sprouts", "squash", "zucchini", "tomatoes", "beef", 
"pork", "lamb", "veal", "specialty", "crab", "fish", "steaks", "lobster", "oil", "sauce", "mussels", 
"clams", "oysters", "scallops", "shrimp", "dairy", "yogurt", "milk", "cream", "creamers", "cheese", 
"eggs", "butter", "margarine", "biscuits", "dough", "pasta", "sauce", "hummus", "dips", "salsa", 
"guacamole", "packs", "pudding", "gelatin", "condiments", "sour", "soy", "chili", "mustard", 
"ketchup", "jam", "peanut", "honey", "pancake", "soap", "shampoo", "cleaning", "detergent", "powder", 
"salt", "sugar", "pepper", "chive", "cookie", "ice cream", "eggplant"], ["screws", "bolts", "wrench", 
"repair", "ladder", "wires", "tires", "tools", "nails", "fuel", "gas", "car", "motor", "electronic", 
"computer", "monitor", "phone", "keyboard", "mouse", "comfort", "bed", "printer", "toner", "office", 
"supplies", "paint", "color", "devices", "fridge", "stove", "oven", "cooker", "bulb", "camera", 
"television", "dryer", "washer", "scooter", "bicycle", "sunscreen", "scanner"], ["golf", "soccer", 
"ball", "music", "movie", "ticket", "tennis", "basketball", "watch", "band", "concert", "theatre", 
"drama", "toy", "sports", "activity", "baseball", "softball", "archery", "cricket", "dancing", 
"ballet", "snowboarding", "trek", "climbing", "cycling", "horse", "fishing", "book", "games"], 
["allergies", "flu", "conjunctivitis", "diarrhea", "headaches", "mononucleosis", "aches", "asthma", 
"cough", "fever", "medicine", "panadol", "antibiotics", "treatment", "hospital", "ambulance", "ward", 
"antiseptic", "medical", "prevention", "vitamin", "iron", "paracetamol", "painkiller", "sore", 
"mylanta", "lozenges", "thermometer", "calamine", "gauze", "aspirin"]]

receipt = Receipt("images/1.txt")
receipt.to_list()
print receipt.find_phone()
print receipt.find_price()
print receipt.find_date()
print receipt.categorizer(receipt.list_word())
