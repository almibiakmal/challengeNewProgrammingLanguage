<?php 
/*
Output: 

1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

 */
echo "Lebar: ";
$lebar = trim(fgets(STDIN));
$batas = $lebar;

while($lebar >= 1){
    for($l = 1; $l <= $lebar; $l++){
        echo $l." ";
    }

    echo"\n";
    $lebar--;
}

$lebar+=2;

while($batas > 1){
    for($l = 1; $l <= $lebar; $l++){
        echo $l." ";
    }

    echo"\n";
    $batas--;
    $lebar++;
}
?>