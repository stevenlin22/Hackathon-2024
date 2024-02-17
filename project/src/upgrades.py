class Upgrades:
    def __init__(self):
        """initializes upgrades where multiplier is the multiplier and the increase rate is the rate at which the score increases
        """
        # Matt: shouldn't we take in multiplier and increaserate as args so we can change it on a case-by-case basis?
        self.multiplier = 1
        self.increaseRate = 1

    def scoreIncrease(self, score):
        """Run inside the event loop on click. Increases the score based on multiplier

        Args:
            score (): the current score

        Returns:
            score: the new score
        """
        self.increaseRate *= self.multiplier
        score += self.increaseRate
        return score