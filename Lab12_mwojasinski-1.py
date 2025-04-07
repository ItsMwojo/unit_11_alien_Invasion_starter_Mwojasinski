# Lab12_mwojasinski_1.py
# Author: Matthew Wojasinski
# This program places the spaceship on either the left or right edge, facing the center,
# and allows it to move vertically with the arrow keys.
# Date: 2025-04-06

import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (30, 30, 30)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lab12 - Reposition Spaceship")

# Load ship image with dynamic path
base_path = os.path.dirname(__file__)
ship_image_path = os.path.join(base_path, 'Assets', 'images', 'ship.png')

try:
    ship_image = pygame.image.load(ship_image_path)
except FileNotFoundError:
    print("Ship image not found at:", ship_image_path)
    pygame.quit()
    sys.exit()

# Rotate the ship image 90 degrees to the right (clockwise)
ship_image = pygame.transform.rotate(ship_image, -90)

# Get rect and set initial position (left side)
ship_rect = ship_image.get_rect()
ship_rect.left = 20  # start near the left edge
ship_rect.centery = SCREEN_HEIGHT // 2

# Speed settings
ship_speed = 5

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ship_rect.top > 0:
        ship_rect.y -= ship_speed
    if keys[pygame.K_DOWN] and ship_rect.bottom < SCREEN_HEIGHT:
        ship_rect.y += ship_speed

    # Draw rotated ship
    screen.blit(ship_image, ship_rect)

    # Update screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
