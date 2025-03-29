import pygame
import button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption ("Main Menu")
#game variables
game_paused = False

font = pygame.font.SysFont("Consolas",50 )

TEXT_COL = (255, 255, 255)


#load button images
continue_img = pygame.image.load("R.png").convert_alpha()
#create button instances
continue_button = button.Button(304, 125, continue_img,1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:

    screen.fill((60, 80, 90))

    if game_paused:
       if continue_button.draw(screen):
           game_paused = False
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False



    pygame.display.update()

pygame.quit()