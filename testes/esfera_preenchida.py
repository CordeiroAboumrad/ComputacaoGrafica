from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
from random import randint

r = 1
n = 200
halfpi = math.pi / 2


def f(u, v):
    theta = (u * math.pi / (n - 1)) - halfpi
    phi = (v * 2 * math.pi) / (n - 1)
    x = r * math.cos(theta) * math.cos(phi)
    y = r * math.sin(theta)
    z = r * math.cos(theta) * math.sin(phi)
    return x, y, z


cores = [[1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]]


def desenhaEsfera():
    glBegin(GL_POLYGON)
    for i in range(n):
        for j in range(n):
            glColor3fv(cores[(i + 1) % len(cores)])
            glVertex3fv(f(j, i))
    glEnd()


a = 0


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a, 0, 2, 0)
    desenhaEsfera()
    glPopMatrix()
    glutSwapBuffers()
    a += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Esfera")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -8)
glutTimerFunc(50, timer, 1)
glutMainLoop()
