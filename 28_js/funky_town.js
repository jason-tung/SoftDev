 // azrael - Jason Tung and Vincent Chi
 // SoftDev1 pd8
 // K28 -- Sequential Progression
 // 2018-12-18


var fibonacci = function(n){
	if (n < 2)
		return n;
	else
		return fibonacci(n - 1) + fibonacci(n - 2);
};

function gcd(a, b)
{
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
