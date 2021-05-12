package main
import "fmt"

func main(){
	var high int
	var wide int

	fmt.Print("Tinggi : ")
    fmt.Scanf("%d", &high)

	fmt.Print("Lebar : ")
    fmt.Scanf("%d", &wide)

	for high > 0{
		for i := 1; i <= wide; i++{
			fmt.Print(i, " ")
		}

		fmt.Println("")
		high--
	}
}

