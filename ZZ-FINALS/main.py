import pygame
import sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Main Menu")

# Load and resize the background image to full screen size (1280x720)
BG = pygame.image.load("BG.png")
BG = pygame.transform.scale(BG, (1280, 720))  # Resize to screen size

def get_font(size):
    return pygame.font.Font(None, size)

def play():
    pygame.display.set_caption("Play")
    running = True

    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the Play screen", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="Back", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    running = False

        pygame.display.update()

def options():
    pygame.display.set_caption("Options")
    running = True

    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("White")

        OPTIONS_TEXT = get_font(45).render("This is the Options screen", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="Back", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    running = False

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menu")

    # Load and scale the button image
    button_image = pygame.image.load("pl.png")
    button_image = pygame.transform.scale(button_image, (400, 100))  # Adjust size here

    while True:
        SCREEN.fill((0, 0, 0))  # Clear screen behind background
        SCREEN.blit(BG, (0, 0))  # Display background scaled to fit the full screen

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("WELCOME TO THE GAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        PLAY_BUTTON = Button(image=button_image, pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="Blue", hovering_color="White")
        OPTIONS_BUTTON = Button(image=button_image, pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="Blue", hovering_color="White")
        QUIT_BUTTON = Button(image=button_image, pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="Blue", hovering_color="White")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
