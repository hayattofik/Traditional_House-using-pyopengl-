from OpenGL.GL import *
from .base_furniture import BaseFurniture
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from ..scene import TextureLoader

default_color = (0.538, 0.411, 0.518)


def draw_cube(translate=None, scale=None, color=None):
    if color is None:
        color = default_color

    vertices = (
        (0, 0, 0),  # 0
        (1, 0, 0),  # 1
        (0, 1, 0),  # 2
        (1, 1, 0),  # 3

        (0, 0, -1),  # 4
        (1, 0, -1),  # 5
        (0, 1, -1),  # 6
        (1, 1, -1),  # 7
    )

    edges = (
        # front face
        (0, 1, 2),
        (1, 3, 2),
        # back face
        (4, 5, 6),
        (5, 7, 6),
        # left
        (4, 0, 6),
        (0, 2, 6),
        # right
        (1, 5, 7),
        (1, 7, 3),
        # up
        (2, 3, 6),
        (3, 7, 6),
        # down
        (0, 1, 4),
        (1, 5, 4)
    )

    normals = [
        (0, 0, 1),  # front face
        (0, 0, 1),  # front face
        (0, 0, -1),  # back face
        (0, 0, -1),  # back face
        (-1, 0, 0),  # left face
        (-1, 0, 0),  # left face
        (1, 0, 0),  # right face
        (1, 0, 0),  # right face
        (0, 1, 0),  # up face
        (0, 1, 0),  # up face
        (0, -1, 0),  # down face
        (0, -1, 0),  # down face
    ]

    glPushMatrix()

    if translate:
        glTranslatef(*translate)

    if scale:
        glScalef(*scale)

    glColor3f(*color)

    glBegin(GL_TRIANGLES)
    for (edge, normal) in zip(edges, normals):
        glNormal3d(*normal)
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

    glPopMatrix()


def draw_circle(texture,translate=None, radius=None, slices=None, stacks=None, color=None):
    if color is None:
        color = default_color

    sphere = gluNewQuadric()
    glBindTexture(GL_TEXTURE_2D, texture)
    glPushMatrix()
    glTranslatef(*translate)
    # glColor3f(*color)  # Put color
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    gluSphere(sphere, radius, slices, stacks)  # Draw sphere

    glPopMatrix()




class Armario(BaseFurniture):
    translate = [-3, -8, -35]
    scale = (0.5, 0.5, 0.5)
    rotate = (360, 0, 1, 0)

    def __init__(self, texture_loader: TextureLoader):
        super().__init__(texture_loader)

        self.texture = texture_loader.load_texture('grades.jpeg')
        self.btexture = texture_loader.load_texture('fanos.jpg')
    def draw_on_scene(self):
        glScalef(*self.scale)
        glTranslatef(*self.translate)
        glRotatef(*self.rotate)

        glBindTexture(GL_TEXTURE_2D, self.texture)
        draw_circle(self.btexture,translate=(3, 13, 2), radius=0.7, slices=100, stacks=10)
