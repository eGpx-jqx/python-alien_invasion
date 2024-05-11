class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.ships_left = self.settings.ship_limit

        self.score = 0
        # 最高分记录
        self.high_score = 0
        # 等级
        self.level = 1

        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        # 游戏得分
        self.score = 0
