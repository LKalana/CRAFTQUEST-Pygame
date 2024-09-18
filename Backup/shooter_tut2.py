import pygame

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')  # Set the window title

# Set up the game clock and frames per second
clock = pygame.time.Clock()  # Create a Pygame clock object to control the game's timing
FPS = 60  # Define the desired frames per second for the game's update/render loop


# Variables to track player movement
moving_left = False
moving_right = False

# Background color in RGB format
BG = (144, 201, 120)

# Function to draw the background
def draw_bg():
    screen.fill(BG)

# Soldier class representing game characters
class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type  # Type of character, such as 'player' or 'enemy'
        self.speed = speed  # Movement speed of the soldier
        self.direction = 1  # Direction the soldier is facing (1 for right, -1 for left)
        self.flip = False  # Flag indicating whether the soldier's image should be flipped horizontally
        # Load the character image and scale it
        img = pygame.image.load(f'img/{self.char_type}/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()  # Get the rectangular area of the image
        self.rect.center = (x, y)  # Set the center of the rectangle to the specified initial position (x, y)

    def move(self, moving_left, moving_right):
        # Reset movement variables
        dx = 0  # Change in x-coordinate (horizontal movement) initialized to 0
        dy = 0  # Change in y-coordinate (vertical movement) initialized to 0


        # Assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed  # Set horizontal movement to the left with the soldier's speed
            self.flip = True  # Flip the soldier's image to face left
            self.direction = -1  # Set the direction to -1, indicating movement to the left
        if moving_right:
            dx = self.speed  # Set horizontal movement to the right with the soldier's speed
            self.flip = False  # Do not flip the soldier's image (face right)
            self.direction = 1  # Set the direction to 1, indicating movement to the right


        # Update rectangle position
        self.rect.x += dx  # Update the x-coordinate of the soldier's rectangle based on horizontal movement
        self.rect.y += dy  # Update the y-coordinate of the soldier's rectangle based on vertical movement


    def draw(self):
        # Draw the character on the screen
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

# Create player and enemy instances
player = Soldier('player', 200, 200, 3, 5)
enemy = Soldier('enemy', 400, 200, 3, 5)

# Game loop
run = True
while run:
    clock.tick(FPS)  # Control the frame rate

    draw_bg()  # Draw the background
    player.draw()  # Draw the player character
    enemy.draw()   # Draw the enemy character

    player.move(moving_left, moving_right)  # Move the player character

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Quit the game if the window is closed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True  # Set the flag for moving left
            if event.key == pygame.K_d:
                moving_right = True  # Set the flag for moving right
            if event.key == pygame.K_ESCAPE:
                run = False  # Quit the game if the ESC key is pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False  # Reset the flag for moving left
            if event.key == pygame.K_d:
                moving_right = False  # Reset the flag for moving right

    pygame.display.update()  # Update the display

pygame.quit()  # Clean up and exit the Pygame library
