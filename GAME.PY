import pygame
from pygame.locals import *
from sys import exit
import random

# -----------------------------设置全局变量-----------------------------
GAME_WINDP_HEIGH = 864  # 窗口高度
# GAME_WINDP_WEDTH = 1024  # 窗口宽度
GAME_WINDP_WEDTH = 960  # 窗口宽度
GAME_WINDP_BASEY = 432  # 中心高度
GAME_PIPES_WIDTH = 52  # 管子宽度
GAME_PIPES_HEIGH = 512  # 管子高度
GAME_PIPES_GAPSZ = 10  # 水管间距
GAME_BIRDS_WIDTH = 48  # 小鸟宽度
GAME_BIRDS_HEIGH = 48  # 小鸟高度
global BIRD_X
global BIRD_Y
global BIRD_V
BIRD_X = 420
BIRD_Y = 432
BIRD_V = 0
WIND_WINDP = pygame.display.set_mode((GAME_WINDP_HEIGH, GAME_WINDP_WEDTH))


# -----------------------------设置全局变量-----------------------------
class IMGS:
    POSX = 0
    POSY = 0
    POSW = 0
    POSH = 0
    NAME = ""

    def __init__(self, NAME):
        self.NAME = NAME
        self.DATA = pygame.image.load("./ASSE/PICTS_" + NAME + ".PNG").convert_alpha()

    def PICS(self, NAME):
        self.NAME = NAME
        self.DATA = pygame.image.load("./ASSE/PICTS_" + NAME + ".PNG").convert_alpha()

    def SETP(self, X, Y, W, H):
        self.POSX = X
        self.POSY = Y
        self.POSW = W
        self.POSH = H

    def SHOW(self):
        WIND_WINDP.blit(self.DATA, (self.POSX, self.POSY, self.POSW, self.POSH))


def GAME_PIPE():
    # 两个水管之间的距离有如下变量
    PIPE_GAPS = [100, 200, 300, 400]
    PIPE_PIJG = [60, 90, 120, 150, 180]
    PIPE_RAND = random.randint(0, len(PIPE_GAPS) - 1)
    PIPE_GAPY = PIPE_GAPS[PIPE_RAND]
    PIPE_RAND = random.randint(0, len(PIPE_PIJG) - 1)
    PIPE_PIJR = PIPE_PIJG[PIPE_RAND]
    PIPE_GAPX = GAME_WINDP_WEDTH + 10
    return [
        {'x': PIPE_GAPX, 'y': PIPE_GAPY - GAME_PIPES_WIDTH - 600 - PIPE_PIJR},  # 上面水管的左上角位置
        {'x': PIPE_GAPX, 'y': PIPE_GAPY + GAME_PIPES_HEIGH - 300 + PIPE_PIJR},  # 下面水管的左上角位置
    ]


def GAME_INIT():
    pygame.init()
    pygame.display.set_caption("Flappy Bird")
    pygame.mixer.music.load("./ASSE/MUSIC_BGM.WAV")
    global REND_BGPBT
    global REND_BGPHY
    global REND_START
    global REND_TITLE
    global REND_BIRD1
    global REND_BIRD2
    global REND_BIRD3
    global REND_BIRDS
    global REND_PIPUP
    global REND_PIPDO
    global REND_STTIP
    global REND_LANGS
    global REND_OVERD
    global REND_SCORE
    global REND_PANEL
    REND_BGPBT = IMGS("BGPBT")
    REND_BGPHY = IMGS("BGPHY")
    REND_START = IMGS("START")
    REND_TITLE = IMGS("TITLE")
    REND_BIRDS = IMGS("BIRD1")
    REND_BIRD1 = IMGS("BIRD1")
    REND_BIRD2 = IMGS("BIRD2")
    REND_BIRD3 = IMGS("BIRD3")
    REND_PIPUP = IMGS("PIPUP")
    REND_PIPDO = IMGS("PIPDO")
    REND_STTIP = IMGS("STTIP")
    REND_LANGS = IMGS("LANGS")
    REND_OVERD = IMGS("OVERD")
    REND_PANEL = IMGS("PANEL")
    REND_SCORE = []
    REND_BGPBT.SETP(000, 000, 576, 1024)
    REND_BGPHY.SETP(000, 000, 576, 1024)
    REND_START.SETP(320, 330, 170, 48)
    REND_TITLE.SETP(170, 140, 170, 48)
    REND_STTIP.SETP(170, 140, 170, 48)
    REND_OVERD.SETP(130, 200, 170, 48)
    REND_PANEL.SETP(135, 350, 170, 48)
    REND_LANGS.SETP(0, 0, 100, 100)
    for i in range(10):
        REND_SCORE.append(IMGS("NUML" + str(i)))
        REND_SCORE[i].SETP(0, 0, 24, 44)
    pygame.mixer.init()
    # SOUND_BGM = pygame.mixer.music.load("")

    pygame.mixer.music.set_volume(0.5)


def GAME_OVER(STATUE, BIRD_SCOE):
    with open('./ASSE/SAVE.DAT', 'r+') as f:
        LAST_SCOE = int(f.read())
        f.close()
    if LAST_SCOE < BIRD_SCOE:
        with open('./ASSE/SAVE.DAT', 'w+') as f:
            f.write(str(BIRD_SCOE))
    if BIRD_SCOE <= 9:
        MSTR = 'MEDA' + str(0)
    elif BIRD_SCOE <= 49:
        MSTR = 'MEDA' + str(1)
    elif BIRD_SCOE <= 99:
        MSTR = 'MEDA' + str(2)
    else:
        MSTR = 'MEDA' + str(3)
    REND_MEDAL = IMGS(MSTR)
    REND_MEDAL.SETP(210,475,96,96)

    SOUND_DIE = pygame.mixer.Sound("./ASSE/MUSIC_DIE.WAV")
    pygame.time.delay(1000)
    SOUND_DIE.play()

    pygame.time.delay(300)
    if STATUE == 1:
        REND_BIRDS.SETP(BIRD_X, BIRD_Y, 48, 48)
        REND_BIRDS.SHOW()
    REND_OVERD.SHOW()
    REND_PANEL.SHOW()
    REND_START.SETP(320, 700, 170, 48)
    REND_START.SHOW()
    SCOE_B = BIRD_SCOE // 100
    SCOE_S = BIRD_SCOE %100 // 10
    SCOE_G = BIRD_SCOE % 10
    REND_SCORE[SCOE_G].SETP(630, 450, 24, 44)
    REND_SCORE[SCOE_G].SHOW()
    REND_SCORE[SCOE_S].SETP(600, 450, 24, 44)
    REND_SCORE[SCOE_S].SHOW()
    REND_SCORE[SCOE_B].SETP(570, 450, 24, 44)
    REND_SCORE[SCOE_B].SHOW()

    SCOE_B = LAST_SCOE // 100
    SCOE_S = LAST_SCOE %100 // 10
    SCOE_G = LAST_SCOE % 10
    REND_SCORE[SCOE_G].SETP(630, 560, 24, 44)
    REND_SCORE[SCOE_G].SHOW()
    REND_SCORE[SCOE_S].SETP(600, 560, 24, 44)
    REND_SCORE[SCOE_S].SHOW()
    REND_SCORE[SCOE_B].SETP(570, 560, 24, 44)
    REND_SCORE[SCOE_B].SHOW()
    REND_MEDAL.SHOW()
    pygame.display.update()

    while 1:
        for GAME_EVENT in pygame.event.get():
            if GAME_EVENT.type == QUIT:
                exit(0)
            if GAME_EVENT.type == MOUSEBUTTONUP:
                EVEN_MOUSE_X, EVEN_MOUSE_Y = GAME_EVENT.pos
                if EVEN_MOUSE_X >= 320 and EVEN_MOUSE_X <= 540 and EVEN_MOUSE_Y >= 700 and EVEN_MOUSE_Y <= 450 + 370:
                    return


def GAME_MENU():
    OFPS_NUMS = 60
    OFPS_LOCK = pygame.time.Clock()

    while True:
        REND_BGPBT.SHOW()
        REND_START.SETP(320, 330, 170, 48)
        REND_START.SHOW()
        REND_TITLE.SHOW()
        REND_LANGS.SETP(REND_LANGS.POSX - 2, 850, 52, 320)
        REND_LANGS.SHOW()
        REND_LANGS.SETP(REND_LANGS.POSX + 940, 850, 52, 320)
        REND_LANGS.SHOW()
        REND_LANGS.SETP(REND_LANGS.POSX - 943, 850, 52, 320)
        pygame.display.update()
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
        if REND_LANGS.POSX <= -941:
            REND_LANGS.SETP(0, 850, 52, 320)
        for GAME_EVENT in pygame.event.get():
            if GAME_EVENT.type == QUIT:
                exit()
            if GAME_EVENT.type == MOUSEBUTTONUP:
                EVEN_MOUSE_X, EVEN_MOUSE_Y = GAME_EVENT.pos
                if EVEN_MOUSE_X >= 320 and EVEN_MOUSE_X <= 540 and EVEN_MOUSE_Y >= 330 and EVEN_MOUSE_Y <= 450:
                    GAME_GAME()
        OFPS_LOCK.tick(OFPS_NUMS)


def GAME_GAME():
    BIRD_V = 0
    OFPS_NUMS = 60
    OFPS_LOCK = pygame.time.Clock()
    BIRD_Y = 300  # 小鸟状态
    PIPE_SPEX = -4  # 管道速度
    PIPE_SPEO = -4  # 初始速度
    PIPE_NEWP = GAME_PIPE()
    PIPE_UPPS = [{'x': GAME_WINDP_WEDTH, 'y': PIPE_NEWP[0]['y']}]
    PIPE_DOPS = [{'x': GAME_WINDP_WEDTH, 'y': PIPE_NEWP[1]['y']}]
    BIRD_SCOE = 0
    GAME_TIME = pygame.time.get_ticks()
    GAME_LAST = GAME_TIME
    BIRD_SCOE += 0  # 跳关数
    SOUND_POT = pygame.mixer.Sound("./ASSE/MUSIC_POT.WAV")
    SOUND_PAS = pygame.mixer.Sound("./ASSE/MUSIC_PAS.WAV")
    SOUND_HIT = pygame.mixer.Sound("./ASSE/MUSIC_HIT.WAV")
    while True:
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
        for GAME_EVENT in pygame.event.get():
            if GAME_EVENT.type == QUIT:
                exit(0)
            if GAME_EVENT.type == MOUSEBUTTONUP or GAME_EVENT.type == KEYDOWN:
                BIRD_V = -15 - BIRD_SCOE / 48
                SOUND_POT.play()
                if BIRD_V <= -16:
                    BIRD_V = -16
        if BIRD_V < 0:
            BIRD_Y += BIRD_V
            BIRD_V += 1
        else:
            BIRD_A = 0.5 + BIRD_SCOE / 96
            if BIRD_A >= 1:
                BIRD_A = 1
            BIRD_V += BIRD_A
            BIRD_Y += BIRD_V
        BIRD_Y = BIRD_Y + 3
        if BIRD_Y > GAME_WINDP_HEIGH - 80:
            SOUND_HIT.play()
            GAME_OVER(0, BIRD_SCOE)
            return
        if BIRD_Y < 0:
            BIRD_Y = 0
            BIRD_V = 5
        if BIRD_SCOE // 10 % 2 == 0:
            REND_BGPBT.SHOW()
        else:
            REND_BGPHY.SHOW()

        for PIPE_SET_UP, PIPE_SET_DO in zip(PIPE_UPPS, PIPE_DOPS):
            REND_PIPUP.SETP(PIPE_SET_UP['x'], PIPE_SET_UP['y'], 52, 320)
            REND_PIPDO.SETP(PIPE_SET_DO['x'], PIPE_SET_DO['y'], 52, 320)
            REND_PIPUP.SHOW()
            REND_PIPDO.SHOW()
            REND_LANGS.SETP(REND_LANGS.POSX - 3, 850, 52, 320)
            REND_LANGS.SHOW()
            REND_LANGS.SETP(REND_LANGS.POSX + 941, 850, 52, 320)
            REND_LANGS.SHOW()
            REND_LANGS.SETP(REND_LANGS.POSX - 944, 850, 52, 320)
            if REND_LANGS.POSX <= -941:
                REND_LANGS.SETP(0, 850, 52, 320)
            if BIRD_X >= PIPE_SET_UP['x'] - 50 and BIRD_X <= PIPE_SET_UP['x'] + 52:
                if BIRD_Y >= PIPE_SET_DO['y'] - 60 or BIRD_Y <= PIPE_SET_UP['y'] + 740:
                    SOUND_HIT.play()
                    GAME_OVER(1, BIRD_SCOE)
                    return
            if BIRD_SCOE // 10 % 3 == 0:
                REND_BIRDS = REND_BIRD1
            elif BIRD_SCOE // 10 % 3 == 1:
                REND_BIRDS = REND_BIRD2
            else:
                REND_BIRDS = REND_BIRD3
            REND_BIRDS.SETP(BIRD_X, BIRD_Y, 48, 48)
            REND_BIRDS.SHOW()
        SCOE_B = (BIRD_SCOE // 100)
        SCOE_S = BIRD_SCOE % 100 // 10
        SCOE_G = BIRD_SCOE % 10
        REND_SCORE[SCOE_G].SETP(90, 30, 24, 44)
        REND_SCORE[SCOE_G].SHOW()
        REND_SCORE[SCOE_S].SETP(60, 30, 24, 44)
        REND_SCORE[SCOE_S].SHOW()
        REND_SCORE[SCOE_B].SETP(30, 30, 24, 44)
        REND_SCORE[SCOE_B].SHOW()
        for PIPE_SET_UP, PIPE_SET_DO in zip(PIPE_UPPS, PIPE_DOPS):
            PIPE_SET_UP['x'] += PIPE_SPEX
            PIPE_SET_DO['x'] += PIPE_SPEX
        # 当水管移动到某一位置的时候，生成新的水管
        GAME_TIME = pygame.time.get_ticks()
        GAME_TTDS = 3000 - BIRD_SCOE * 50
        if GAME_TTDS <= 600:
            GAME_TTDS = 600
        if int(GAME_TIME - GAME_LAST) > GAME_TTDS:
            PIPE_NEWS = GAME_PIPE()
            PIPE_UPPS.append(PIPE_NEWS[0])
            PIPE_DOPS.append(PIPE_NEWS[1])
            GAME_LAST = GAME_TIME
            BIRD_SCOE += 1
            SOUND_PAS.play()
            PIPE_SPEX = PIPE_SPEO - BIRD_SCOE / 20
            if PIPE_SPEX <= -10:
                PIPE_SPEX = -10
        # 如果水管从右往左移动到边缘，则摧毁水管
        if PIPE_UPPS[0]['x'] < -10:
            # 队列头出队
            PIPE_UPPS.pop(0)
            PIPE_DOPS.pop(0)
        # 刷新画面
        pygame.display.update()
        OFPS_LOCK.tick(OFPS_NUMS)
while 1:
    GAME_INIT()
    GAME_MENU()
