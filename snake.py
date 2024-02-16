# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:24:46 2024
Snake Game
@author: Ayden
"""

import pygame
from pygame.math import Vector2
import sys, random

class SNAKE:
    def __init__(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = Vector2(1,0)
        self.length = 3
        #up,down,right,left
        
    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (38,181,255), block_rect)
    
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, self.body[0] + self.direction)
        #removes last element and adds new head position
        self.body = body_copy[:]
        
    def add_block(self):
        self.body.insert(self.length,self.body[self.length-1])
        self.length+=1       
class FRUIT:
    def __init__(self):
        self.x = random.randint(0,num_cells-1)
        self.y = random.randint(0,num_cells-1)
        self.pos = Vector2(self.x,self.y)
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(255,0,0),fruit_rect)
        
    def move(self):
        self.x = random.randint(0,num_cells-1)
        self.y = random.randint(0,num_cells-1)
        self.pos = Vector2(self.x,self.y)       
class MAIN:

    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.move()
            self.snake.add_block()
        
            
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < num_cells or not 0 <= self.snake.body[0].y <= num_cells:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
    def game_over(self):
        pygame.quit()
        sys.exit()
            
    def draw_grass(self):
        grass_color = (121, 219, 0)#(167,209,61)
        for col in range(num_cells):
            for row in range(num_cells):
                if ((col + row) % 2 == 0):
                    grass_rect = pygame.Rect(col*cell_size, row*cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)
            
    def draw_score(self):
        score_text = self.snake.length - 3
        score_surface = game_font.render(f'Score: {score_text}',True,(56,74,12))
        score_rect = score_surface.get_rect(center = (cell_size * num_cells -60, cell_size * num_cells -60))
        
        screen.blit(score_surface, score_rect) 
        
pygame.init()
num_cells = 20
cell_size = 40
screen = pygame.display.set_mode((num_cells * cell_size, num_cells * cell_size))
clock = pygame.time.Clock()
snake_head = pygame.image.load('Graphics/snake.png').convert_alpha()
game_font = pygame.font.Font(None,25)
#('Fonts/PortsonOne-Regular.ttf, font_size)
fruit = FRUIT()
snake = SNAKE()
    
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150) #150 ms

main_game = MAIN()
while True:
    #draws elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
    screen.fill((159, 240, 60))
    
    main_game.draw_elements();
    pygame.display.update()
    #runs at 60 frames per second
    clock.tick(60)
