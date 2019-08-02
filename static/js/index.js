var slideIndex = 1;
var collapsed = false;
showDivs(slideIndex);
expand();

function plusDivs(n) {
    showDivs(slideIndex += n);
}

function showDivs(n) {
    var i;
    var x = document.getElementsByClassName("mySlides");
    if (n > x.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = x.length
    }
    ;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    x[slideIndex - 1].style.display = "block";
}

function expand() {

    var d = window.matchMedia("(max-width: 700px)")
    const x = document.getElementById("buttonvav");
    const y = document.getElementById("nav");
    const z = document.getElementsByClassName("zeby");
    var list = document.getElementById("rest");
    if ( list.style.display === "block") {
        y.style.position = "";
        z[0].style.display = "block";
        list.style.display="none";

    } else {
        y.style.height = "auto";
        z[0].style.display = "none";
        list.style.display="block";

    }
}