package playground

import (
	"fmt"
	"math"
)

func add(x, y int) int {
	return x + y
}

func swap(x, y string) (string, string) {
	return y, x
}

func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func main() {
	var you, suck bool
	var i int

	a, b := swap("hello", "world")

	count := 3
	for index := 0; index < count; index++ {
		fmt.Println(index)
	}

	j, k := 1, 2

	if j > k {
		fmt.Printf("j is bigger than k %d > %d\n", j, k)
	} else {
		fmt.Printf("k is bigger than j %d > %d\n", k, j)
	}

	fmt.Println(i, you, suck)
	fmt.Println(math.Pi)
	fmt.Println(add(1, 3))
	fmt.Println(a, b)
	fmt.Println(split(10))

	defer hello()

	fmt.Println(playground.Vertex{1, 2})
}
