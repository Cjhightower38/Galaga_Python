# Import the pygame() functionality for games
import pygame

from settings import Settings
from ninja import Ninja
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
	
	# Make a ship
	ship = Ninja(screen)
	
	# Set the background color.
	# Add a variable equal to a RGB(color)
	bg_color = (230, 230, 230)
	
	# Start the main loop for a game.
	while True:
		gf.check_events()
		gf.update_screen(ai_settings, screen, ship)
		
		# The call to pygame.display.flip() tells python to		
		# make the most recently drwan visible.
		pygame.display.flip()

# Call the run_game function		
run_game()
