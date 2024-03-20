cook_book = {}
# ingredients_list = []

with open('cookBook.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        ingredients_list = []
        dish = line.strip()
        ingredient_quantity = int(f.readline())
        for ingredients in range(ingredient_quantity):
            ingredient = f.readline()
            ingredient_name, quantity, measure = ingredient.strip().split(' | ')
            ingredients_list.append({'ingredient_name': ingredient_name,
                                     'quantity': quantity,
                                     'measure': measure})
            a = {dish: ingredients_list}
        empty_string = f.readline()
        cook_book.update(a)
    print(cook_book)