package playground

import "fmt"

func main() {
	fmt.Print("hello")
	x := make([]string, 3)
	x[0] = "hello"
	x[1] = "me"
	x[2] = "omar"
	fmt.Print(x)
}
