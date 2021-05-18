<?php
echo "Lebar: ";
$lebar = trim(fgets(STDIN));

echo "Tinggi: ";
$tinggi = trim(fgets(STDIN));

for($t = 0; $t < $tinggi; $t++){
    for($l = 0; $l < $lebar; $l++){
        echo " *";
    }

    echo "\n";
}
echo"\n";
?>