from pygame import *
import pygame
import time
import random

#Main Window Code
init() #Initialize pygame
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
icon = pygame.image.load('misc/assets/snakie.png')
pygame.display.set_icon(icon)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
field = 'misc/assets/field.png'
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
Background = Background(field, [0, 0])
 

 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 35)
def Your_score(score):
    # value = score_font.render("Your Score: " + str(score), True, yellow)
    # screen.blit(value, [0, 0])
    high = open('misc/highscore.txt', 'r')

 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 9, screen_height / 9])


 
def drawGrid():
    snake_block = 10 #Set the size of the grid block
    for x in range(0, screen_width, snake_block):
        for y in range(0, screen_height, snake_block):
            rect = pygame.Rect(x*snake_block, y*snake_block, snake_block, snake_block)
            pygame.draw.rect(screen, white, rect, 10)



def gameLoop():
    game_over = False
    game_close = False
 
    x1 = screen_width / 2
    y1 = screen_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
        while game_close == True:
            screen.fill(blue)
            screen.blit(Background.image, Background.rect) 
            message("You Lost! Press C to Play Again or Q to Quit",red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        screen.blit(Background.image, Background.rect)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        # for x in snake_List[:-1]:
        #     if x == snake_Head:
        #         game_close = True
        
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        # def Highscore():
        score = Length_of_snake - 1
        f = open('misc/highscore.txt', 'r')
        highscore = int(f.readline())
        if highscore < score:
               highscore = open('misc/highscore.txt', 'w')
               highscore.write(str(score))
               highscore.close()
        f.close()
        title = display.set_caption("Snakie | Score: "+str(score)+ " | Highscore: " + str(highscore)) #Set window title
        print(score, highscore)
        display.update()
        # Highscore()
        pygame.display.update()

        clock.tick(snake_speed)
        drawGrid()
    pygame.quit()
    quit()
drawGrid()
gameLoop()