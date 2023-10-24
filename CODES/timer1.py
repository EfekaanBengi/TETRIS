import pygame

class Timer:
    def __init__(self, duration, repeated = False, func = None):
        self.repeated = repeated
        self. func = func
        self.duration = duration

        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()
    
    def diactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration and self.active:
            
            #call a function
            if self.func and self.start_time != 0:
                self.func()

            # reset timer
            self.diactivate()

            #repeat timer
            if self.repeated:
                self.activate()
