function increase() {
  let input = document.getElementById('quantity');
  let value = parseInt(input.value);
  let max = parseInt(input.getAttribute('max')); // Converte para número

  if (value < max) {
    input.value = value + 1;
  }
}

function decrease() {
  let input = document.getElementById('quantity');
  let value = parseInt(input.value);
  let min = parseInt(input.getAttribute('min')); // Converte para número

  if (value > min) {
    input.value = value - 1;
  }
}

const selectAllCheckbox = document.getElementById('selectAll');
const itemCheckboxes = document.querySelectorAll('.itemCheckbox');

selectAllCheckbox.addEventListener('change', () => {
  itemCheckboxes.forEach(checkbox => {
    checkbox.checked = selectAllCheckbox.checked;
  });
});