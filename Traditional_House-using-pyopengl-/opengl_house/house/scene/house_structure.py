from OpenGL.GL import *

from house.scene import TextureLoader

default_color = (1.0, 0.5, 0.31)
DEFAULT_WALL_HEIGHT = 8
DEFAULT_WALL_THICKNESS = 0.9


def draw_cube(translate=None, scale=None, color=None, rotate=None):
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

    if rotate:
        glRotatef(*rotate)

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


def inside_walls():
    draw_cube(translate=(5, 0, -8), scale=(13, DEFAULT_WALL_HEIGHT, DEFAULT_WALL_THICKNESS))


def draw_walls(ground_texture):
    # front walls
    glBindTexture(GL_TEXTURE_2D, ground_texture)
    draw_cube(translate=(5, 0, 0), scale=(13, DEFAULT_WALL_HEIGHT, DEFAULT_WALL_THICKNESS))
    glBindTexture(GL_TEXTURE_2D, ground_texture)
    draw_cube(translate=(1, 6, 0), scale=(4, 2, DEFAULT_WALL_THICKNESS))
    glBindTexture(GL_TEXTURE_2D, ground_texture)
    draw_cube(translate=(-5, 0, 0), scale=(6, DEFAULT_WALL_HEIGHT, DEFAULT_WALL_THICKNESS))
    # left walls
    glBindTexture(GL_TEXTURE_2D, ground_texture)
    draw_cube(translate=(-4.8, 0, -.1), scale=(4, DEFAULT_WALL_HEIGHT, DEFAULT_WALL_THICKNESS), rotate=(90, 0, 1, 0))
    draw_cube(translate=(-6.8, 0, -4), scale=(2, DEFAULT_WALL_HEIGHT, DEFAULT_WALL_THICKNESS))
    draw_cube(translate=(-6.8, 0, -4), scale=(15, DEFAULT_WALL_HEIGHT, DEFAULT_WALL_THICKNESS), rotate=(90, 0, 1, 0))
    # back wall

    glBindTexture(GL_TEXTURE_2D,ground_texture)
    draw_cube(translate=(-6.8, 0, -18.8), scale=(25, DEFAULT_WALL_HEIGHT, DEFAULT_WALL_THICKNESS))
    # right wall
    glBindTexture(GL_TEXTURE_2D, ground_texture)
    draw_cube(translate=(18, 0, 0), scale=(19, DEFAULT_WALL_HEIGHT, DEFAULT_WALL_THICKNESS), rotate=(90, 0, 1, 0))



class HouseStructure:
    def __init__(self, texture_loader: TextureLoader):
        self.texture_loader = texture_loader
        self.ground_texture = self.texture_loader.load_texture('ground_texture.jpg')
        self.wall_texture = self.texture_loader.load_texture('pe-fogao.jpg')

    def draw_structure(self):
        glPushMatrix()
        glTranslatef(0, -4, 0)

        draw_walls(self.wall_texture)
        glPopMatrix()
