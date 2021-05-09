const readlineSync = require('readline-sync')

let high = readlineSync.questionInt("Tinggi : ");
let wide = readlineSync.questionInt("Lebar : ");

while (high > 0){
    let temp = "";
	for(let i = 0; i < wide; i++){
		temp += ((i+1)+" ");
    }
    console.log(temp);
	high--;
}