var slideIndex = 1;
var collapsed = false;
var actu = 9;
var gale = 9;
showDivs(slideIndex);
expand();

function plusDivs(n) {
    showDivs(slideIndex += n);
}

function showDivs(n) {
    var i;
    var x = document.getElementsByClassName("mySlides");
    var y = document.getElementsByClassName("info_near_slider");
    if (n > x.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = x.length
    }
    ;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
        y[i].style.display = "none";
    }
    x[slideIndex - 1].style.display = "block";
    y[slideIndex - 1].style.display = "";
}

function expand() {

    var d = window.matchMedia("(max-width: 700px)")
    const x = document.getElementById("buttonvav");
    const y = document.getElementById("nav");
    const z = document.getElementsByClassName("zeby");
    var body = document.body;
    var list = document.getElementById("rest");
    if (list.style.display === "block") {
        z[0].style.display = "block";
        list.style.display = "none";
        body.style.overflowY = "scroll";

    } else {
        z[0].style.display = "none";
        list.style.display = "block";
        body.style.overflowY = "hidden";
    }
}

function nextactu(n, m) {
    var l = document.getElementById("leftarrin");
    var r = document.getElementById("rightarrin");
    var b = document.getElementsByClassName("aktual");
    for (s = actu - 9; s < actu; s++) {
        if (s < m)
            b[s].style.display = "none";
    }
    actu += n;
    for (s = actu - 9; s < actu; s++) {
        if (s < m)
            b[s].style.display = "block";
    }
    if (actu <= 9) {
        l.style.display = "none";
    } else {
        l.style.display = "";
    }
    if (actu > m) {
        r.style.display = "none";
    } else {
        r.style.display = "";
    }
}
function expandmenu(nr) {
    var gets = document.getElementById("no"+nr);
    console.log(nr);
    if(gets.style.display==="" || gets.style.display==="none"){
        gets.style.display="block";
    }else{
        gets.style.display="none";
    }

}
function expandgroup(nr) {
    var gets = document.getElementById("grp"+nr);
    console.log(nr);
    if(gets.style.display==="" || gets.style.display==="none"){
        gets.style.display="block";
    }else{
        gets.style.display="none";
    }

}


function nextgal(n, m) {
    var l = document.getElementById("leftarrin");
    var r = document.getElementById("rightarrin");
    var b = document.getElementsByClassName("gale");
    for (s = gale - 19; s < gale; s++) {
        if (s < m)
            b[s].style.display = "none";
    }
    gale += n;
    for (s = gale - 19; s < gale; s++) {
        if (s < m)
            b[s].style.display = "block";
    }
    if (gale <= 19) {
        l.style.display = "none";
    } else {
        l.style.display = "";
    }
    if (gale > m) {
        r.style.display = "none";
    } else {
        r.style.display = "";
    }
}
function nextgal(n, m) {
    var l = document.getElementById("leftarrin");
    var r = document.getElementById("rightarrin");
    var b = document.getElementsByClassName("gale");
    for (s = gale - 19; s < gale; s++) {
        if (s < m)
            b[s].style.display = "none";
    }
    gale += n;
    for (s = gale - 19; s < gale; s++) {
        if (s < m)
            b[s].style.display = "block";
    }
    if (gale <= 19) {
        l.style.display = "none";
    } else {
        l.style.display = "";
    }
    if (gale > m) {
        r.style.display = "none";
    } else {
        r.style.display = "";
    }
}