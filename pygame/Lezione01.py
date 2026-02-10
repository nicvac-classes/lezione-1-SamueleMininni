import pygame
import pymunk
import pymunk.pygame_util
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test Pymunk - Fisica")
clock = pygame.time.Clock()

# Spazio fisico
space = pymunk.Space()
space.gravity = (0, 900)

# Pavimento
floor = pymunk.Segment(space.static_body, (0, 580), (800, 580), 5)
floor.elasticity = 1
floor.friction = 0.5
space.add(floor)

wall2 = pymunk.Segment(space.static_body, (0, 600), (0, 600), 5)
wall2.elasticity = 1
wall2.friction = 0.5
space.add(wall2)

wall = pymunk.Segment(space.static_body, (0, 400), (300, 500), 5)
wall.elasticity = 1
wall.friction = 0.5
space.add(wall)

# Funzione per creare una pallina
def create_ball(pos):
    mass = 1
    radius = 20
    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.9
    shape.friction = 0.5
    space.add(body, shape)
    return shape

balls = []

def create_ball(pos):
    mass = 1
    radius = random.randint(10, 40)                   # 🆕
    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.9
    shape.friction = 0.5
    space.add(body, shape)
    return shape
# Renderer
draw_options = pymunk.pygame_util.DrawOptions(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(create_ball(event.pos))

    screen.fill((30, 30, 50))
    space.debug_draw(draw_options)
    space.step(1/60)
    pygame.display.flip()
    clock.tick(60)
# Pavimento
floor = pymunk.Segment(space.static_body, (0, 580), (800, 580), 5)
floor.elasticity = 0.8
floor.friction = 0.5
space.add(floor)
                                                # 🆕
pygame.quit()
sys.exit()