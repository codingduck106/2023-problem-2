import pygame, random

pygame.init()

# Set up window
window = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
pygame.display.set_caption("Pygame Random Color & Movement")

# Game variables
running = True
x, y = 300, 300
font = pygame.font.Font(None, 74)

# Initial random color
r, g, b = 1, 2, 3

# Main game loop
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            if random.randint(0, 5) == 1:
                running = False
            else:
                window = pygame.display.set_mode((1,1))
                pygame.time.wait(1000)
                window = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
                # pygame.display.toggle_fullscreen()
                # Render the text only when quitting
                text = font.render('*But it refused*', True, (255 - r, 255 - g, 255 - b)) # Optional: fill the window with black before displaying text
                window.blit(text, (100,100))
                pygame.display.flip()
                  # Wait a bit to show the text before quitting
                pygame.time.wait(1000)
        elif e.type == pygame.KEYDOWN:
            # Player movement
            if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                x -= 5
            if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                x += 5
            if e.key == pygame.K_UP or e.key == pygame.K_w:
                y -= 5
            if e.key == pygame.K_DOWN or e.key == pygame.K_s:
                y += 5

    # Update the background color randomly
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    color = pygame.Color(r, g, b)

    # Fill the window with the background color
    window.fill(color)

    # Render the player character (as a rectangle)
    player_rect = pygame.Surface((100, 100))
    player_rect.fill(pygame.Color(255 - r, 255 - g, 255 - b))  # Player color is complementary to background
    window.blit(player_rect, (x, y))

    # Refresh the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
