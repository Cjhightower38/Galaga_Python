# Import the pygame() functionality for games
import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

# Create a def() for run_game function
def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	# Add a variable to store Settings()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	
	# Make the Play button.
	play_button = Button(ai_settings, screen, 'Press Play')
	
	# Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	# Make a ship, a group of bullets, and a group of aliens
	ship = Ship(ai_settings, screen)
	# Make a group to store bullets in.
	bullets = Group()
	aliens = Group()
	
	# Set the background color.
	# Add a variable equal to a RGB(color)
	bg_color = (230, 230, 230)
	
	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# Start the main loop for a game.
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
			
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
			
		# The call to pygame.display.flip() tells python to		
		# make the most recently drwan visible.
		pygame.display.flip()

# Call the run_game function		
run_game()
