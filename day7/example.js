/*
프로그램에 대한 설명
라이센스에 대한 명시
작성자에 대한 정보
*/

// var name = "홍길동"; //개발시에는 매버 사용자로부터 입력받을 필요가 없으니 정해진 변수로 동작하도록 코딩

var name = prompt("이름을 입력해주세요");

var msg = "당신의 이름은 " + name + "입니다. " + name + "님의 이름은 " + name.length + " 글자 입니다."

// console.log(msg); //개발시에는 경고창을 띄우지 말고, 콘솔에서 메세지를 화긴
alert(msg); 