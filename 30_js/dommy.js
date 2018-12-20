var head = document.getElementById("h");
var thelist = document.getElementById("thelist");
var fiblist = document.getElementById("fiblist");
var b = document.getElementById("b");
var fb = document.getElementById("fb");

b.addEventListener('click', function(){
    var listele = document.getElementsByTagName("li");
    console.log(listele);
    var doggy = document.createElement("li");
    doggy.innerHTML = "item " + (listele.length);
    thelist.appendChild(doggy);
    //add event listener to hover.
})

