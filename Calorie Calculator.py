class food():
    def __init__(self, item, carbs, protein, fat):
        self.item = item
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

        print(f'''Food: {self.item}
Carboydrates(g): {self.carbs}
Protein(g): {self.protein}
Fat(g): {self.fat}
---------------------
''')

    def calories(self):
        print(f'The total number of calories in a {self.item} is {(self.carbs * 4) + (self.protein * 4) + (self.fat * 9)}.')


carrot = food(item='Carrot', carbs=6, protein=9, fat=0.2)
pizza = food(item='Pizza', carbs=33, protein=11, fat=10)
mango = food(item='Mango', carbs=15, protein=0.8, fat=0.4)

carrot.calories()
pizza.calories()
mango.calories()
