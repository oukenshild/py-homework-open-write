recipes_file = 'recipes.txt'

# Задача №1
def file_reader(recipes_file):
    with open(recipes_file, encoding='utf-8') as file:
        global cook_book
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredients = []
            for item in range(int(file.readline())):
                ingredient = file.readline().split(' | ')
                ingredients.append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2].strip()})
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book

dishes = file_reader(recipes_file)
print(dishes)

# Задача №2

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    result[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': (ingredient['quantity'] * person_count)}
        else:
            print(f'Этого блюда нет в поваренной книге')
    return result

dishes_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(dishes_list)

# Задача №3

import os

catalog_name = 'Files_merged'
merged_file_name = 'merged.txt'

base_path = os.getcwd()
catalog_path = os.path.join(base_path, catalog_name)
merged_file_name_path = os.path.join(base_path, merged_file_name)

def process_files(base_path, catalog_path):
    files = os.listdir(catalog_path)
    files_data = {}
    for filename in files:
      with open(os.path.join(catalog_path, filename), 'r', encoding='utf-8') as read_file:
        file_lines = read_file.readlines()
        count = len(file_lines)
        files_data[filename] = count
        files_data[filename] = file_lines
    sorted_files_data = sorted(files_data.items(), key=count)
    with open(merged_file_name_path, 'w') as write_file:
            write_file.write(sorted_files_data)

process_files(base_path, catalog_path)