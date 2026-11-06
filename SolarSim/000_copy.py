# -*- coding: utf-8 -*-
import pygame
import random
pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 1800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("예술은 폭☆8이다 갈")

#이벤트 루프 - 종료까지 대기
running = True # 실행 중인지 확인
while running: # 반복
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#종료 처리
pygame.quit()