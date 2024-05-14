import pygame
import image
from settings import *
from hand_tracking import HandTracking
import cv2

class Hand:
    def __init__(self):
        self.orig_image = image.load("Assets/Tools/snapedit_1712624426740.png", size=(100,200))
        self.image = self.orig_image.copy()
        self.image_smaller = image.load("Assets/Tools/snapedit_1712624426740.png", size=(100 - 30, 200 - 30))
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])
        self.left_click = False
        


    def follow_mouse(self): # thay đổi vị trí của con chuột dựa trên chuyển động của tay.
        self.rect.center = pygame.mouse.get_pos()
        

    def follow_mediapipe_hand(self, x, y):
        self.rect.center = (x, y)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)


    def draw(self, surface):
        image.draw(surface, self.image, self.rect.center, pos_mode="center")

        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def on_insect(self, insects): # trả lại list các đối tượng đang nằm trong phạm vi tính điểm của con trỏ
        return [insect for insect in insects if self.rect.colliderect(insect.rect)]


    def kill_insects(self, insects, score, sounds): # tiêu diệt đối tượng đang nằm trong pạm vi hitbox của con trỏ khi nhấn chuột trái
        if self.left_click: # if left click
            for insect in self.on_insect(insects):
                insect_score = insect.kill(insects)
                score += insect_score
                sounds["slap"].play()
                if insect_score < 0:
                    sounds["screaming"].play()
        else:
            self.left_click = False
        return score
