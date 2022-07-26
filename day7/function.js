// 함수는 입력을 받고 특정한 기능이나 계산을 수행 후 결과를 되돌려 줄 수 있다.
//함수를 호출한다. -> 함수가 기능을 하고 반환

/*function 함수 이름 (인자1, 인자2){
	
	실행할 코드
	
	return 결과값;
}*/

function return_test(){
	return;
	console.log("실행되지 않는 코드");
}

function print(message){
	console.log("print function in");
	console.log(message);
	console.log("print function out");
}

function sum(arg1, arg2){
	var result = arg1 + arg2;
	return result;
}

