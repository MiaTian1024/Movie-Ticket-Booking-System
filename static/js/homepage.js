const search = document.querySelector(".search-box input"),
      images = document.querySelectorAll(".cards");

search.addEventListener("keyup", (e) => {
if (e.key === "Enter") {
    let searchValue = search.value.toLowerCase(); // Convert search value to lowercase
    images.forEach(image => {
        const name = image.dataset.name.toLowerCase(); // Convert attribute value to lowercase
        if (searchValue === name) {
            image.style.display = "flex";
        } else {
            image.style.display = "none";
        }
    });
}
});

search.addEventListener("keyup", () =>{
    if(search.value != "") return;

    images.forEach(image =>{
        image.style.display = "flex";
    })
})


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


// Open the Cancel
const openCancelButton = document.getElementById('openCancelButton');
const Cancel = document.getElementById('myCancel');
const closeCancelButton = document.getElementById('closeCancelButton');

openCancelButton.addEventListener('click', function() {
    Cancel.style.display = 'block';
});

// Close the cancel
closeCancelButton.addEventListener('click', function() {
    Cancel.style.display = 'none';
});

// Click outside the cancel to close it
window.addEventListener('click', function(event) {
    if (event.target == Cancel) {
        Cancel.style.display = 'none';
    }
});

// close popup
function closePopup() {
    document.querySelector('.overlay_popup').style.display = 'none';
}
