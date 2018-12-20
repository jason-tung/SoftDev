//Team Azrael:  Derek C, Jason T
//SoftDev1 pd8
//K #29: Sequential Progression II: Electric Boogaloo
//2018-12-19

var fib = (n) => {

    var window = [0, 1];

    if(n < 2){
        return window[n];
    }else{
        var inc = 2;
        while(inc <= n){
            window[inc % 2] = window[(inc + 1) % 2] + window[inc % 2];
            inc++;
        }
        return window[(inc - 1) % 2];
    }
}

var gcd = (a, b) =>{
    temp = b;
    while(b != 0)
    {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
};

students = ["dog", "cat", "tbm", "dw", "k"];

var randomStudent = () =>{
  return students[Math.floor(Math.random()*students.length)];
};

var disp = (element, fx) => {
    console.log(fx);
    console.log(element);
    document.getElementById(element).innerText = fx;
};

var fibButton = document.getElementById("fib");
//console.log(fibButton);
fibButton.addEventListener('click',function(){
    var n = document.getElementById("fibarg").value;
    disp("fibres",fib(n))
});

var gcdButton = document.getElementById("gcd");
//console.log(gcdButton);
gcdButton.addEventListener('click', function(){
    var a = document.getElementById("gcdarg1").value;
    var b = document.getElementById("gcdarg2").value;
    disp("gcdres",gcd(a,b))
});

var studentButton = document.getElementById("rs");
//console.log(studentButton);
studentButton.addEventListener('click', function(e){console.log(e);disp("rsres",randomStudent())});