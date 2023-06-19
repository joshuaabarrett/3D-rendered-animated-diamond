import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (0, 3, 0),
    (1, 1, 1),
    (-1, 1, 1),
    (1, 1, -1),
    (-1, 1, -1),
    (0, -1, 0)
)

edges = (
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 3),
    (4, 2),
    (4, 3),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4)
)


def tri ():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(50, display[0] / display[1], .01, 50.0)
    glTranslate(0.0, -1.5, -8)
    glRotate(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotate(.5, 0, .3, .1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        tri()
        pygame.display.flip()
        pygame.time.wait(10)

main()
