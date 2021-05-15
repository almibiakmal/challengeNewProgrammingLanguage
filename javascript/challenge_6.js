const readlineSync = require('readline-sync')

console.log("====================================\nWelcome to Sorting Program\n====================================\n");

let angkas = [];

if(angkas.length > 1){
    while(true){
        let answare = readlineSync.question("Do you want to start sorting (y/n) ? ");
        
        switch(answare){
            case "y":
                let tempAngka = "";
                angkas.forEach((angka)=>{tempAngka += ", "+angka});
                console.log(`Input : ${tempAngka}`);
                console.log("Processing...");

                while(true){
                    let move = 0;

                    angkas.forEach((val, index)=>{
                        if(){
                            
                        }
                    });

                    if(move === 0){
                        break;
                    }
                }

                console.log("Success...");
                console.log(`Output : ${angkas}`);

                break;
            case "n":
                break;
            default:
                console.log("Unknow, please try again...");
        }
        
    }   
}else{
    if(angkas.length === 1){
        console.log(`Input: ${angkas[0]}`);
        console.log(`Output: ${angkas[0]}`);
    }else{
        console.log("Input is empty");
    }
}

console.log("Finish");
