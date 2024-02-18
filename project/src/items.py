import pygame

class Item:
    def __init__(self):
        pass

    def update(self, score, item_rate):
        pygame.time.wait(1000)
        score += item_rate
        return score
        
    def item_type(self,item_type):
        if item_type == 1:
            item_rate = 1
        elif item_type == 2:
            item_rate = 5
        elif item_type == 3:
            item_rate = 25
        elif item_type == 4:
            item_rate = 2000
        elif item_type == 5:
            item_rate = 1000
        elif item_type == 6:
            item_rate = 4500
        return item_rate