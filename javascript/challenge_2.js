let high = 6;
let wide = 6;

while (high > 0){
    let temp = "";
	for(let i = 0; i < wide; i++){
		temp += ((i+1)+" ");
    }
    console.log(temp);
	high--;
}