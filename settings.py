class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # 背景色
        self.bg_color = (230, 230, 230)

        # 飞船速度/数量限制
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 外星人
        self.alien_speed = 1
        self.alien_drop_speed = 10
        # 方向控制
        self.alien_orientations = 1
