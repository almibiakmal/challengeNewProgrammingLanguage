const readlineSync = require('readline-sync')

console.log("====================================\nWelcome to Sorting Program\n====================================\n");

let angkas = [];
let jumlahGerbong = readlineSync.questionInt("Jumlah gerbong : ");

while(jumlahGerbong > 0){
    let temp = readlineSync.questionInt("Enter a number : ");
    angkas.push(temp);
    jumlahGerbong--;
}



if(angkas.length > 1){
    while(true){
        let answare = readlineSync.question("\nDo you want to start sorting (y/n) ? ");
        
        switch(answare){
            case "y":
                
                console.log(`Input : ${angkas}`);
                console.log("Processing...");

                while(true){
                    let move = 0;

                    angkas.forEach((val, index)=>{
                        let temp = 0;

                        if(val > angkas[index+1]){
                            temp = val;
                            angkas[index] = angkas[index+1];
                            angkas[index+1] = temp;
                            move++;
                        }
                    });

                    if(move === 0){
                        break;
                    }
                }

                console.log(`Output : ${angkas}`);

                break;
            case "n":
                break;
            default:
                console.log("Unknow, please try again...");
        }
        break;
    }   
}else{
    if(angkas.length === 1){
        console.log(`Input: ${angkas[0]}`);
        console.log(`Output: ${angkas[0]}`);
    }else{
        console.log("Input is empty");
    }
}

