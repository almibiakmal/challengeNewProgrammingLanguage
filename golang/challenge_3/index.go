package main
import
	"fmt"

func main(){
	lebar, tinggi := 0, 0
	fmt.Print("Tinggi: ")
	fmt.Scanln(&tinggi)

	fmt.Print("Lebar: ")
	fmt.Scanln(&lebar)

	if tinggi != 0 && lebar != 0{
		build(tinggi, lebar)	
	}
	
}

func build(tinggi, lebar int){
	for i := 0; i < tinggi; i++{
		for j := 1; j <= lebar; j++{
			fmt.Print(j)
			fmt.Print(" ")
		}
		lebar--
		fmt.Println()
	}
}