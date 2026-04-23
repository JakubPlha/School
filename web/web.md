![[Pasted image 20260423134856.png]]

## __Problematika__

Tento web je o evidenci receptu. Je to jednoduchá webová aplikace napsaná v HTML, CSS a JavaScript. Umožňuje prohlížet pěeddělané recepty, hledat je podle názvů, a přidávat nové recepty s obtížností.

## Klíčové zdrojové kódy

### 1. HTML - Formulář pro přidání receptu
```html
<form id="add-recipe-form">
    <label for="recipe-name">Název receptu (max 15 znaků):</label>
    <input type="text" id="recipe-name" maxlength="15" required>
    
    <label for="prep-time">Doba přípravy (minuty):</label>
    <input type="number" id="prep-time" min="1" required>
    
    <button type="submit">Přidat recept</button>
</form>
```

### 2. JavaScript - Přidání nového receptu
```javascript
document.getElementById('add-recipe-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('recipe-name').value.trim();
    const prepTime = document.getElementById('prep-time').value;
    
    if (name && prepTime) {
        const newRecipe = {
            name: name,
            difficulty: Math.floor(Math.random() * 5) + 1,
            ingredients: 'Ingredience budou přidány později'
        };
        recipes.push(newRecipe);
        renderRecipes(recipes);
        this.reset();
    }
});
```

### 3. CSS - Styl pro kartu receptu
```css
.recipe-card {
    background-color: white;
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.recipe-card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
```
