import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable, asteroid_group)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (updatable, drawable, shot_group)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for u in updatable:
            u.update(dt)
        for asteroid in asteroid_group:
            if asteroid.is_collide(player):
                print("Game over!")
                exit()
            for shot in shot_group:
                if asteroid.is_collide(shot):
                    shot.kill()
                    asteroid.split()
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # convert ms to seconds


if __name__ == "__main__":
    main()
