import pygame
import sys
import time
import random

# 初始化
pygame.init()

# 设置窗口
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('乒乓球')

# 自定义颜色
black = (0, 0, 0)
white = (255, 255, 255)

# 球拍设定
paddle_width, paddle_height = 20, 200
paddle_speed = 14

# 球的设定
ball_size = 30
ball_speed_x, ball_speed_y = 5, 5

# 设置球和拍
left_paddle = pygame.Rect(10, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 30, height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)

# 分数
left_score = 0
right_score = 0

# 字体
font = pygame.font.SysFont(None, 36)

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取按键
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < height:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < height:
        right_paddle.y += paddle_speed

    # 移动球
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 球到顶或底
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y = -ball_speed_y

    # 球碰到球拍
    if ball.colliderect(left_paddle):
        ball_speed_x = -ball_speed_x
        ball_speed_x *= 1.01  # 增加球的速度
        ball_speed_y *= 1.01
        left_score += 1
    if ball.colliderect(right_paddle):
        ball_speed_x = -ball_speed_x
        ball_speed_x *= 1.01  # 增加球的速度
        ball_speed_y *= 1.01
        right_score += 1

    # 球飞出边界
    if ball.left <= 0:
        ball.x, ball.y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
        ball_speed_x, ball_speed_y = 5, 5
        time.sleep(1)
        left_score -= 1
    if ball.right >= width:
        ball.x, ball.y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
        ball_speed_x, ball_speed_y = -5, 5
        time.sleep(1)
        right_score -= 1

    # 填充背景
    window.fill(black)

    # 渲染控件
    pygame.draw.rect(window, white, left_paddle)
    pygame.draw.rect(window, white, right_paddle)
    pygame.draw.ellipse(window, white, ball)

    # 显示分数
    left_text = font.render(f'Score: {left_score}', True, white)
    right_text = font.render(f'Score: {right_score}', True, white)
    window.blit(left_text, (50, 20))
    window.blit(right_text, (width - 150, 20))

    # 更新窗口
    pygame.display.flip()

    # 设置帧率
    pygame.time.Clock().tick(60)