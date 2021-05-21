<?php
echo "Lebar: ";
$lebar = trim(fgets(STDIN));

while($lebar >= 1){
    for($l = 1; $l <= $lebar; $l++){
        echo $l." ";
    }

    echo"\n";
    $lebar--;
}
?>