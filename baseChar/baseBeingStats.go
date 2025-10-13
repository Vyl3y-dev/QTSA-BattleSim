package basechar

type BaseBeing struct {
	Wellbeing    int
	Drive        int
	Force        int
	Defense      int
	Accuracy     int
	Evasion      int
	Breakthrough int
	Speed        int
	Morale       int
	Stability    int
}

func BaseBeingStats(charStat BaseCharacterStats) BaseBeing {
	wellbeing := charStat.Endurance + charStat.Insight + charStat.Willpower + charStat.Confidence + charStat.Focus
	drive := charStat.Academics + charStat.Charisma + charStat.Creativity
	force := charStat.Willpower + charStat.Confidence + charStat.Focus
	defense := charStat.Endurance
	accuracy := charStat.Adaptability
	evasion := charStat.Insight
	breakthrough := (charStat.Academics + charStat.Focus) / 2
	speed := 2
	morale := charStat.Charisma + charStat.Confidence + charStat.Focus
	stability := charStat.Endurance + charStat.Willpower + charStat.Focus

	return BaseBeing{
		Wellbeing: wellbeing, Drive: drive, Force: force,
		Defense: defense, Accuracy: accuracy, Evasion: evasion,
		Breakthrough: breakthrough, Speed: speed, Morale: morale, Stability: stability,
	}
}
