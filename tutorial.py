from main import eval_genomes
import pygame
from pong import Game
import neat
import os

#Sizing for the window
width, height = 700, 500
window = pygame.display.set_mode((width, height))

class PongGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball


    def test_ai(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left = True, up = True)
            if keys[pygame.K_s]:
                self.game.move_paddle(left = True, down = True)

            game_info = self.game.loop()
            print(game_info.left_score, game_info.right_score)
            self.game.draw(False, True)
            pygame.display.update()

        pygame.quit()

def eval_genomes(genomes, config):
    pass

def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-5')
    p = neat.Population(config) #Comment out this one if you want to restore
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))


    p.run(eval_genomes,50)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        config_path)

    