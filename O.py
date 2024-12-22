import pygame
from paddle import *
from ball import *
from block import *

class Game():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.bg = pygame.image.load("resource-main/images/bg.jpeg")
        self.bg = pygame.transform.scale(self.bg, (800, 600))

        #paddle
        self.paddle_img = pygame.image.load('resource-main/images/paddle.png')
        self.paddle_img = pygame.transform.scale_by(self.paddle_img, 2)
        self.paddle = Paddle(self.window, 450, 500, self.paddle_img)

        #Ball
        self.ball_img = pygame.image.load("resource-main/images/ball.png")
        self.ball_img = pygame.transform.scale_by(self.ball_img, 2)
        self.ball = Ball(self.window, 250, 350 , self.ball_img)

        #block
        self.block_img = pygame.image.load("resource-main/images/pink_block.png")
        self.block_img = pygame.transform.scale_by(self.block_img, 2)

        self.block = list()

        for y in self.y_pos():
            for x in self.x_pos():
                self.block.append(Block(self.window, x, y, self.block_img))

        #delta
        self.clock = pygame.time.Clock()

    def x_pos(self):
        w = self.block_img.get_width()
        gap = 20
        total = self.window.get_width() // (w + gap)
        lst = list()

        for i in range(total):
            lst.append(gap + (w + gap) * i)

        return lst

    def destroy(self):
        for block in self.block:
            if self.ball.ball_rect.colliderect(block.block_rect):
                self.block.remove(block)
                self.ball.v_y *= -1

    def y_pos(self):
        y= self.block_img.get_height()
        gap = 10
        lst = list()

        for i in range(4):
            lst.append(gap + (y + gap) * i)

        return lst

    def run(self):
        running = True
        while running:
            #delta time
            self.delta_time = self.clock.tick(120) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running =False

            #render
            self.window.blit(self.bg, (0, 0))
            self.paddle.draw()
            self.paddle.move(self.delta_time)
            self.ball.draw()
            self.ball.move(self.delta_time,self.paddle)

            for block in self.block:
                block.draw()

            self.destroy()
            pygame.display.update()
        pygame.quit()

game = Game()
game.run()
