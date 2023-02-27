from pprint import pprint
import time

def read_file():
    with open('recipes.txt', encoding='UTF-8') as file:
        cook_book = {}
        for line in file:
            name_dish = line.strip()
            x = int(file.readline())
            cook_book_all = []
            for _ in range(x):
                emp = file.readline().strip()
                ingredient, quantity, weight = emp.split(' | ')
                cook_book_all.append(
                    {'ingredient': ingredient,
                    'quantity': quantity,
                    'weight': weight}
                )
            cook_book[name_dish] = cook_book_all
            file.readline()
    return cook_book
        

def get_shop_list_by_dishes(dishes, person_count):
    # start = time.time()
    cook_book = read_file()
    dishes_dict = {}
    for dish in dishes:
        for element in cook_book[dish]:
            if element['ingredient'] not in dishes_dict:
                dishes_dict[element['ingredient']] = {'weight': element['weight'], 'quantity': int(element['quantity']) * person_count}
            else:
                dishes_dict[element['ingredient']]['quantity'] += int(element['quantity']) * person_count 
    return dishes_dict


def read_other_file(txt):
    txt_dict = {}
    ready_txt = open('final_text.txt', 'w', encoding='UTF-8')
    for book in txt:
        with open(book, encoding='UTF-8') as file:
            counter = 0
            for line in file:
                counter += 1
            txt_dict[book] = counter           
    for key, value in sorted(txt_dict.items(), key=lambda p: p[1]):
        ready_txt.writelines(f'{key}\n{value}\n')
        for line in open(key, encoding='UTF-8'):
            ready_txt.writelines(line)
        ready_txt.writelines('\n')
    ready_txt.close()

print(read_other_file(['1.txt', '2.txt', '3.txt']))
