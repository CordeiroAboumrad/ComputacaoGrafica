from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import numpy as np
from random import uniform

n = 20
r = 3

base = []
vertices = []
faces = []
face_base = [x for x in range(n)]
linhas = []
cores = []

for angle in np.arange(0.0, 2 * math.pi, 2 * math.pi / n):
    x = math.cos(angle) * r
    y = math.sin(angle) * r
    vertices.append([x, y, 0])

vertice_topo = [0, 0, 3]
vertices.append(vertice_topo)

print(f'Vértices: {vertices}')

num_vertices = len(vertices)
for linha in range(len(vertices) - 1):
    if linha == 0:
        linhas.append([linha, len(vertices) - 2])
    else:
        linhas.append([linha, linha - 1])

    if linha == len(vertices) - 2:
        linhas.append([linha, 0])
    else:
        linhas.append([linha, linha + 1])

    linhas.append([linha, len(vertices) - 1])

for i in range(n):
    if i != 7:
        faces.append([i, i + 1, n])
    else:
        faces.append([7, 0, 8])

faces.append(face_base)

print(f'Linhas: {linhas}')
print(f'Faces: {faces}')

for j in range(n + 1):
    cores.append([uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)])

print(f'Cores: {cores}')


def Prisma():
    glBegin(GL_POLYGON)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        for vertex in face:
            glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i + 1
    glEnd()

    glColor3f(0, 0.5, 0)
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()


a = 0


def desenhaPrisma():
    # Prisma
    glPushMatrix()
    # glTranslatef(-2, 0, 0)
    glRotatef(-a, 1, 1, 1)
    Prisma()
    glPopMatrix()


def desenhaUmCubo():
    glPushMatrix()
    glTranslatef(-2, 0, 0)
    glRotatef(-a, 0, 0, 1)
    Prisma()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    # glTranslatef(0, -2, 0)
    desenhaPrisma()
    glPopMatrix()
    glPushMatrix()
    # glTranslatef(0, 2, 0)
    # desenhaDoisCubos()
    glPopMatrix()
    glutSwapBuffers()
    a += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


# def mouse(botao, estado, x, y):
#     print(botao, estado, x, y)


# def mouseMove(x, y):
#     print("-->", x, y)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Prisma")
glutDisplayFunc(desenha)
# glutMotionFunc(mouseMove)
# glutPassiveMotionFunc(mouseMove)
# glutMouseFunc(mouse)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -20)
glutTimerFunc(50, timer, 1)
glutMainLoop()
