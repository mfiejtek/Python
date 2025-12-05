import pygame
import random
import math
import settings

class Snowflake:
    def __init__(self):
        self.col_idx = random.randint(0, settings.NUM_COLUMNS - 1)

        self.x = self.col_idx * settings.COLUMN_WIDTH + settings.SNOWFLAKE_RADIUS
        
        self.y = -settings.SNOWFLAKE_RADIUS
        
        self.radius = settings.SNOWFLAKE_RADIUS
        self.speed = settings.SNOWFLAKE_SPEED

    def move(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, settings.SNOW_COLOR, (self.x, int(self.y)), self.radius)

    def is_clicked(self, mouse_pos):
        mx, my = mouse_pos
        distance = math.hypot(mx - self.x, my - self.y)
        return distance <= self.radius + 5