package playground

import "fmt"

func hello() {
	fmt.Println("****Pointers*****")

	i := 10

	j := &i

	fmt.Printf("*j : %2d\n", *j)
	fmt.Printf("j  : %2p\n", j)
	fmt.Printf("i  : %2d\n", i)

	*j = 100

	fmt.Printf("*j : %2d\n", *j)
	fmt.Printf("j  : %2p\n", j)
	fmt.Printf("i  : %2d\n", i)

}
