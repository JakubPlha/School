import json

def load_ingredients(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    ingredients = {}
    for item in data:
        id_ = item['id']
        name = item['nm']
        qty = item['qty']
        if id_ in ingredients:
            ingredients[id_]['quantity'] += qty
        else:
            ingredients[id_] = {'id': id_, 'name': name, 'quantity': qty}
    
    return list(ingredients.values())

def sort_ingredients(ingredients_list):
    return sorted(ingredients_list, key=lambda x: x['name'])

def calculate_portions(ingredients, adults, childs):
    portions = adults + childs * 0.5
    for ing in ingredients:
        ing['quantity'] *= portions
    return ingredients

if __name__ == "__main__":
    ingredients = load_ingredients('prg/data.json')
    print("Načtené suroviny:")
    for ing in ingredients:
        print(ing)
    
    sorted_ing = sort_ingredients(ingredients)
    print("\nSeřazené suroviny:")
    for ing in sorted_ing:
        print(ing)
    
    calc_ing = calculate_portions(ingredients.copy(), 2, 2)
    print("\nPřepočtené porce pro 2 dospělé a 2 děti:")
    for ing in calc_ing:
        print(ing)