# Matt: Following what I learned in CS110, we should be following MVC (model, view, controller).
# In this case the models are the structure of the game (sprites, buttons, etc.), the view is pygame, and the controller is this file which initializes and works with the two.

# import necessary files and modules
import pygame
import json
from src.upgrades import Upgrades
from src.items import Item
from src.buttons import Button
from src.music import Sound

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
        self.sound = Sound()

        self.data = {
            "score": 0,
            "upgrade_price": 0,
            "multiplier": 0,
            "items": {
                "gear": 0,
                "wd40": 0,
                "cpu": 0,
                "thingy": 0,
                "wires": 0,
                "sheets": 0
            },
            "item_rate": 0,
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
        running = True
        while running == True:
            if self.state == "MAIN":
                self.mainloop()
            elif self.state == "END":
                self.endloop()
            elif self.state == "STOP":
                running = False




    # mainloop is the main game (not the start, or end, etc.)
    def mainloop(self):

        score = self.data["score"]
        upgrade_price = self.data["upgrade_price"]
        multiplier = 25
        parts = [1000, 2500, 10000, 50000, 100000, 1000000]
        parts_text = ['(z)Left Leg(1000)','(x)Right Leg (2500)', '(c)Body(10K)','(v)Right Arm(50K)','(b)Left Arm(100K)','(n)Head(1M)']
        items = [100, 750, 3000, 20000, 111111, 500000]
        item_text = ['(1) Gear (100) +1/s','(2) WD40 (750) +5/s','(3) CPU (3000) +25/s','(4) Thingy (20K) +200/s','(5) New Wires (111K) +1K/s','(6)Gold (500K) +4.5k/s']
        item_rate = self.data["item_rate"]
        self.sound.play_music()
        
        while self.state == "MAIN":
            # timer.tick(framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open("data.txt", "w") as f:
                        json.dump(self.data, f)
                    self.state = "STOP"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        #Clicker part
                        self.sound.tap_sound()
                        score = self.score_increase.scoreIncrease(score, multiplier)
                        self.data["score"] = score
                        
                    if event.key == pygame.K_LSHIFT:
                        #upgrades
                        if score >= upgrade_price:
                            self.sound.upgrade_sound()
                            score -= upgrade_price
                            multiplier = self.score_increase.multiplier(multiplier)
                            self.data["multiplier"] = multiplier
                            upgrade_price = 25 * multiplier
                            self.data["upgrade_price"] = upgrade_price
                    if event.key == pygame.K_z: # add score requirement for below
                        if score >= parts[0] and self.data["robot"]["leg1"] is False:
                            self.sound.part_sound()
                            score -= parts[0]
                            self.data["robot"]["leg1"] = True
                    if event.key == pygame.K_x:
                        if score >= parts[1] and self.data["robot"]["leg2"] is False:
                            self.sound.part_sound()
                            score -= parts[1]
                            self.data["robot"]["leg2"] = True
                    if event.key == pygame.K_c:
                        if score >= parts[2] and self.data["robot"]["body"] is False:
                            self.sound.part_sound()
                            score -= parts[2]
                            self.data["robot"]["body"] = True
                    if event.key == pygame.K_v:
                        if score >= parts[3] and self.data["robot"]["arm1"] is False:
                            self.sound.part_sound()
                            score -= parts[3]
                            self.data["robot"]["arm1"] = True
                    if event.key == pygame.K_b:
                        if score >= parts[4] and self.data["robot"]["arm2"] is False:
                            self.sound.part_sound()
                            score -= parts[4]
                            self.data["robot"]["arm2"] = True
                    if event.key == pygame.K_n:
                        if score >= parts[5] and self.data["robot"]["head"] is False:
                            self.sound.part_sound()
                            score -= parts[5]
                            self.data["robot"]["head"] = True

                    # Item buys (code rlly repetitive lolo)
                    if event.key == pygame.K_1:
                        if score >= items[0]:
                            self.sound.upgrade_sound()
                            score -= items[0]
                            item_rate += self.items.item_type(1)
                            self.data["item_rate"] += item_rate
                    if event.key == pygame.K_2:
                        if score >= items[1]:
                            self.sound.upgrade_sound()
                            score -= items[1]
                            item_rate += self.items.item_type(2)
                            self.data["item_rate"] += item_rate
                    if event.key == pygame.K_3:
                        if score >= items[2]:
                            self.sound.upgrade_sound()
                            score -= items[2]
                            item_rate += self.items.item_type(3)
                            self.data["item_rate"] += item_rate
                    if event.key == pygame.K_4:
                        if score >= items[3]:
                            self.sound.upgrade_sound()
                            score -= items[3]
                            item_rate += self.items.item_type(4)
                            self.data["item_rate"] += item_rate
                    if event.key == pygame.K_5:
                        if score >= items[4]:
                            self.sound.upgrade_sound()
                            score -= items[4]
                            item_rate += self.items.item_type(5)
                            self.data["item_rate"] += item_rate
                    if event.key == pygame.K_6:
                        if score >= items[5]:
                            self.sound.upgrade_sound()
                            score -= items[5]
                            item_rate += self.items.item_type(6)
                            self.data["item_rate"] += item_rate
                    if event.key == pygame.K_m:
                        self.sound.mute_key()

                    if event.key == pygame.K_RETURN:
                        if self.data["robot"]["head"]:
                            self.state = "END"
                            running = False

            score = self.items.update(score, item_rate)
            # print(score)
            
            # Display BG
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
        
            if self.data["robot"]["leg1"]:
                img = pygame.transform.scale(pygame.image.load("project/assets/leg1.png"), (250,250))
                self.screen.blit(img, (130, 180))
            if self.data["robot"]["leg2"]:
                img = pygame.transform.scale(pygame.image.load("project/assets/leg2.png"), (250,250))
                self.screen.blit(img, (130, 180))
            if self.data["robot"]["body"]:
                img = pygame.transform.scale(pygame.image.load("project/assets/body.png"), (250,250))
                self.screen.blit(img, (130, 180))
            if self.data["robot"]["arm1"]:
                img = pygame.transform.scale(pygame.image.load("project/assets/arm1.png"), (250,250))
                self.screen.blit(img, (130, 180))
            if self.data["robot"]["arm2"]:
                img = pygame.transform.scale(pygame.image.load("project/assets/arm2.png"), (250,250))
                self.screen.blit(img, (130, 180))
            if self.data["robot"]["head"]:
                img = pygame.transform.scale(pygame.image.load("project/assets/head.png"), (250,250))
                self.screen.blit(img, (130, 180))
                endprompt = Button(360, 210, 240, 120, self.screen, -1, font, "Press enter to end.", 24, "white")
                endprompt.draw(0)


            fontsize = 20

            # Draw score and multiplier
            current_score = "Score (space): {}".format(score)
            scorebutton = Button(10, 440, 200, 90, self.screen, -1, font, current_score, fontsize)
            scorebutton.draw(0)

            current_multiplier = "Multiplier (shift): {}".format(multiplier)
            multbutton = Button(265, 440, 200, 90, self.screen, -1, font, current_multiplier, fontsize)
            multbutton.draw(0)
            multcostfont = pygame.font.Font(font, 12)
            multcosttext = multcostfont.render(f"Cost: {upgrade_price}", True, "black")
            multcosttextRect = multcosttext.get_rect()
            multcosttextRect.center = (multbutton.rect.centerx, multbutton.rect.centery + 15)
            self.screen.blit(multcosttext, multcosttextRect)
            
            # Display everything
            
            pygame.display.flip()



    

    def endloop(self):
        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "STOP"
            self.screen.fill("black")
            pygame.display.flip()
        pass
        #TODO: Spawn robot
        #TODO: Put robot in field of flowers
        #TODO: Let player move robot around in field

    def saveload(self):
        try:
            with open("data.txt") as f:
                self.data = json.load(f)
        except:
            with open("data.txt", "w") as f:
                json.dump(self.data, f)