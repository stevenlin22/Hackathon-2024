class Upgrades:
    def __init__(self):
        """initializes upgrades where multiplier is the multiplier and the increase rate is the rate at which the score increases
        """
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