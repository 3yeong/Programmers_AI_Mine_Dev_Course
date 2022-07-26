function shadowing_example(){
	var val = 0;
	console.log("F", val);
	val ++;
}

var val = 0;

shadowing_example();
console.log("O",val);