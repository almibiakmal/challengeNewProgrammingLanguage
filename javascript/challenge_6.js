const readlineSync = require('readline-sync')

console.log("====================================\nWelcome to Sorting Program\n====================================\n");

let angka = [];
try{
	while(true){
        let temp = readlineSync.questionInt("Enter a number : ");
		temp = int(input("Enter a number : "))
		angka.append(temp)
    }
}catch(ValueError){
    console.log("Process input stoped.");
}