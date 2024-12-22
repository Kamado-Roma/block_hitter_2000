import pygame
import math
from paddle import*

class Ball:

    def __init__(self, window, x, y, image):
        self.window = window
        self.image = image
        self.ball_rect = self.image.get_rect(x = x, y = y)

        self.velocity = 500
        self.angle = math.pi / 4

        self.v_x = self.velocity * math.cos(self.angle)
        self.v_y = self.velocity * math.sin(self.angle)

    def draw(self):
        self.window.blit(self.image, (self.ball_rect.x, self.ball_rect.y))
        
    def move(self, dt, paddle):
        self.bound_checker(paddle)
        self.ball_rect.x += self.v_x * dt
        self.ball_rect.y += self.v_y * dt

    def bound_checker(self, paddle):

        if self.ball_rect.colliderect(paddle.paddle_rect):
            self.ball_rect.bottom = paddle.paddle_rect.top
            self.v_y *= -1
        #if self.ball_rect.y >= self.window.get_height() - self.ball_rect.h:
           # self.v_y *= -1
        if self.ball_rect.x >= self.window.get_width() - self.ball_rect.w:
            self.v_x *= -1
        if self.ball_rect.y <= 0:
            self.v_y *= -1
        if self.ball_rect.x <= 0:
            self.v_x *= -1