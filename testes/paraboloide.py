from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

r = 1
n = 100
halfpi = math.pi / 2


def f(i, j):
    theta = (j * 2 * math.pi) / (n - 1)  # Varia de 0 a 2 * PI
    w = (i * 1) / (n - 1)  # Varia de 0 a 1
    x = w * math.cos(theta)
    y = w ** 2
    z = w * math.sin(theta)
    return x, y, z


cores = [[1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]]


def desenhaParaboloide():
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(n):
        for j in range(n):
            glVertex3fv(f(i, j))
            glVertex3fv(f(i+1, j+1))
            glColor3fv(cores[(i + 1) % len(cores)])
    glEnd()


a = 0


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a, 1, 1, 1)
    desenhaParaboloide()
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
