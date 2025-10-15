package basechar

import (
	"fmt"
	"math/rand/v2"
)

func GlobalLuck() float64 {
	badluck := 10
	goodluck := 90
	chance := rand.IntN(100)
	variance := 0.0
	goodvariance := 0.10
	badvariance := -0.10

	if badluck <= chance {
		if badluck >= 7 {
			fmt.Println("You tripped and fell, causing you to do less damage!")
		} else if badluck <= 4 {
			fmt.Println("The sunlight was a little too bright in your eyes, causing you to do less damage!")
		} else {
			fmt.Println("Oh no! You lost focus, causing you to do less damage!")
		}
		return badvariance
	} else if goodluck >= chance {
		fmt.Println("Wow! that looked super cool, it caused you to do a bit more damage!")
		return goodvariance
	} else {
		return variance
	}
}
