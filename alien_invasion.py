import sys

from alien import Alien
from ship import Ship
import pygame

from settings import Settings
from bullet import Bullet


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(size=(self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            # 设置刷新率
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # 按下按键
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    # 松开按键
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # 填充背景色
        self.screen.fill(self.settings.bg_color)
        # 写入飞船
        self.ship.blitme()
        # 写入子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 写入飞船
        self.aliens.draw(self.screen)
        # 绘制
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _update_bullets(self):
        # 删除子弹
        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    # 创建飞船舰队
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y <= (self.settings.screen_height - 3 * alien_height):
            while current_x <= (self.settings.screen_width - 2 * alien_width):
                alien = Alien(self)
                alien.rect.x = current_x
                alien.rect.y = current_y
                alien.x = current_x
                self.aliens.add(alien)
                current_x = current_x + alien_width * 2
            current_x = alien_width
            current_y = current_y + alien_height * 2

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.alien_orientations *= -1


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
