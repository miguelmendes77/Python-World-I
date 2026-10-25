import pygame

pygame.init()
pygame.mixer.music.load('Nils Frahm - You.mp3')
pygame.mixer.music.play()
pygame.event.wait()