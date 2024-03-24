import os

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
    print(f'cook_book = {cook_book}')



def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient["ingredient_name"] not in ingredient_list:
                    ingredient_list[ingredient["ingredient_name"]] = {'measure': ingredient['measure'],
                                                                      'quantity': (int(ingredient['quantity']) * person_count)}
                else:
                    ingredient_list[ingredient["ingredient_name"]]['quantity'] += (int(ingredient['quantity']) * person_count)
    print(ingredient_list)
get_shop_list_by_dishes(["Омлет", "Бургер"], 5)


file_path_1 = os.path.join(os.getcwd(), '1.txt')
file_path_2 = os.path.join(os.getcwd(), '2.txt')
file_path_3 = os.path.join(os.getcwd(), '3.txt')
file_from_writing = os.path.join(os.getcwd(),'file_from_writing')
files_all = [file_path_1, file_path_2, file_path_3]
total_count_str = []
for file in files_all:
    with open(file, 'rt', encoding='utf-8') as f:
        count_str = 0
        for line in f:
            f.readline()
            count_str += 1
        total_count_str.append(count_str)
contents = [file_path_1.readlines(), file_path_2.readlines(), file_path_3.readlines()]
line_content = {}
for key in total_count_str:
    for value in contents:
        line_content[key] = value
sorted_line_content = dict(sorted(line_content.items()))


