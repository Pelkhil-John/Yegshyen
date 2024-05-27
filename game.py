import pygame
import random
import math


WIDTH, HEIGHT = 1360,700
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 40
MAX_VEL = 10
pygame.init()
FONT = pygame.font.SysFont("times new roman", 100)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("☭☭☭☭☭")
entities = []
score = 0 
he_disconnected = pygame.mixer.music.load('CodingClub\John_Caudill\sound\he_disconnected.mp3') 

class Entity:

    x, y = 0, 0
    on_screen = True
    rect = pygame.Rect(x,y,x,y)
    color ="blue"

    def __init__(self, x=random.random()*WIDTH, y=random.random()*HEIGHT, width=PLAYER_WIDTH, height=PLAYER_HEIGHT):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.set_color((random.random()*255,random.random()*255, random.random()*255))

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def set_color(self, color):
        self.color = color




def find_collisions(player):
    global score
    for ent in entities:
        if player.colliderect(ent):
            score += 1
            pygame.mixer.music.play()
            entities.remove(ent)


def draw(player):
    # WIN.blit()
    WIN.fill((0, 0, 0))
    for ent in entities:
        pygame.draw.rect(WIN, ent.color, ent.rect)
    WIN.blit(FONT.render(str(score), False, ((136, 8, 8))), (0,0))
    pygame.display.update()


def is_on_screen(ent):
    if ent.rect.right < 0 or ent.rect.left > WIDTH or ent.rect.bottom < 0 or ent.rect.top > HEIGHT:
        ent.on_screen = False
    return ent.on_screen


def rolling_add(ent):
    if not is_on_screen(ent):
        if ent.rect.right < 0:
            entities.append(Entity(WIDTH, random.random()*HEIGHT))
        elif ent.rect.left > WIDTH:
            entities.append(Entity(0-PLAYER_WIDTH, random.random()*HEIGHT))
        elif ent.rect.bottom < 0:
            entities.append(Entity(random.random()*WIDTH, HEIGHT))
        elif ent.rect.top > HEIGHT:
            entities.append(Entity(random.random()*WIDTH, 0-PLAYER_HEIGHT))


def update_position(vel_x, vel_y):
    for ent in entities:
        ent.x -= vel_x
        ent.y -= vel_y
        ent.update()
        if ent.on_screen:
            rolling_add(ent)


def main():
    player = pygame.Rect(WIDTH/2 - PLAYER_WIDTH/2, HEIGHT/2 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
    for x in range(10):
        entities.append(Entity(random.random()*WIDTH, random.random()*HEIGHT))
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit(0)
 
        keys = pygame.key.get_pressed()
        vel_x, vel_y = 0, 0
        if keys[pygame.K_a]:
            vel_x -= MAX_VEL
        if keys[pygame.K_d]:
            vel_x += MAX_VEL
        if keys[pygame.K_s]:
            vel_y += MAX_VEL
        if keys[pygame.K_w]:
            vel_y -= MAX_VEL
        if math.sqrt(math.pow(vel_x, 2) + math.pow(vel_y, 2)) > MAX_VEL:
            vel_x, vel_y = vel_x/math.sqrt(2), vel_y/math.sqrt(2)
        update_position(vel_x, vel_y)
        find_collisions(player)
        draw(player)


if __name__ == "__main__":
    main()
    

