<?php
echo "Lebar: ";
$lebar = trim(fgets(STDIN));

echo "Tinggi: ";
$tinggi = trim(fgets(STDIN));

for($t = 0; $t < $tinggi; $t++){
    for($l = 1; $l <= $lebar; $l++){
        echo $l." ";
    }

    echo"\n";
}
echo"\n";
?>