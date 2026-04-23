![[Pasted image 20260423140948.png]]

## __Problematika__

Tento program je napsaný v Pythonu a slouží k zpracování dat o surovinách z JSON souboru. Načíta data, shromažďuje množství podle ID, seřadí suroviny podle názvu a přepočítá porce pro dospělé a děti. Je to užitečné pro např. recepty nebo nakupní seznamy.

## Klíčové zdrojové kódy

### 1. Načtení surovin
```python
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
```

### 2. Řazení surovin
```python
def sort_ingredients(ingredients_list):
    return sorted(ingredients_list, key=lambda x: x['name'])
```

### 3. Přepočet porcí
```python
def calculate_portions(ingredients, adults, childs):
    portions = adults + childs * 0.5
    for ing in ingredients:
        ing['quantity'] *= portions
    return ingredients
```

## Výsledky práce

Program běží v terminálu a vypisuje výsledky:

- **Načtené suroviny:** Zobrazuje suroviny z JSON (např. Cukr má 60g, protože 10+50).
- **Seřazené suroviny:** Seřazené podle názvu (Cukr, Mouka, Vejce).
- **Přepočtené porce:** Pro 2 dospělé a 2 děti (celkem 3 porce), množství * 3 (např. Mouka 1500g, Cukr 180g).