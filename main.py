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
ball_speed_x, ball_speed_y = 5,5

paddle1 = pygame.Rect(paddle1_x,paddle1_y,paddle_width,paddle_height)
paddle2 = pygame.Rect(paddle2_x,paddle2_y,paddle_width,paddle_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_w] and paddle1.top > 0:
        paddle1.move_ip(0,-paddle_speed)

    if key_pressed[pygame.K_s] and paddle1.bottom < height:
        paddle1.move_ip(0,paddle_speed)

    #! прописати рух другого гравця

    
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    

    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_speed_y *= -1

    screen.fill(background_color)

    if paddle1.collidepoint(ball_x - ball_radius,ball_y) or paddle1.collidepoint(ball_x + ball_radius,ball_y):
        ball_speed_x *= -1

    pygame.draw.rect(screen,paddle_color,paddle1)
    pygame.draw.rect(screen,paddle_color,paddle2)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    
    pygame.display.flip()

    pygame.time.Clock().tick(60)
pygame.quit()

