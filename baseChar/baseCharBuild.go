package basechar

func BaseCharacterBuild() BaseBeing {
	baseCharacterStats := BaseCharacterStats{
		Academics:    5,
		Charisma:     5,
		Creativity:   5,
		Endurance:    5,
		Insight:      5,
		Willpower:    5,
		Confidence:   5,
		Focus:        5,
		Adaptability: 5,
	}

	return BaseBeingStats(baseCharacterStats)
}
