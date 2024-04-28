import pygame.image


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 配置类, 如飞船移动速度
        self.settings = ai_game.settings

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # 放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 飞船坐标, self.rect中的坐标只允许整数, 但是移动速度为float, 后面要转换
        self.x = float(self.rect.x)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  # 速度
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        # 将只保留整数值部分
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
