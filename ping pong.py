from pygame import*


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))


display.set_caption("ping pong")
background = transform.scale(image.load("u.jpg"), (win_width, win_height))

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
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width-190:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width-190:
            self.rect.y += self.speed
            

        

clock = time.Clock()
FPS = 60
run = True
rac1 =Player('t.jpg',0,300,10,30,100)
rac2 =Player('t.jpg',630,300,10,30,100)
ball = GameSprite("dizlajk-64x64.png", 350, 250, 8, 55, 55)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(background,(0,0))
    ball.reset()
    rac1.update_l()
    rac1.reset()
    rac2.update_r()
    rac2.reset()
    display.update()
    time.delay(50)