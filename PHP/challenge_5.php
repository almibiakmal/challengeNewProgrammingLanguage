<?php
/*
Output: 
1 2 3 4 5 6
2 4 6 8 10
7 8 9 10
12 14 16
11 12
18

 */
echo"Lebar: ";
$lebar = trim(fgets(STDIN));

$baris = 1;
$pointerGanjil = 1;
$pointerGenap = 1;

while($lebar >= 1){

    $temp = 0;
    if($baris % 2 == 0){
        //baris genap
        $logPrint = 0;
        for($l = $pointerGenap; $l <= $l; $l++){

            if($l % 2 == 0){
                echo $l." ";
                $logPrint++;

                if($logPrint == $lebar){
                    break;
                }
            }
            
            $temp = $l;
        }

        $pointerGenap = $temp;

    }else{
        //baris ganjil
        for($l = $pointerGanjil; $l <= $lebar; $l++){
            echo $l." ";
            $temp = $l;
        }

        $pointerGanjil = $temp;
    }

    echo"\n";

    $baris++;
    $lebar--;
}


?>