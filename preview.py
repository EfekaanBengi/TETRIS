from settings import *
from pygame.image import load
from os import path

class Preview:
    def __init__(self):
        #general
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((sidebar_width, game_height*preview_Height_Franction - padding))
        self.rect = self.surface.get_rect(topright = (window_widht- padding, padding))

        #shapes
        self.shape_surfaces = {shape: load(path.join(f"{shape}.png")).convert_alpha() for shape in Tetrominos.keys()}

        # image pos data
        self.increment_height = self.surface.get_height() / 3

    def display_pieces(self, shapes):
        for i, shape in enumerate(shapes):
            shape_surface = self.shape_surfaces[shape]
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            rect = shape_surface.get_rect(center = (x,y))
            self.surface.blit(shape_surface, rect)


    def run(self, next_shapes):
        self.surface.fill(black)
        self.display_pieces(next_shapes)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, line_Color, self.rect, 2, 2)