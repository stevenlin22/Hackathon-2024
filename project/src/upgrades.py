class Upgrades:
    def __init__(self, multiplier, increaseRate):
        """initializes the multiplier and increase rate

        Args:
            multiplier (int): the multiplier of score
            increaseRate (int): rate at which the score increases
        """ 
        self.multiplier = multiplier
        self.increaseRate = increaseRate

    def scoreIncrease(self, score):
        """Run inside the event loop on click. Increases the score based on multiplier

        Args:
            score (): the current score

        Returns:
            score: the new score
        """
        self.increaseRate *= self.multiplier
        new_score = score + self.increaseRate
        return new_score