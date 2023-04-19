const form = document.querySelector('form');
const output = document.getElementById('output');

/*form.addEventListener('submit', event => {
const number = form.elements.number.value;

fetch(`/generateQuestions?number=${n}`, { method: 'POST' })
    .then(response => response.text())
    .then(text => {
    output.textContent = text;
    })
});*/

$("#btn").click(function() {
    alert("The Form has been Submitted.");
 });