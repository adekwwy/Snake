import pygame
import random
import time
from Jablko import Jablko

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

#stworzenie tła
tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

#25x19
for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("images/background.png")
        maska = (random.randrange(0,20), random.randrange(0,20), random.randrange(0,20))
        
        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i*32, j*32))

#ustawienia
pygame.init()
#obiekt ekranu i zegara
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

#jablko
jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)

gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    #rysowanie tła
    ekran.blit(tlo, (0, 0))
    
    #eysowane jabłek
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)

    #wyczyszczenie ekranu
    pygame.display.flip()
    #ustawienie stałego 30 FPS
    zegar.tick(30)

#opóźnienie 3 sekund
time.sleep(3)
#zamknięcie aplikacji
pygame.quit()
