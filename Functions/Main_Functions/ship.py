import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class of the Ship aka player"""

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Ship's position"""
        # Update the ship's x value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def __init__(self, ai_game):
        """ship starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Ship image
        self.image = pygame.image.load("Resources/Game_Images/ship.png")
        self.rect = self.image.get_rect()
        # Start each new ship 
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False






