import pygame.sysfont


class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.sysfont.SysFont(None, 45)

        # 画一个长方形按钮,  并设置居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 将文字转成image, 方便后面渲染
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        # 填充(绘制)长方形
        self.screen.fill(self.button_color, self.rect)
        # 将图片传输(绘制)到屏幕上
        self.screen.blit(self.msg_image, self.msg_image_rect)
