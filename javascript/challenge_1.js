let high = 11;
let wide = 11;

//Versi 1
console.log("Versi 1");

let i=0
while (i < high){
	let j = 0;
	let temp = "";
	while (j < wide){
		temp +=" *";
		j+=1;
    }

	console.log(temp);
	i++;
}

//Versi 2
console.log("Versi 2");

while (high > 0){
	let temp = "";
	let l = wide;
	while (l > 0){
		temp +=" *";
		l -= 1;
	}
	console.log(temp);
	high--;
}