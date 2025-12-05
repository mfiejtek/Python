# main.py
import pygame
import sys
import settings
from snowflake import Snowflake

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Topnienie Śniegu")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 24)
    game_over_font = pygame.font.SysFont("arial", 48, bold=True)

    falling_snowflakes = []
    snow_piles = [0] * settings.NUM_COLUMNS 
    
    spawn_timer = 0
    score = 0
    game_over = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_pos = pygame.mouse.get_pos()
                for flake in falling_snowflakes[:]:
                    if flake.is_clicked(mouse_pos):
                        falling_snowflakes.remove(flake)
                        score += 1

        if game_over:
            draw_game_over(screen, game_over_font, score)
            pygame.display.flip()
            continue

        spawn_timer += 1
        if spawn_timer >= settings.SPAWN_RATE:
            falling_snowflakes.append(Snowflake())
            spawn_timer = 0

        for flake in falling_snowflakes[:]:
            flake.move()

            current_pile_height = snow_piles[flake.col_idx]
            ground_level = settings.SCREEN_HEIGHT - current_pile_height

            if flake.y + flake.radius >= ground_level:
                falling_snowflakes.remove(flake)
                
                snow_piles[flake.col_idx] += (flake.radius * 2)
                
                if snow_piles[flake.col_idx] >= settings.SCREEN_HEIGHT:
                    game_over = True

        screen.fill(settings.BG_COLOR)

        for flake in falling_snowflakes:
            flake.draw(screen)

        for i in range(settings.NUM_COLUMNS):
            if snow_piles[i] > 0:
                rect_x = i * settings.COLUMN_WIDTH
                rect_h = snow_piles[i]
                rect_y = settings.SCREEN_HEIGHT - rect_h
                pygame.draw.rect(screen, settings.SNOW_COLOR, (rect_x, rect_y, settings.COLUMN_WIDTH, rect_h))

        score_surf = font.render(f"Wynik: {score}", True, settings.TEXT_COLOR)
        screen.blit(score_surf, (10, 10))

        pygame.display.flip()
        clock.tick(settings.FPS)

    pygame.quit()
    sys.exit()

def draw_game_over(screen, font, score):
    text = font.render("KONIEC GRY", True, settings.GAME_OVER_COLOR)
    text_rect = text.get_rect(center=(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2))
    screen.blit(text, text_rect)
    
    score_text = font.render(f"Twój wynik: {score}", True, settings.TEXT_COLOR)
    score_rect = score_text.get_rect(center=(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2 + 50))
    screen.blit(score_text, score_rect)

if __name__ == "__main__":
    main()