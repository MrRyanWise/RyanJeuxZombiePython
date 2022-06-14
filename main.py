# Press Maj+F10 to execute it or replace it with your code.
import pygame
import math
from game import Game

pygame.init()  # Initialisation du jeu

# definir une clock
clock = pygame.time.Clock()
FPS = 60

# generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")  # titre du jeu
screen = pygame.display.set_mode((1080, 720))  # genère la fenetre

# importer le  fond d'ecran
background = pygame.image.load('Assets/bg.jpg')

# importer la bannière
banner = pygame.image.load('Assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# import charger notre bouton pour lacer la partie
play_button = pygame.image.load('Assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger notre jeu
game = Game()
running = True

# boucle tant que cette condition est vrai

while running:
    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, -200))

    # verifier si notre jeu a commencé
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre à jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            # quelle touche a été utilisée
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en mode lancé
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le boutton
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancé
                game.start()
                # jouer le son
                game.sound_manager.play('click')

    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)
