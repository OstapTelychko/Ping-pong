from random import randint
from time import sleep
import threading
import pygame
timer = 1
class Player():
    def __init__(self,x,y,width,height,speed) -> None:
        self.Rect = pygame.rect.Rect(x,y,width,height)
        self.speed = speed
    def move(self):
        keys=pygame.key.get_pressed()
        if self is player1:
            if keys[pygame.K_w] and self.Rect.y >0:
                self.Rect.y -= self.speed
            if keys[pygame.K_s] and self.Rect.y < 400:
                self.Rect.y += self.speed
        else:
            if keys[pygame.K_UP] and self.Rect.y >0:
                self.Rect.y -= self.speed
            if keys[pygame.K_DOWN] and self.Rect.y < 400:
                self.Rect.y += self.speed
    def draw(self):
        if self is player1:
            pygame.draw.rect(display,(0,255,00),self.Rect)
        else:
            pygame.draw.rect(display,(255,0,0),self.Rect)
class Ball():
    def __init__(self,x,y,radius,speed) -> None:
        self.Rect = pygame.rect.Rect(x,y,radius,radius)
        self.speed = speed
        self.radius = radius
        self.rotate_degrees = randint(0,360)
        self.move_mode = None
        self.y_change_per_step = 0
        self.x_change_per_step = 0
    def move(self):
        global player2_score,player1_score
        if self.move_mode == 1 or self.move_mode == 2:
            self.Rect.x -= self.x_change_per_step
            self.Rect.y -= self.y_change_per_step
        if self.move_mode == 3 or self.move_mode == 4:
            self.Rect.x += self.x_change_per_step
            self.Rect.y -= self.y_change_per_step
            # print(self.y_change_per_step)
        if self.move_mode == 5 or self.move_mode == 6:
            self.Rect.x  += self.x_change_per_step
            self.Rect.y += self.y_change_per_step
        if self.move_mode == 7 or self.move_mode == 8:
            self.Rect.x -= self.x_change_per_step
            self.Rect.y += self.y_change_per_step
        if self.move_mode == 9:
            self.Rect.x -= self.x_change_per_step
        if self.move_mode == 10:
            self.Rect.x -= self.x_change_per_step
            self.Rect.y -= self.y_change_per_step
        if self.move_mode == 11:
            self.Rect.y -= self.y_change_per_step
        if self.move_mode == 12:
            self.Rect.x += self.x_change_per_step
            self.Rect.y -= self.y_change_per_step
        if self.move_mode == 13:
            self.Rect.x += self.x_change_per_step
        if self.move_mode == 14:
            self.Rect.x += self.x_change_per_step
            self.Rect.y += self.y_change_per_step
        if self.move_mode == 15:
            self.Rect.y -= self.y_change_per_step
        if self.move_mode == 16:
            self.Rect.x -= self.x_change_per_step
            self.Rect.y += self.y_change_per_step
        if self.Rect.colliderect(player1.Rect):
            if self.Rect.y < 250:
                self.rotate_degrees = randint(180,225)
            else:
                self.rotate_degrees = randint(135,179)
            self.create_route()
        if self.Rect.colliderect(player2.Rect):
            if self.Rect.y > 250:
                self.rotate_degrees = randint(0,44) 
            else:
                self.rotate_degrees = randint(316,360)
            self.create_route()
        if self.Rect.x > 350 and self.Rect.y >= 490 and self.Rect.x < 700:
            self.Rect.y -= 10
            self.rotate_degrees = randint(181,200)
            self.create_route()
            self.move_mode = 12
        if self.Rect.x <= 350 and self.Rect.y >= 490 and self.Rect.x > 0:
            self.Rect.y -= 10
            self.rotate_degrees = randint(320,359)
            self.create_route()
            self.move_mode = 10
        if self.Rect.x <= 350 and self.Rect.y <= 0 and self.Rect.x > 0:
            self.Rect.y += 10
            self.rotate_degrees = randint(1,35)
            self.create_route()
            self.move_mode = 7
        if self.Rect.x > 350 and self.Rect.y <=0 and self.Rect.x < 700:
            self.Rect.y += 10
            self.rotate_degrees = randint(160,179)
            self.create_route()
            self.move_mode = 5
        if self.Rect.x >=700:
            player1_score += 1
            self.rotate_degrees = randint(0,360)
            self.Rect.x = 350
            self.Rect.y = 250
            self.create_route()
        if self.Rect.x <=0:
            player2_score += 1
            self.rotate_degrees = randint(0,360)
            self.Rect.x = 350
            self.Rect.y = 250
            self.create_route()
        # sleep(0.1)
        # print(f"x:{self.Rect.x}, y:{self.Rect.y}")
    def create_route(self):
        if 0 < self.rotate_degrees < 45:
            point_x = 0
            point_y = 250-250/45*self.rotate_degrees
            self.move_mode = 1
        elif 45 < self.rotate_degrees < 90:
            point_x = 350/45*(45-(90-self.rotate_degrees))
            point_y = 0
            self.move_mode = 2
        elif 90 < self.rotate_degrees < 135:
            point_x =  350/45*(45-(135-self.rotate_degrees))+350
            point_y = 0
            self.move_mode = 3 
        elif 135 < self.rotate_degrees < 180:
            point_x = 700
            point_y = 250/45*(45-(180-self.rotate_degrees))
            self.move_mode = 4
        elif 180 < self.rotate_degrees < 225:
            point_x = 700
            point_y = 250/45*(45-(225-self.rotate_degrees))+250
            self.move_mode = 5
        elif 225 < self.rotate_degrees < 270:
            point_x = 350/45*(45-(270-self.rotate_degrees))+350
            point_y = 500
            self.move_mode = 6
        elif 270 < self.rotate_degrees < 315:
            point_x = 350/45*(45-(315-self.rotate_degrees))
            point_y = 500
            self.move_mode = 7
        elif 315 < self.rotate_degrees < 360:
            point_x = 0
            point_y = 250/45*(45-(360-self.rotate_degrees))+250
            self.move_mode = 8
        elif self.rotate_degrees == 0 or self.rotate_degrees == 360:
            point_x = 0
            point_y = 250
            self.move_mode = 9
        elif self.rotate_degrees == 45:
            point_x = 0
            point_y = 0
            self.move_mode = 10
        elif self.rotate_degrees == 90:
            point_x = 350
            point_y = 250
            self.move_mode = 11
        elif self.rotate_degrees == 135:
            point_x = 700
            point_y = 0
            self.move_mode = 12
        elif self.rotate_degrees == 180:
            point_x = 700
            point_y = 250
            self.move_mode = 13
        elif self.rotate_degrees == 225:
            point_x = 700
            point_y = 500
            self.move_mode = 14
        elif self.rotate_degrees == 270:
            point_x = 350
            point_y = 500
            self.move_mode = 15 
        elif self.rotate_degrees == 315:
            point_x = 0
            point_y = 500
            self.move_mode = 16
        vector_length = ((point_x-self.Rect.x)**2+(point_y-self.Rect.y)**2)**0.5
        step_amount = vector_length/self.speed
        self.y_change_per_step = abs((self.Rect.y - point_y)/step_amount)
        self.x_change_per_step = abs((self.Rect.x - point_x)/step_amount)
        # print(f"degrees:{self.rotate_degrees}")
        # print(f"point_x:{point_x:.2f}, point_y:{point_y:.2f}")
        # print(f"x_change:{self.x_change_per_step:.2f}, y_change:{self.y_change_per_step:.2f}")
    def draw(self):
        pygame.draw.circle(display,(0,255,0),self.Rect.center,self.radius)
def timer_run():
    global timer
    while pygame.get_init():
        sleep(1)
        timer += 1

def run_game():
    global display,player1,player2,ball,player1_score,player2_score
    display = pygame.display.set_mode((700,500))
    pygame.display.set_caption("Ping Pong")
    main_loop = True
    finish = False
    player1 = Player(0,250,10,100,3)
    player1_score = 0
    player2_score = 0
    player2 = Player(690,250,10,100,3)
    FPS = pygame.time.Clock()
    ball = Ball(350,250,10,5)
    ball.create_route()
    # print(ball.rotate_degrees)
    pygame.font.init()
    player1_score_text = pygame.font.SysFont("Aeral",35,True)
    player2_score_text = pygame.font.SysFont("Aeral",35,True)
    timer_text = pygame.font.SysFont("Aeral",35,True)
    while main_loop:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                main_loop = False
                finish = True
                pygame.quit()
        if finish is True:
            if pygame.get_init() is True:
                pass
            break
        display.fill((30,30,120))
        ball.draw()
        ball.move()
        player1.move()
        player2.move()
        player1.draw()
        player2.draw()
        display.blit(timer_text.render(f"Timer: {timer}",True,(255,255,255)),(310,30))
        display.blit(player1_score_text.render(str(player1_score),True,(0,255,0)),(330,60))
        display.blit(player2_score_text.render(str(player2_score),True,(255,0,0)),(370,60))
        pygame.display.flip()
        FPS.tick(60)

if __name__ == "__main__":
    pygame.init()
    timer_thread = threading.Thread(target=timer_run)
    timer_thread.start()
    run_game()
