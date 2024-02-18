# Matt: Following what I learned in CS110, we should be following MVC (model, view, controller).
# In this case the models are the structure of the game (sprites, buttons, etc.), the view is pygame, and the controller is this file which initializes and works with the two.

# import necessary files and modules
import pygame
import json
from src.upgrades import Upgrades
from src.items import Item
from src.buttons import Button

class Controller:
    # init
    def __init__(self):
        pygame.init()
        self.screenwidth = 960
        self.screenheight = 540
        self.screen = pygame.display.set_mode([self.screenwidth, self.screenheight])
        self.screen.fill("white")
        self.width, self.length = pygame.display.get_window_size()
        pygame.display.set_caption("HackBU clicker game")
        self.framerate = 60
        increaseRate = 1
        self.score_increase = Upgrades(increaseRate)
        self.items = Item()

        self.data = {
            "score": 0,
            "upgrades": 0,
            "items": {
                "gear": 0,
                "wd40": 0,
                "cpu": 0,
                "thingy": 0,
                "wires": 0,
                "sheets": 0
            },
            "robot": {
                "leg1": False,
                "leg2": False,
                "body": False,
                "arm1": False,
                "arm2": False,
                "head": False,
            },
            "platformer": False,
        }

        self.saveload()

        self.state = "MAIN"



    # the gameloop manages game state
    def gameloop(self):
        if self.state == "MAIN":
            self.mainloop()
        elif self.state == "PLACEHOLDER":
            self.placeholder()




    # mainloop is the main game (not the start, or end, etc.)
    def mainloop(self):

        score = self.data["score"]
        running = True
        upgrade_price = 25
        multiplier = 1
        
        parts = [1000, 2500, 10000, 50000, 100000, 1000000]
        parts_text = ['(z)Left Leg(1000)','(x)Right Leg (2500)', '(c)Body(10K)','(v)Right Arm(50K)','(b)Left Arm(100K)','(n)Head(1M)']
        
        items = [100, 750, 3000, 20000, 111111, 500000]
        item_text = ['(1) Gear (100) +1/s','(2) WD40 (750) +5/s','(3) CPU (3000) +25/s','(4) Thingy (20K) +200/s','(5) New Wires (111K) +1K/s','(6)Gold (500K) +4.5k/s']

        item_rate = 0
        while running:
            # timer.tick(framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open("data.txt", "w") as f:
                        json.dump(self.data, f)
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        #Clicker part
                        score = self.score_increase.scoreIncrease(score, multiplier)
                        self.data["score"] = score
                        print("Score: ", score)
                        print("multiplier1: ", multiplier)
                        print("Upgrade Cost: ", upgrade_price)
                    if event.key == pygame.K_LSHIFT:
                        #upgrades
                        print("run")
                        print("Score2: ", score)
                        if score >= upgrade_price:
                            score -= upgrade_price
                            multiplier = self.score_increase.multiplier(multiplier)
                            print("Multplier: ", multiplier)
                            upgrade_price = 25 * multiplier
                            print("Upgrade price: ", upgrade_price)
                        print(score)
                    if event.key == pygame.K_z: # add score requirement for below
                        if score >= parts[0] and self.data["robot"]["leg1"] is False:
                            score -= parts[0]
                            self.data["robot"]["leg1"] = True
                            self.screen.blit(img, (100, 100))
                    if event.key == pygame.K_x:
                        if score >= parts[1] and self.data["robot"]["leg2"] is False:
                            score -= parts[1]
                            self.data["robot"]["leg2"] = True
                            self.screen.blit(img, (100, 100))
                    if event.key == pygame.K_c:
                        if score >= parts[2] and self.data["robot"]["body"] is False:
                            score -= parts[2]
                            self.data["robot"]["body"] = True
                            img = pygame.image.load("project/assets/body.png")
                    if event.key == pygame.K_v:
                        if score >= parts[3] and self.data["robot"]["arm1"] is False:
                            score -= parts[3]
                            self.data["robot"]["arm1"] = True
                    if event.key == pygame.K_b:
                        if score >= parts[4] and self.data["robot"]["arm2"] is False:
                            score -= parts[4]
                            self.data["robot"]["arm2"] = True
                    if event.key == pygame.K_n:
                        if score >= parts[5] and self.data["robot"]["head"] is False:
                            score -= parts[5]
                            self.data["robot"]["head"] = True
                    if event.key == pygame.K_1:
                        if score >= items[0]:
                            score -= items[0]
                            item_rate += self.items.item_type(1)
                    if event.key == pygame.K_2:
                        if score >= items[1]:
                            score -= items[1]
                            item_rate += self.items.item_type(2)
                    if event.key == pygame.K_3:
                        if score >= items[2]:
                            score -= items[2]
                            item_rate += self.items.item_type(3)
                    if event.key == pygame.K_4:
                        if score >= items[3]:
                            score -= items[3]
                            item_rate += self.items.item_type(4)
                    if event.key == pygame.K_5:
                        if score >= items[4]:
                            score -= items[4]
                            item_rate += self.items.item_type(5)
                    if event.key == pygame.K_6:
                        if score >= items[5]:
                            score -= items[5]
                            item_rate += self.items.item_type(6)
            score = self.items.update(score, item_rate)
            print(score)

            #TODO: display everything
            left = pygame.image.load('project/assets/Background.png')
            left = pygame.transform.scale(left, ((self.screenwidth / 2) - 5, self.screenheight))
            self.screen.blit(left, (0,0))

            right = pygame.image.load('project/assets/RBackground.jpg')
            right = pygame.transform.scale(right, ((self.screenwidth / 2) - 5, self.screenheight))
            self.screen.blit(right, ((self.screenwidth / 2) + 5, 0))

            pygame.draw.rect(self.screen, "black", pygame.Rect(475, 0, 10, 540))

            font = 'freesansbold.ttf'
            fontsize = 20

            buttonwidth = 180
            buttonheight = 70

            xpos = 525
            ypos = 10

            for j in range(6):
                button = Button(xpos, ypos, buttonwidth, buttonheight, self.screen, parts[j], font, parts_text[j], fontsize)
                button.draw(score)
                ypos += 90
            
            xpos += 215
            fontsize -= 6
            ypos = 10

            for j in range(6):
                button = Button(xpos, ypos, buttonwidth, buttonheight, self.screen, items[j], font, item_text[j], fontsize)
                button.draw(score)
                ypos += 90
        
            if self.data["robot"]["leg1"] is True:
                img = pygame.transform.scale(pygame.image.load("project/assets/leg1.png"), (250,250))
                self.screen.blit(img, (130, 180))
            if self.data["robot"]["leg2"] is True:
                img = pygame.transform.scale(pygame.image.load("project/assets/leg2.png"), (250,250))
                self.screen.blit(img, (130, 180))
            if self.data["robot"]["body"] is True:
                img = pygame.transform.scale(pygame.image.load("project/assets/body.png"), (250,250))
                self.screen.blit(img, (130, 180))
            if self.data["robot"]["arm1"] is True:
                img = pygame.transform.scale(pygame.image.load("project/assets/arm1.png"), (250,250))
                self.screen.blit(img, (130, 180))
            if self.data["robot"]["arm2"] is True:
                img = pygame.transform.scale(pygame.image.load("project/assets/arm2.png"), (250,250))
                self.screen.blit(img, (130, 180))
            if self.data["robot"]["head"] is True:
                img = pygame.transform.scale(pygame.image.load("project/assets/head.png"), (250,250))
                self.screen.blit(img, (130, 180))
            pygame.display.flip()
        pygame.quit()

    

    def placeholder(self):
        # some things that could be other states:
        # credits
        # end scene that plays when the robot is done
        # etc.
        pass

    def saveload(self):
        try:
            with open("data.txt") as f:
                self.data = json.load(f)
        except:
            with open("data.txt", "w") as f:
                json.dump(self.data, f)