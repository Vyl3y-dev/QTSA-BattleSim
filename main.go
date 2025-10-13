package main

import (
	"fmt"

	basechar "QTSA-BattleSim/baseChar"
)

func main() {

	fmt.Println("Hello! Yoan :)")

	fmt.Println("\nPlayer Stats")
	baseCharacterStats := basechar.BaseCharacterBuild()
	fmt.Printf("Wellbeing: %v\nDrive: %v\nForce: %v\nDefense: %v\nAccuracy: %v\nEvasion: %v\nBreakthrough: %v\nSpeed: %v\nMorale: %v\nStability: %v\n", baseCharacterStats.Wellbeing, baseCharacterStats.Drive, baseCharacterStats.Force, baseCharacterStats.Defense, baseCharacterStats.Accuracy, baseCharacterStats.Evasion, baseCharacterStats.Breakthrough, baseCharacterStats.Speed, baseCharacterStats.Morale, baseCharacterStats.Stability)

	// Next make it so character stays default
	// Add way to generate baseCharacterStats and enemyStats separately from ChracterStats
	// start on battle elements
}
