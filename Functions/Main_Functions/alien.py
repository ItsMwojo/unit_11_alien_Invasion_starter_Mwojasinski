import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """A class for a alien enemy"""

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def __init__(self, ai_game):
        """Initialize and place the alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien image
        self.image = pygame.image.load("Resources/Game_Images/enemy_4.png")
        self.rect = self.image.get_rect()
        # Start each new alien near the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x


