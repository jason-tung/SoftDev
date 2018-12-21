var head = document.getElementById("h");
var thelist = document.getElementById("thelist");
var fiblist = document.getElementById("fiblist");
var b = document.getElementById("b");
var fb = document.getElementById("fb");

var listevent = (x) =>{
    x.addEventListener('mouseover', function(){head.innerHTML = this.innerHTML});
    x.addEventListener('mouseout', function(){head.innerHTML = "Hello World!"});
    x.addEventListener('click', function(){
        x.remove();
	head.innerHTML = "Hello World!";
        lcount--;
    });
};


var listele = document.getElementsByTagName("li");
for (var i = 0; i < listele.length; i++){
    listevent(listele[i]);
}

var lcount = 8;
var fcount = 0;

b.addEventListener('click', function(){
    //var listele = document.getElementsByTagName("li");
    console.log(lcount);
    var doggy = document.createElement("li");
    doggy.innerHTML = "item " + (lcount);
    thelist.appendChild(doggy);
    listevent(doggy);
    lcount++;
})

fb.addEventListener('click', function(){
    //var fbele = document.getElementsByTagName("li");
    console.log(fcount);
    var doggy = document.createElement("li");
    console.log(fcount);
    doggy.innerHTML = fib(fcount);
    fiblist.appendChild(doggy);
    fcount++;
})


var fib = (n) => {
    var hey = [0, 1];
    if(n < 2){
        return hey[n];
    }else{
        var inc = 2;
        while(inc <= n){
            hey[inc % 2] = hey[(inc + 1) % 2] + hey[inc % 2];
            inc++;
        }
        return hey[(inc - 1) % 2];
    }
}


