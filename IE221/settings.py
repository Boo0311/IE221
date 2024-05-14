import pygame

WINDOW_NAME = "Cockroach Exterminator"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 100
HAND_HITBOX_SIZE = (60,80)
COCKROACH_SIZES = (80, 80)
COCKROACH_SIZE_RANDOMIZE = (1,2) # Với mỗi đối tượng được tạo mới sẽ ngẫu nhiên lựa chọn giữa giá trị 1 và 2
INSECTS_SIZES = (85, 85)
INSECTS_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
DRAW_HITBOX = False # tạo hit box cho đối tượng
# animation
ANIMATION_SPEED = 0.08 # frame của đối tượng sẽ thay đổi trên x giây

# difficulty
GAME_DURATION = 60 # trò chơi sẽ kết thúc sau x giây
COCKROACH_SPAWN_TIME = 1
COCKROACH_MOVE_SPEED = {"min": 1, "max": 5}
INSECTS_PENALITY = 1 # sẽ trừ 1 điểm nếu tiêu diệt đối tượng không phải gián

# colors
COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} # màu hiển thị trên màn hình và các nút bấm

# sounds / music
MUSIC_VOLUME = 0.16 # giá trị giữa 0 và 1
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
