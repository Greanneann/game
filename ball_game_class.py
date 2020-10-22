from random import randint
import pygame
from pygame.draw import *

pygame.init()
width, length = 1200, 900
FPS = 8
pygame.font.init()

screen = pygame.display.set_mode((width, length))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class BaseTarget:
    def __init__(self, screen):
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.color = COLORS[randint(0, 5)]
        self.color2 = RED
        self.screen = screen
        self.vx = randint(1, 10)
        self.vy = randint(1, 10)

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def check_bord(self):
        if self.x >= width - 10 or self.x < 10:
            self.vx *= -1
        if self.y >= length - 10 or self.y < 10:
            self.vy *= -1


class Circle(BaseTarget):
    def __init__(self, screen):
        super().__init__(screen)
        self.R = randint(30, 100)

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.R)

    def check_event(self, pos):
        event_x, event_y = pos
        a = (self.x - event_x) ** 2
        b = (self.y - event_y) ** 2
        c = a + b
        print(c, self.R**2)
        if c <= self.R ** 2:
            return True
        return False


class Rectangle(BaseTarget):
    def __init__(self, screen):
        super().__init__(screen)
        self.width_2 = randint(30, 40)
        self.height_2 = randint(30, 80)

    def draw(self):
        rect(screen, self.color, (self.x, self.y, self.width_2, self.height_2))

    def check_event(self, pos):
        event_x, event_y = pos
        if event_x - self.x <= self.width_2 and event_y - self.y <= self.height_2:
            return True
        return False


def give_score(score):
    # print and write to file "out" score
    file = open("out.txt", "a")
    file.write('Name: ' + str(input("\n")) + ': ' + str(score) + '\n')
    file.close()
    print("Score: " + str(score))

n_1 = 10
balls = [Circle(screen) for _ in range(n_1)]
n_2 = 3
rects= [Rectangle(screen) for _ in range(n_2)]
score = 0
clock = pygame.time.Clock()
finished = False
font = pygame.font.Font(None, 50)

while not finished:
    clock.tick(FPS)
   # for ball in balls:
    #    ball.move()
     #   ball.check_bord()
      #s
    #ball.draw()
    for rect in rects:
        rect.move()
        rect.check_bord()
        rect.draw()

    pygame.display.update()
    screen.fill(BLACK)
    score_text = font.render("Score: " + str(score), True, (0, 255, 75))
    screen.blit(score_text, (100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, ball in enumerate(balls):
                result = ball.check_event(event.pos)
                if result:
                    score += 1
                    balls.pop(i)
                    balls.append(Circle(screen))

give_score(score)
pygame.quit()
