from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

r = 1
n = 100
R = 2


def f(u, v):
    theta = (u * 2 * math.pi) / (n - 1)
    phi = (v * 2 * math.pi) / (n - 1)
    x = (R + r * math.cos(theta)) * math.cos(phi)
    y = (R + r * math.cos(theta)) * math.sin(phi)
    z = r * math.sin(theta)
    return x, y, z


cores = [[1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]]


def desenhaTorus():
    for i in range(n):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n):
            glColor3fv(cores[(i + 1) % len(cores)])
            glVertex3fv(f(i, j))
            glVertex3fv(f(i + 1, j + 1))
        glEnd()


a = 0


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a, 0, 1, 0)
    desenhaTorus()
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
glutCreateWindow("Torus")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -8)
glutTimerFunc(50, timer, 1)
glutMainLoop()
