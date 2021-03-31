import pygame
import os
FPS = 60
WHITE = (255,255,255)
HIT = pygame.USEREVENT + 1
pygame.font.init()

def get_path(name):
    import os
    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, name))
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


RANDFONT = pygame.font.Font(os.path.join('res',"SimHei.ttf"), 30)

def get_pos(img, x, y, width, height):
    import pygame
    image = pygame.Surface((width, height), pygame.SRCALPHA)
    image.blit(img, (0, 0), (x, y, width, height))
    return image

def handle_bullets(bullets,rect):
    for bullet in bullets:
        bullet.x += 10
        if rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(HIT))
            bullets.remove(bullet)

if __name__ == '__main__':
    from pygame.locals import *
    # 导入一些常用的函数和常量
    from sys import exit

    # 向sys模块借一个exit函数用来退出程序

    pygame.init()
    # 初始化pygame,为使用硬件做准备

    screen = pygame.display.set_mode((640, 480), 0, 32)
    # 创建了一个窗口
    pygame.display.set_caption("Cat Tower")
    # 设置窗口标题
    from render.image_background import cfg_shop_bg
    background = cfg_shop_bg[126]
    bg = pygame.image.load(os.path.join('res','shop_bg.png'))
    bg = get_pos(bg, 0, 387, 390, 390)
    rect_pic = pygame.Rect(100,100,10,400)
    # 加载并转换图像
    bg = pygame.transform.scale(bg,(50,50))

    # time
    clock = pygame.time
    bullets = []

    def draw_window(bg, rect, bullets):
        screen.fill(WHITE)
        screen.blit(bg, (rect.x, rect.y))
        pygame.draw.rect(screen,(0,0,0), rect_pic)

        text = RANDFONT.render("你好", 1, (255, 0, 0))
        screen.blit(text, (200, 200))

        for bullet in bullets:
            pygame.draw.rect(screen, (255,0,0), bullet)

        pygame.display.update()

    #
    rect = pygame.Rect(100,100, 50,50)
    while True:
        # 游戏主循环

        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出事件后退出程序
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(rect.x + rect.width, rect.y + rect.height//2 - 2, 10, 5)
                    bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            rect.y -= 1
        if keys_pressed[pygame.K_DOWN]:
            rect.y += 1
        if keys_pressed[pygame.K_LEFT]:
            rect.x -= 1
        if keys_pressed[pygame.K_RIGHT]:
            rect.x += 1

        handle_bullets(bullets,rect)
        draw_window(bg, rect, bullets)


        # 将背景图画上去


        # 刷新一下画面