document.getElementById('filter-city').addEventListener('input', function () {
    const filter = this.value.toLowerCase();
    const rows = document.querySelectorAll('#data-table tbody tr');
  
    rows.forEach(row => {
      const city = row.cells[1].textContent.toLowerCase();
      if (city.includes(filter)) {
        row.style.display = '';
      } else {
        row.style.display = 'none';
      }
    });
  });
  
  document.getElementById('filter-select').addEventListener('input', function () {
    const filter = this.value.toLowerCase();
    const options = document.querySelectorAll('#city-select option');
  
    options.forEach(option => {
      const text = option.textContent.toLowerCase();
      option.style.display = text.includes(filter) ? '' : 'none';
    });
  });
  
  document.getElementById('city-form').addEventListener('submit', function (event) {
    event.preventDefault();
    const selectedCity = document.getElementById('city-select').value;
    alert('Vybrali jste město: ' + selectedCity);
  });
  