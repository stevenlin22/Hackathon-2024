class Upgrades:
    def __init__(self, increaseRate):
        """initializes the multiplier and increase rate

        Args:
            multiplier (int): the multiplier of score
            increaseRate (int): rate at which the score increases
        """ 
        self.increaseRate = increaseRate

    def scoreIncrease(self, score, multiplier):
        """Run inside the event loop on click. Increases the score based on multiplier

        Args:
            score (): the current score

        Returns:
            score: the new score
        """
        increaseRate = self.increaseRate * multiplier
        new_score = score + increaseRate
        return new_score
    
    def multiplier(self, multiplier):
        new_multiplier = multiplier + 1
        return new_multiplier