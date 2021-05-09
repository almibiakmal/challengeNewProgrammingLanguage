const readlineSync = require('readline-sync')

let lebar = readlineSync.questionInt("Lebar : ");
let limit = lebar;
let awal = false;

while (true){
    let temp = ""; 
	for(let i = 1; i <= lebar; i++){
		temp += i+" ";
    }
    console.log(temp);	

	if(!awal){
		lebar--;
    }

	if(lebar === 0){
		awal = true;
    }

	if(awal){
		if(lebar === 0){
			lebar += 2;
        }else{
			lebar++;
        }
    }

	if(lebar > limit){
		console.log("Selesai");
		break
    }
}