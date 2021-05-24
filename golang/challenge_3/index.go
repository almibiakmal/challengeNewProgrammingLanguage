package main
import
	"fmt"

func main(){
	build(6,6)
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