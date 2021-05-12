package main
import
	"fmt"

func main(){
	high := 6
	wide := 6

	for high > 0{
		for i := 1; i <= wide; i++{
			fmt.Print(i, " ")
		}
		
		fmt.Println("")
		high--
	}
}

