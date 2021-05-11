const readlineSync = require('readline-sync')

console.log("====================================\nWelcome to Sorting Program\n====================================\n");

let angka = [];
try{
	while(true){
        let temp = readlineSync.questionInt("Enter a number : ");
		angka.push(temp)
    }
}catch(ValueError){
    console.log("Process input stoped.");
}