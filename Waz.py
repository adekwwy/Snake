import pygame
from pygame.sprite import _Group
from Kierunek import Kierunek

class Waz(pygame.sprite.Sprite):
    def __init__(self):
        #oryginalny obraz głowy
        self.orginalny_obraz = pygame.image.load("images/head.png")
        #obraz pomocniczy, będzie się on zmieniał przy zmianie kierunku gracza
        self.obraz = pygame.transform.rotate(self.orginalny_obraz, 0)
        #współrzędnie głowy
        self.rect = self.obraz.get_rect(center=(12*32+16, 9*32+16))