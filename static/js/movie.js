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
