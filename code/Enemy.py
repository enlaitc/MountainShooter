#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction = -1  # -1 para cima, 1 para baixo
        self.ySpeed = 1  # Velocidade no eixo y
    def move(self):
        if self.name == 'Enemy3':
            self.rect.centerx -= ENTITY_SPEED[self.name]
            self.rect.centery += self.ySpeed * self.direction

            # Verificar limites da tela
            if self.rect.centery <= 0:  # Se bater no topo
                self.rect.centery = 0
                self.direction = 1  # Mudar direção para baixo
                self.ySpeed += 1 # Aumenta a velocidade quando está caindo
            elif self.rect.centery >= WIN_HEIGHT:  # Se bater na borda inferior
                self.rect.centery = WIN_HEIGHT
                self.direction = -1  # Mudar direção para cima
                self.ySpeed -= 1 # Diminui a velocidade quando está subindo
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
