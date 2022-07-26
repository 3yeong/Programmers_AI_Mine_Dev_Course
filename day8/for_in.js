var obj = {
	name : "object",
	weight : 30,
	isObject:true,
	arr:[1,2,3,4],
	obj:{property:1}
};

console.log("For 구문으로 object property 반복하기");

var property_list = Object.keys(obj);
console.log("property List : ", property_list);

for(var i = 0; i < property_list.length; i++){
	var propertyName = property_list[i];
	console.log("\t", propertyName, " : ", obj[propertyName]);
}

console.log("\n\nFor in 구문으로 object property 반복하기");

for(var propertyName in obj){
	console.log("\t",propertyName," : ", obj[propertyName]);
}
