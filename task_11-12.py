class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_calories(self, new_calories):
        self.calories = new_calories

    def get_calories(self):
        return self.calories

    def is_healthy(self):
        try:
            self.to_string()
            return True if self.calories <= 200 else False
        except TypeError:
            return False

    def is_delicious(self):
        return True

    def to_string(self):
        print("Dessert:", self.name, "has calories:", self.calories)


class JellyBean(Dessert):
    def __init__(self, name, calories):
        super().__init__(name, calories)

    def is_delicious(self):
        try:
            return False if self.name == 'black licorice' else True
        except TypeError:
            return True


des1 = Dessert('Cake', 199)
print(des1.is_healthy())  # --> Dessert: Cake has calories: 199 True
des2 = Dessert()
print(des2.is_healthy())  # --> Dessert: None has calories: None False
des3 = Dessert('Cake', 250)
print(des3.is_healthy())  #--> Dessert: Cake has calories: 250 False
jb1 = JellyBean('black licorice', 199)
print(jb1.is_delicious())  # --> False
jb2 = JellyBean('black', 199)
print(jb2.is_delicious())  # --> True
