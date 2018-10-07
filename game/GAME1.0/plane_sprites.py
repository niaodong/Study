import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 852)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 调用父类创建精灵
        super().__init__("./images/background.png")
        # 判断是否是交替图像，如果是就要设置初始设置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法
        super().update()
        # 判断是否移除屏幕，移除后返回屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 调用父类创建敌机，指定敌机图片
        super().__init__("./images/enemy0.png")
        # 指定随机速度
        self.speed = random.randint(1, 4)
        # 指定随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类，保持垂直飞行
        super().update()
        # 判断是否飞出屏幕，飞出就删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 设置image和速度
        super().__init__("./images/hero1.png", 0)
        # 初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平方向移动
        self.rect.x += self.speed
        # 不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0, 1):
            # 创建子弹精灵
            bullet = Bullet()
            # 设置位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 设置图片与初始速度
        super().__init__("./images/bullet.png", -2)

    def update(self):
        # 调用父类 子弹垂直方向飞行
        super().update()
        # 判断是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()
