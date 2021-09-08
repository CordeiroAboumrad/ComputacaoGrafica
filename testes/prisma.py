from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

n = 4
r = 3

x = math.cos(2 * math.pi / n) * r
y = math.sin(2 * math.pi / n) * r

vertices = (
    (1, 0, 1),
    (-1, 0, 1),
    (-1, 0, -1),
    (1, 0, -1),
    (0, 2, 0)
)

linhas = (
    (0, 1),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 4),
    (2, 3),
    (2, 4),
    (3, 4)
)

faces = (
    (0, 1, 4),
    (0, 3, 4),
    (3, 2, 4),
    (1, 2, 4),
    (0, 1, 2, 3)
)

base = (
    (0, 1, 2, 3)
)

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1))


def Prisma():
    glBegin(GL_QUADS)
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


def mouse(botao, estado, x, y):
    print(botao, estado, x, y)


def mouseMove(x, y):
    print("-->", x, y)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Prisma")
glutDisplayFunc(desenha)
# glutMotionFunc(mouseMove)
glutPassiveMotionFunc(mouseMove)
glutMouseFunc(mouse)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -20)
glutTimerFunc(50, timer, 1)
glutMainLoop()
