<?php
/*
Output:

1 2 3 4 5 6
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1

 */
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