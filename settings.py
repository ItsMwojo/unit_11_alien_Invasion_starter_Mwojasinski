class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship 
        self.ship_limit = 3
        # Bullet 
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien 
        self.fleet_drop_speed = 10
        # Speed up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Settings that change throughout the game."""
        self.ship_speed = 2.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.5
        # fleet_direction 1 right -1 left
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 150


