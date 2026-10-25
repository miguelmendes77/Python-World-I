import pygame

pygame.init()
arquivo = input('Digite o caminho do arquivo de áudio (.mp3): ')
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()
pygame.event.wait()
