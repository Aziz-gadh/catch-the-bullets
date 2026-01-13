import pygame as pg
from math import sin, cos, pi
from random import uniform
pg.init()
font = pg.font.SysFont('Arial', 80)
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
arrow=pg.Rect(20,200,20,20)
n,m=10,5
abs_vel1=7
abs_vel2=7
good_ball=[]
bad_ball=[]
x=uniform(0,2*pi)
for i in range(n):
    good_ball.append((pg.Rect(393,293,14,14),[abs_vel1*cos(2*pi*(i+1)/(m+n)+x),abs_vel1*sin(2*pi*(i+1)/(m+n+1)+x)]))
for i in range(m):
    bad_ball.append((pg.Rect(393,293,14,14),[abs_vel2*cos(2*pi*(i+n+1)/(m+n)+x),abs_vel2*sin(2*pi*(i+n+1)/(m+n+1)+x)]))
running = True
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
            running = False
    keys=pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        arrow.x-=7
    if keys[pg.K_RIGHT]:
        arrow.x+=7
    if keys[pg.K_UP]:
        arrow.y-=7
    if keys[pg.K_DOWN]:
        arrow.y+=7
    arrow.clamp_ip(screen.get_rect())
    for ball in good_ball:
        ball[0].x+=ball[1][0]
        ball[0].y+=ball[1][1]
        if ball[0].left <= 0 or ball[0].right >= 800:
            ball[1][0] *= -1
        if ball[0].top <= 0 or ball[0].bottom >= 600:
            ball[1][1] *= -1
        if ball[0].colliderect(arrow):
            good_ball.remove(ball)
            n-=1
    for ball in bad_ball:
        ball[0].x+=ball[1][0]
        ball[0].y+=ball[1][1]
        if ball[0].left <= 0 or ball[0].right >= 800:
            ball[1][0] *= -1
        if ball[0].top <= 0 or ball[0].bottom >= 600:
            ball[1][1] *= -1
        if ball[0].colliderect(arrow):
            running = False
            text = font.render("GAME OVER", True, (255, 0, 0))
    if n==0 :
        running = False
        text=font.render("YOU WON!!", True, (0,255,0))
    screen.fill((0,0,0))
    pg.draw.rect(screen, (0,0,255), arrow)
    for i in range(n):
        pg.draw.ellipse(screen, (0, 255, 0), good_ball[i][0])
    for i in range(m):
        pg.draw.ellipse(screen, (255, 0, 0), bad_ball[i][0])
    if not running:
        text_rect = text.get_rect()
        text_rect.topleft=(200,280)
        screen.blit(text, text_rect)
    pg.display.flip()
pg.quit()