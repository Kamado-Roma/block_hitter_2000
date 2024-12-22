import pygame

class Paddle():

    def __init__(self, window, x, y, image):
        self.window = window
        self.image = image
        self.paddle_rect = self.image.get_rect(x=x, y=y)

        self.velocity = 700

    def draw(self):
        self.window.blit(self.image, (self.paddle_rect.x, self.paddle_rect.y))
        self.check_bound()

    def move(self, dt):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            self.paddle_rect.x -= self.velocity * dt
        if pressed[pygame.K_d]:
            self.paddle_rect.x += self.velocity * dt

    def check_bound(self):
        if self.paddle_rect.x < 0:
            self.paddle_rect.x = 0

        if self.paddle_rect.x > self.window.get_width() - self.paddle_rect.w:
            self.paddle_rect.x = self.window.get_width() - self.paddle_rect.w
