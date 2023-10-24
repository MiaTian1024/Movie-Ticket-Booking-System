// Get a reference to the form element
const form = document.getElementById('filter-form');

// Get a reference to the radio buttons
const radioButtons = form.querySelectorAll('input[type="radio"]');

// Add an event listener to each radio button
radioButtons.forEach((radioButton) => {
    radioButton.addEventListener('change', function () {
        // Automatically submit the form when a radio button is selected
        form.submit();
    });
});

// Open the modal
const openModalButton = document.getElementById('openModalButton');
const modal = document.getElementById('myModal');
const closeModalButton = document.getElementById('closeModalButton');

openModalButton.addEventListener('click', function() {
    modal.style.display = 'block';
});

// Close the modal
closeModalButton.addEventListener('click', function() {
    modal.style.display = 'none';
});

// Click outside the modal to close it
window.addEventListener('click', function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
});

function closePopup() {
    document.querySelector('.overlay_popup').style.display = 'none';
}
