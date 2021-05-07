let high = 6;
let wide = 6;

while (high > 0){
    let temp = "";
	for(let i=1; i <= wide; i++){
		temp += i+" ";
    }
	console.log(temp);
	high--;
	wide--;
}