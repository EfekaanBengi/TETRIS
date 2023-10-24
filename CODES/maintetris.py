import pygame
import sys

from sys import exit
from random import choice

from game import *
from settings import *
from preview import *
from scoreboard import *
from timer1 import *







class Main:
	def __init__(self):

		# general 
		pygame.init()
		self.display_surface = pygame.display.set_mode((window_widht,window_height))
		self.clock = pygame.time.Clock()
		pygame.display.set_caption('TETRIS')

		# shapes
		self.next_shapes = [choice(list(Tetrominos.keys())) for shape in range(3)]

		# components
		self.game = Game(self.get_next_shape, self.update_score)
		self.score = ScoreBoard()
		self.preview = Preview()


	def update_score(self, lines, score, level):
		self.score.lines = lines
		self.score.score = score
		self.score.level = level

	def get_next_shape(self):
		next_shape = self.next_shapes.pop(0)
		self.next_shapes.append(choice(list(Tetrominos.keys())))
		return next_shape

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			# display 
			self.display_surface.fill(black)
			
			# components
			self.game.run()
			self.score.run()
			self.preview.run(self.next_shapes)

			# updating the game
			pygame.display.update()
			self.clock.tick()





# Function to draw text on the screen with the selected language
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Main menu variables
main_menu = True
options_menu = False
selected_option = 0
language = "English"  # Default language is English

# Options menu variables
options_selected = 0

while main_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if selected_option > 0:
                    selected_option -= 1
            elif event.key == pygame.K_DOWN:
                if selected_option < 2:
                    selected_option += 1
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    # Your Play logic here
                    if __name__ == '__main__':
                          main = Main()
                          main.run()
                elif selected_option == 1:
                    options_menu = True
                    main_menu = False
                elif selected_option == 2:
                    pygame.quit()	
                    sys.exit()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the main menu image
    screen.blit(main_menu_image, (WIDTH // 2 - main_menu_image.get_width() // 2, HEIGHT // 4 - main_menu_image.get_height() // 2))

    # Draw the main menu buttons in the selected language
    draw_text(text_en["Main Menu"] if language == "English" else text_tr["Main Menu"], font, (255, 255, 255), screen, WIDTH // 2, HEIGHT // 5 + main_menu_image.get_height() // 2 + 10)
    draw_text(text_en["Play"] if language == "English" else text_tr["Play"], font, (255, 0, 0) if selected_option == 0 else (255, 255, 255), screen, WIDTH // 2, HEIGHT // 2 + 5)
    draw_text(text_en["Options"] if language == "English" else text_tr["Options"], font, (255, 0, 0) if selected_option == 1 else (255, 255, 255), screen, WIDTH // 2, HEIGHT // 2 + 50)
    draw_text(text_en["Quit"] if language == "English" else text_tr["Quit"], font, (255, 0, 0) if selected_option == 2 else (255, 255, 255), screen, WIDTH // 2, HEIGHT // 2 + 100)

    # Update the display
    pygame.display.flip()

    while options_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                options_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    options_menu = False
                if event.key == pygame.K_UP:
                    if options_selected > 0:
                        options_selected -= 1
                elif event.key == pygame.K_DOWN:
                    if options_selected < 2:
                        options_selected += 1
                elif event.key == pygame.K_RETURN:
                    if options_selected == 0:
                        language = "Turkish" if language == "English" else "English"
                        last_language = language
                    elif options_selected == 1:
                        options_menu = False
                        main_menu = True  # Return to main menu

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw the options menu in the selected language
        draw_text(text_en["Options Menu"] if language == "English" else text_tr["Options Menu"], font, (255, 255, 255), screen, WIDTH // 2, HEIGHT // 4)
        draw_text(text_en["Language"] if language == "English" else text_tr["Language"], font, (255, 0, 0) if options_selected == 0 else (255, 255, 255), screen, WIDTH // 2, HEIGHT // 2)
        draw_text(text_en["Back to Main Menu"] if language == "English" else text_tr["Back to Main Menu"], font, (255, 0, 0) if options_selected == 1 else (255, 255, 255), screen, WIDTH // 2, HEIGHT // 2 + 50)

        # Update the display
        pygame.display.flip()



# Quit Pygame
pygame.quit()
sys.exit()