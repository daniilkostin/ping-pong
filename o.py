#Создай собственный Шутер!

from pygame import *
from random import randint


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))


display.set_caption("Shooter Game")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire1 = mixer.Sound('fire.ogg')
font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)


clock = time.Clock()
FPS = 60
run = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image =  transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed
    def fire(self):
        bull  = Bullet ('bullet.png',self.rect.centerx, self.rect.top, -10,10,30)
        bullets.add(bull)
lost = 0
score=0
class Enemy (GameSprite):
    def update (self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint (80,win_width -80)
            self.rect.y = 0
            lost = lost + 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


ship = Player('rocket.png', 5, win_height - 100, 10, 65, 65)


monsters = sprite.Group()
for i in range (1,6):
    monster = Enemy ('ufo.png',randint(80,win_width -80), -40,randint(1,5),90,65)
    monsters.add(monster)
bullets = sprite.Group()
asteroids = sprite.Group()
for i in range (1,3):
    asteroid = Enemy ('asteroid.png',randint(80,win_width -80), -40,randint(1,5),90,65)
    asteroids.add(asteroid)
health = 3
font.init()
font1 = font.SysFont('Arial',36)
font2 = font.SysFont('Arial',36)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
                fire1.play()
    if not finish:
        window.blit(background,(0,0))
        ship.update()
        text = font2.render('Счет:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        text_health = font2.render('Жизни:' + str(health), 1, (255, 255, 255))
        window.blit(text_health, (10, 80))
        ship.reset()


        sprite_list = sprite.groupcollide(monsters, bullets, True, True)
        for c in sprite_list:
            score+=1
            monster = Enemy ('ufo.png',randint(80,win_width -80), -40,randint(1,5),90,65)
            monsters.add(monster)
        if sprite.spritecollide(ship, monsters, False) or lost >= 3:
            finish = True
            window.blit(lose, (200, 200))
        if score>=10:
            finish = True
            window.blit(win, (200,200))
        if sprite.spritecollide(ship, asteroids, False):
            health -=1
            sprite.spritecollide(ship, asteroids, True)
        if health == 0:
            finish = True
            window.blit(lose, (200, 200))


        
        
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        asteroids.draw(window)
        asteroids.update()
        
        display.update()
 
    clock.tick(FPS)