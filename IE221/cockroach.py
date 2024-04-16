import pygame
import random
import time
import image
from settings import *

class Cockroach:
    def __init__(self):
        #size
        random_size_value = random.uniform(COCKROACH_SIZE_RANDOMIZE[0], COCKROACH_SIZE_RANDOMIZE[1])
        size = (int(COCKROACH_SIZES[0] * random_size_value), int(COCKROACH_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        # Load hình ảnh tùy theo hướng di chuyển của đối tượng
        if moving_direction in ["right", "left"]: #right or left direction
            self.images = [image.load("Assets/Cockroach/right.png", size=size, flip=moving_direction=="right")]
        elif moving_direction == "up": #up
            self.images = [image.load("Assets/Cockroach/up.png", size=size)]
        else:  # down
            self.images = [image.load("Assets/Cockroach/down.png", size=size)]
        self.current_frame = 0
        self.animation_timer = 0

    def define_spawn_pos(self, size): # define the start pos and moving vel of the cockroach
        vel = random.uniform(COCKROACH_MOVE_SPEED["min"], COCKROACH_MOVE_SPEED["max"])
        moving_direction = random.choice(("left", "right", "up", "down"))
        if moving_direction == "right":
            start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [-vel, 0]
        elif moving_direction == "left":
            start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [vel, 0]
        elif moving_direction == "up":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), SCREEN_HEIGHT + size[1])
            self.vel = [0, -vel]
        else:  # down
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), -size[1])
            self.vel = [0, vel]
        return moving_direction, start_pos


    def move(self):
        self.rect.move_ip(self.vel)


    def animate(self): # change the frame of the insect when needed
        t = time.time()
        if t > self.animation_timer:
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images)-1:
                self.current_frame = 0


    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)



    def draw(self, surface):
        self.animate()
        image.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def kill(self, Cockroach): # remove the cockroach from the list
        Cockroach.remove(self)
        return 1
