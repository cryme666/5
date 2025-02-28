import pygame
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")
background_color = (0, 0, 0)
paddle_width = 20
paddle_height = 100
paddle_color = (255, 255, 255)

paddle1_x = 30
paddle1_y = (height - paddle_height) // 2

paddle2_x = width - 50
paddle2_y = (height - paddle_height) // 2

ball_radius = 10
ball_color = (255, 255, 255)
ball_x = width // 2
ball_y = height // 2

paddle_speed = 7
ball_speed_x, ball_speed_y = 5, 5

paddle1 = pygame.Rect(paddle1_x,paddle1_y,paddle_width,paddle_height)
paddle2 = pygame.Rect(paddle2_x,paddle2_y,paddle_width,paddle_height)

score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

game_state = "start" 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = width // 2
    ball_y = height // 2
    ball_speed_x *= -1

def reset_game():
    reset_ball()
    global paddle1_x, paddle1_y,paddle2_x,paddle2_y,paddle1,paddle2

    paddle1_x = 30
    paddle1_y = (height - paddle_height) // 2

    paddle2_x = width - 50
    paddle2_y = (height - paddle_height) // 2

    paddle1 = pygame.Rect(paddle1_x,paddle1_y,paddle_width,paddle_height)
    paddle2 = pygame.Rect(paddle2_x,paddle2_y,paddle_width,paddle_height)



def check_win():
    global game_state
    if score1 >= 5:
        game_state = "game_over"
        return "Player 1"
    elif score2 >= 5:
        game_state = "game_over"
        return "Player 2"

start_button = pygame.Rect(width // 2 - 50, height // 2 - 25, 100, 50)
new_game_button = pygame.Rect(width // 2 - 75, height // 2 + 30, 150, 50)

running = True
while running:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state == "start" and event.type == pygame.MOUSEBUTTONDOWN  and start_button.collidepoint(event.pos):
                game_state = "playing"
        if game_state == "game_over" and event.type == pygame.MOUSEBUTTONDOWN  and new_game_button.collidepoint(event.pos):
                game_state = "playing"
                reset_game()
                score1, score2 = 0,0

    if game_state == "start":
        screen.fill(background_color)
        draw_text("Ping Pong", font, (255, 255, 255), screen, width // 2 - 57, height // 2 - 100)
        pygame.draw.rect(screen, (255, 255, 255), start_button)
        draw_text("Start", font, (0, 0, 0), screen, width // 2 - 27, height // 2 - 15)
        pygame.display.flip()
        continue

    if game_state == "playing":
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_w] and paddle1.top > 0:
            paddle1.move_ip(0, -paddle_speed)
        if key_pressed[pygame.K_s] and paddle1.bottom < height:
            paddle1.move_ip(0, paddle_speed)
        if key_pressed[pygame.K_UP] and paddle2.top > 0:
            paddle2.move_ip(0, -paddle_speed)
        if key_pressed[pygame.K_DOWN] and paddle2.bottom < height:
            paddle2.move_ip(0, paddle_speed)
        # if key_pressed[pygame.K_q]:
        #     game_state = 'game_over'
        #     winner = "Player 1"

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
            ball_speed_y *= -1

        if ball_x - ball_radius <= 0:
            score2 += 1
            reset_ball()
        elif ball_x + ball_radius >= width:
            score1 += 1
            reset_ball()

        if paddle1.collidepoint(ball_x - ball_radius, ball_y) or paddle1.collidepoint(ball_x + ball_radius, ball_y):
            ball_speed_x *= -1
        if paddle2.collidepoint(ball_x - ball_radius, ball_y) or paddle2.collidepoint(ball_x + ball_radius, ball_y):
            ball_speed_x *= -1

        screen.fill(background_color)
        
        pygame.draw.rect(screen, paddle_color, paddle1)
        pygame.draw.rect(screen, paddle_color, paddle2)
        pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
        draw_text(f"Player 1: {score1}", font, (255, 255, 255), screen, 50, 10)
        draw_text(f"Player 2: {score2}", font, (255, 255, 255), screen, width - 150, 10)

        winner = check_win()
        if winner:
            game_state = "game_over"

        pygame.display.flip()

    if game_state == "game_over":
        screen.fill(background_color)
        draw_text(f"{winner} wins!", font, (255, 255, 255), screen, width // 2 - 80, height // 2 - 50)
        draw_text(f"Player 1: {score1}", font, (255, 255, 255), screen, 50, 10)
        draw_text(f"Player 2: {score2}", font, (255, 255, 255), screen, width - 150, 10)
        pygame.draw.rect(screen, (255, 255, 255), new_game_button)
        draw_text("New Game", font, (0, 0, 0), screen, width // 2 - 60, height // 2 + 43)    
        pygame.display.flip()

pygame.quit()
