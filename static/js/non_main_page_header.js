// Get the header
var header = document.getElementById("header_wrapper");
let changing = document.getElementById("changing");
let main_header = document.getElementById("main_header");
// Get the offset position of the navbar
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
    if (screen.width >767) {
        if (window.pageYOffset > sticky) {
            header.classList.add("sticky");
            header.style.backgroundColor = "white";
            changing.style.display = "block";
            main_header.style.paddingBottom = "0vw";
        } else {
            header.classList.remove("sticky");
            header.style.backgroundColor = "transparent";
            main_header.style.paddingBottom = "15vw";
            changing.style.display = "none";

        }
    }
}