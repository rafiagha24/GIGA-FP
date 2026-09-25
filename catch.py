import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600


player_width = 50
player_height = 50
player_speed = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

position_x = WIDTH // 2 - player_width // 2
position_y = 3 * HEIGHT // 4

player = pygame.Rect(
    position_x,
    position_y,
    player_width,
    player_height
)

ground = pygame.Rect(0, 500, 800, 100)

item = pygame.Rect(
    random.randint(0, WIDTH - 20),
    0,
    20,
    20
)

item_type = random.choice([
    "food",
    "double",
    "bomb"
])

score = 0
font = pygame.font.Font(None, 36)
lives = 3


start_time = pygame.time.get_ticks()
game_over = False

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed

        if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
            player.x += player_speed

        player.y += player_speed

        if player.colliderect(ground):
            player.bottom = ground.top

        elapsed_time = pygame.time.get_ticks() - start_time

        item_speed = 3 + elapsed_time // 10000
        item.y += item_speed

        if item.colliderect(player):

            # Food biasa
            if item_type == "food":
                score += 1

            # Double score
            elif item_type == "double":
                score += 2

            # Bomb
            elif item_type == "bomb":
                lives -= 1

                if lives <= 0:
                    game_over = True

            item.x = random.randint(
                0,
                WIDTH - item.width
            )

            item.y = 0

            item_type = random.choice([
                "food",
                "double",
                "bomb"
            ])

        if item.bottom >= ground.top:

            item.x = random.randint(
                0,
                WIDTH - item.width
            )

            item.y = 0

            item_type = random.choice([
                "food",
                "double",
                "bomb"
            ])

    screen.fill((255, 255, 255))

    # Player
    pygame.draw.rect(
        screen,
        (0, 0, 255),
        player
    )

    # Ground
    pygame.draw.rect(
        screen,
        (0, 255, 0),
        ground
    )

    if item_type == "food":

        # Food biasa
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            item
        )

    elif item_type == "double":

        # Double score
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            item
        )

    elif item_type == "bomb":

        # Bomb
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            item
        )

    score_text = font.render(
        f"Score: {score}",
        True,
        (0, 0, 0)
    )

    screen.blit(
        score_text,
        (20, 20)
    )

    lives_text = font.render(
        f"Lives: {lives}",
        True,
        (255, 0, 0)
    )

    screen.blit(
        lives_text,
        (20, 55)
    )

    if game_over:

        game_over_text = font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        screen.blit(
            game_over_text,
            (
                WIDTH // 2 - 80,
                HEIGHT // 2
            )
        )

    pygame.display.update()

    clock.tick(60)

pygame.quit()