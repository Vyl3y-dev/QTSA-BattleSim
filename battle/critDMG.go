package battle

import (
	basechar "QTSA-BattleSim/baseChar"
	"math/rand/v2"
)

// if crit is applied return crit chance as muliplier to attackdmg
// else return crit equals 1

func DoesItCrit(charStat basechar.BaseBeing) int {

	critStrike := charStat.Breakthrough
	chance := rand.IntN(100)

	if critStrike != 0 {

		for i := 0; i < critStrike; i++ {
			if critStrike == chance {
				return critStrike
			} else {
				continue
			}
		}

		return 1

	} else {
		return 1
	}

}
