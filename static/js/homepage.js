const search = document.querySelector(".search-box input"),
      images = document.querySelectorAll(".cards");

search.addEventListener("keyup", e =>{
    if(e.key == "Enter"){
        let searcValue = search.value,
            value = searcValue.toUpperCase();
            images.forEach(image =>{
                if(value === image.dataset.name){ //matching value with getting attribute of images
                    return image.style.display = "flex";
                }
                image.style.display = "none";
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

function closePopup() {
    document.querySelector('.overlay_popup').style.display = 'none';
}
