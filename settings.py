class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # 背景色
        self.bg_color = (230, 230, 230)

        # 数量限制
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 外星人
        self.alien_drop_speed = 10

        # 以什么速度加快游戏节奏
        self.speedup_scale = 1.1
        # 击落外星人得分倍率调整
        self.score_scale = 1.5

        # 击落外星人得分
        self.alien_points = 50

        # 动态数据,下面赋值
        self.alien_orientations = None
        self.alien_speed = None
        self.bullet_speed = None
        self.ship_speed = None
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1
        # 击落外星人得分
        self.alien_points = 50

        # 方向控制
        self.alien_orientations = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = (self.alien_points * self.score_scale)
