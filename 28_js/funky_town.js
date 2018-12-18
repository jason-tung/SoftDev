var fibonacci = (args) =>{
  if (args < 0){
      return 0;
  };
  if (args < 2){
      return args;
  }
  return fibonacci(args - 1) * args;
};

var gcd = (a,b)=> {
    if (b == 0){
        return a;
    };
    if (a < b){
        return gcd(b,a);
    };
    return (a-b,b);
};

var randomStudent = (list) =>{
  return list[Math.floor(Math.random()*list.length)];
};