from pprint import pprint


with open('recipes.txt', encoding = 'utf-8') as file:
    cook_book = dict()
    for line in file:
        dish_name = line.strip()
        counter = int(file.readline())
        temp_list = []

        for item in range(counter):
            ingredient, quantity, metric = file.readline().split('|')
            temp_list.append(
                {'Ингредиент': ingredient.strip(), 'Количество': quantity.strip(), 'Единица измерения' : metric.strip()}
            )
        cook_book[dish_name] = temp_list
        file.readline()





def get_shop_list_by_dishes(dishes, person_count):
    dict_dish = {}
    for key, value in cook_book.items():
        if dishes in key:
            for elem in value:
                dict_dish[elem['Ингредиент']] = {'Количество': int(quantity.strip()) * person_count,
                'Единица измерения': metric.strip()}
    return dict_dish

print(get_shop_list_by_dishes('Омлет', 5))