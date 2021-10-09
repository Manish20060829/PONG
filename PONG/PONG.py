import pygame
from pygame.constants import K_SPACE
pygame.init()

WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


WINNER_FONT = pygame.font.SysFont('comicsans', 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 100
BALL_WIDTH, BALL_HEIGHT = 20, 20
BALL_XSPEED, BALL_YSPEED = 8, 7

PLAYER1 = pygame.image.load("white.png")
PLAYER1_TRANSFORM = pygame.transform.scale(
    PLAYER1, (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER2 = pygame.image.load("white.png")
PLAYER2_TRANSFORM = pygame.transform.scale(
    PLAYER2, (PLAYER_WIDTH, PLAYER_HEIGHT))
BALL = pygame.image.load("ball.png")
BALL_TRANSFORM = pygame.transform.scale(BALL, (BALL_WIDTH, BALL_HEIGHT))

FPS = 60
VEL = 25


WINNER_FONT = pygame.font.SysFont('comicsans', 30)
FONT = pygame.font.SysFont('comicsans', 70)
PLAY_FONT = pygame.font.SysFont('comicsans', 100)


def p1_winner():
    p1winner = WINNER_FONT.render(F"Player 1 Won", False, WHITE)
    SCREEN.blit(p1winner, (200, 400))
    pygame.display.update()
    pygame.time.delay(2500)


def p2_winner():
    p2winner = WINNER_FONT.render(F"Player 2 Won", False, WHITE)
    SCREEN.blit(p2winner, (450, 400))
    pygame.display.update()
    pygame.time.delay(2500)


def score():
    global Player1score, Player2score
    score1_text = FONT.render(f"{Player1score}", False, WHITE)
    score2_text = FONT.render(f"{Player2score}", False, WHITE)
    SCREEN.blit(score1_text, (310, 0))
    SCREEN.blit(score2_text, (450, 0))


def ball_collision(Ball, Playerone, Playertwo):
    global Player1score, Player2score
    global BALL_XSPEED, BALL_YSPEED
    Ball.x += BALL_XSPEED
    Ball.y += BALL_YSPEED
    # collision with borders
    if Ball.right >= WIDTH:
        Ball.x, Ball.y = 380, 340
        Player1score += 1
    if Ball.left <= 0:
        Ball.x, Ball.y = 380, 340
        Player2score += 1
    if Ball.bottom >= HEIGHT:
        BALL_YSPEED *= -1
    if Ball.top <= 0:
        BALL_YSPEED *= -1

    # collison with rectangle
    collision_tolerence = 15
    if Ball.colliderect(Playerone):
        if abs(Ball.right - Playerone.left) < collision_tolerence and BALL_XSPEED > 0:
            BALL_XSPEED *= -1
        if abs(Ball.left - Playerone.right) < collision_tolerence and BALL_XSPEED < 0:
            BALL_XSPEED *= -1
        if abs(Ball.top - Playerone.bottom) < collision_tolerence and BALL_YSPEED < 0:
            BALL_YSPEED *= -1
        if abs(Ball.bottom - Playerone.top) < collision_tolerence and BALL_YSPEED > 0:
            BALL_YSPEED *= -1
    if Ball.colliderect(Playertwo):
        if abs(Ball.right - Playertwo.left) < collision_tolerence and BALL_XSPEED > 0:
            BALL_XSPEED *= -1
        if abs(Ball.left - Playertwo.right) < collision_tolerence and BALL_XSPEED < 0:
            BALL_XSPEED *= -1
        if abs(Ball.top - Playertwo.bottom) < collision_tolerence and BALL_YSPEED < 0:
            BALL_YSPEED *= -1
        if abs(Ball.bottom - Playertwo.top) < collision_tolerence and BALL_YSPEED > 0:
            BALL_YSPEED *= -1


def player1_movement(Playerone, keys_pressed):
    if keys_pressed[pygame.K_UP] and Playerone.y > 0:
        Playerone.y -= VEL
    if keys_pressed[pygame.K_DOWN] and Playerone.y < 800 - PLAYER_HEIGHT:
        Playerone.y += VEL


def player2_movement(Playertwo, keys_pressed):
    if keys_pressed[pygame.K_w] and Playertwo.y > 0:
        Playertwo.y -= VEL
    if keys_pressed[pygame.K_s] and Playertwo.y < 800 - PLAYER_HEIGHT:
        Playertwo.y += VEL


def drawwindow(Playerone, Playertwo, Ball):
    SCREEN.blit(PLAYER1_TRANSFORM, (Playerone.x, Playerone.y))
    SCREEN.blit(PLAYER2_TRANSFORM, (Playertwo.x, Playertwo.y))
    SCREEN.blit(BALL_TRANSFORM, (Ball.x, Ball.y))
    pygame.draw.rect(SCREEN, WHITE, (390, 0, 20, HEIGHT))


def main_menu():
    clock1 = pygame.time.Clock()
    run = True
    while run:
        clock1.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        SCREEN.fill(BLACK)
        pressspace = PLAY_FONT.render("Press SPACE to play", False, WHITE)
        SCREEN.blit(pressspace, (65, 350))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            main()

        pygame.display.update()


def main():
    global Player1score, Player2score
    Player1score = 0
    Player2score = 0
    Ball = pygame.Rect(380, 340, BALL_WIDTH, BALL_HEIGHT)
    Playerone = pygame.Rect(730, 300, PLAYER_WIDTH, PLAYER_HEIGHT)
    Playertwo = pygame.Rect(50, 300, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()

        SCREEN.fill(BLACK)

        player1_movement(Playerone, keys_pressed)
        player2_movement(Playertwo, keys_pressed)
        drawwindow(Playerone, Playertwo, Ball)
        ball_collision(Ball, Playerone, Playertwo)
        score()

        if Player1score == 10:
            p1_winner()
            main_menu()

        if Player2score == 10:
            p2_winner()
            main_menu()

        pygame.display.update()


if __name__ == '__main__':
    main_menu()
