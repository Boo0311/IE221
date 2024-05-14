import pygame
import random
import image
from settings import *
from cockroach import Cockroach

class Insects(Cockroach):
    def __init__(self):
        #size
        random_size_value = random.uniform(INSECTS_SIZE_RANDOMIZE[0], INSECTS_SIZE_RANDOMIZE[1])
        size = (int(INSECTS_SIZES[0] * random_size_value), int(INSECTS_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
       # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        # Load hình ảnh tùy theo hướng di chuyển của đối tượng
        if moving_direction in ["right", "left"]: #right or left direction
            self.images = [image.load("Assets/Insects/cartoonspider_right.png", size=size, flip=moving_direction=="right")]
        elif moving_direction == "up": #up
            self.images = [image.load("Assets/Insects/cartoonspider_up.png", size=size)]
        else:  # down
            self.images = [image.load("Assets/Insects/cartoonspider_down.png", size=size)]
        self.current_frame = 0
        self.animation_timer = 0
        

    def kill(self, Cockroach): # remove the insects from the list
        Cockroach.remove(self)
        return -INSECTS_PENALITY
