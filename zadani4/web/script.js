// recioes
let recipes = [
    { name: 'Spaghetti Bolognese', difficulty: 3, ingredients: 'Maso, rajčata, cibule, těstoviny' },
    { name: 'Pizza Margherita', difficulty: 4, ingredients: 'Těsto, rajčata, mozzarella, bazalka' },
    { name: 'Zeleninový salát', difficulty: 1, ingredients: 'Zelenina, olivový olej, ocet' }
];

// render
function renderRecipes(recipesToRender) {
    const container = document.getElementById('recipes-container');
    container.innerHTML = '';
    recipesToRender.forEach(recipe => {
        const card = document.createElement('div');
        card.className = 'recipe-card';
        
        const name = document.createElement('div');
        name.className = 'recipe-name';
        name.textContent = recipe.name;
        
        const difficulty = document.createElement('div');
        difficulty.className = 'difficulty';
        difficulty.innerHTML = `
            <div>Obtížnost:</div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: ${(recipe.difficulty / 5) * 100}%"></div>
            </div>
        `;
        
        const button = document.createElement('button');
        button.textContent = 'Ingredience';
        button.onclick = () => alert(`Ingredience pro ${recipe.name}: ${recipe.ingredients}`);
        
        card.appendChild(name);
        card.appendChild(difficulty);
        card.appendChild(button);
        
        container.appendChild(card);
    });
}

renderRecipes(recipes);

// Search
document.getElementById('search').addEventListener('input', function() {
    const query = this.value.toLowerCase();
    const filtered = recipes.filter(recipe => recipe.name.toLowerCase().includes(query));
    renderRecipes(filtered);
});

// Add recipe
document.getElementById('add-recipe-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('recipe-name').value.trim();
    const prepTime = document.getElementById('prep-time').value;
    
    if (name && prepTime) {
        // difficulty
        const newRecipe = {
            name: name,
            difficulty: Math.floor(Math.random() * 5) + 1, // Random difficulty 1-5
            ingredients: 'Ingredience budou přidány později'
        };
        recipes.push(newRecipe);
        renderRecipes(recipes);
        
        // Reset
        this.reset();
        
        // Scroll
        document.getElementById('recepty').scrollIntoView();
    }
});