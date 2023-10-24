import pygame

# Game Size
columns = 10
rows= 20
cell_Size = 35

game_width, game_height = columns*cell_Size, rows*cell_Size

# Side Bar Size

sidebar_width = 200
preview_Height_Franction = 0.7
score_height_franction = 1 - preview_Height_Franction

# window

padding = 20
window_widht = game_width + sidebar_width + padding * 3
window_height = game_height + padding *2

# game behavior

update_start_speed = 350
move_wait_time = 200
rotate_Wait_Time = 200
block_offset = pygame.Vector2(columns // 2 , -1)

# colors
yellow = '#FFFD6F'
red = '#fd7878'
blue = '#677EFD'
green = '#88ff92'
purple = '#c485ff'
cyan = '#9dfeff'
orange = '#ffbc79'
black = '#313131'
line_Color = '#FFFFFF'

# shapes

Tetrominos = {
    'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': purple},
    'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': yellow},
    'J': {'shape': [(0,0), (0,-1), (0,1), (-1,-1)], 'color': blue},
    'L': {'shape': [(0,0), (0,-1), (0,1), (1,-1)], 'color': orange},
    'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': cyan},
    'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': green},
    'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': red}
}

score_Data = {1: 40, 2: 100, 3:300, 4: 400}

# Initialize Pygame
pygame.init()


# Constants
WIDTH, HEIGHT = window_widht, window_height
BACKGROUND_COLOR = (black)  # RGB color for #313131

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TETRIS")


font = pygame.font.Font('Russo_One.ttf', 30)


main_menu_image = pygame.image.load('TETRİSSSS.png')

# Define English and Turkish text dictionaries
text_en = {
    "Main Menu": "Main Menu",
    "Play": "Play",
    "Options": "Options",
    "Quit": "Quit",
    "Back to Main Menu": "Back to Main Menu",
    "English": "English",
    "Turkish": "Turkish",
    "Options Menu": "Options Menu",
    "Language": "Language",
	"Score": "Score"
}

text_tr = {
    "Main Menu": "Ana Menü",
    "Play": "Oyna",
    "Options": "Ayarlar",
    "Quit": "Çıkış",
    "Back to Main Menu": "Ana Menü'ye Dön",
    "English": "İngilizce",
    "Turkish": "Türkçe",
    "Options Menu": "Ayarlar Menüsü",
    "Language": "Dil",
	"Score": "Skor"
}
