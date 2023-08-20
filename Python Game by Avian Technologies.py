import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()

        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Simple Game")

        self.clock = pygame.time.Clock()

        self.player = pygame.Rect(50, 50, 50, 50)
        self.player_speed = 5

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.x -= self.player_speed
            if keys[pygame.K_RIGHT]:
                self.player.x += self.player_speed
            if keys[pygame.K_UP]:
                self.player.y -= self.player_speed
            if keys[pygame.K_DOWN]:
                self.player.y += self.player_speed

            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (255, 0, 0), self.player)
            pygame.display.flip()

            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
