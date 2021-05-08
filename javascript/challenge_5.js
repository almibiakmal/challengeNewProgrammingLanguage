let lebar = 6;

let nomor = 1;
let pointerGenap = 0;
let row = 1;

while (true){
	let i = lebar;
    let temp = "";
	while (true){

		if(row > 1){

			if(row % 2 === 0){
				if(pointerGenap === 0){

					if(nomor % 2 === 0){
                        temp += (nomor+" ");
						i--;
                    }

					nomor++;
					if(i === 0){
						pointerGenap = nomor;
						break;
                    }
                }else{
					if(pointerGenap % 2 === 0){
                        temp += (pointerGenap+" ");
						i--;
                    }
					pointerGenap++;

					if(i === 0){
						break;
                    }
                }
            }else if(row % 2 !== 0){
                temp += (pointerAsli+" ");
				pointerAsli++;
				i--;

				if(i === 0){
					break;
                }
            }
        }else{
            temp += (nomor+" ");
			nomor++;

			if(nomor > i){
				pointerAsli = nomor;
				nomor = 1;
				break;
            }
        }
    }

    console.log(temp);

	lebar--;
	row++;
	if(lebar === 0){
		break;
    }
}