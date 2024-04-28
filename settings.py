class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800

        # 背景色
        self.bg_color = (230, 230, 230)

        # 飞船移动速度
        self.ship_speed = 1.5