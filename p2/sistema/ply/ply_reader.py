import OpenGL
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from read_ply import *
from random import randint
import numpy as np
from random import uniform



# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\033'

# Number of the glut window.
window = 0
look_at = 0

# Rotations
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0


object = int(input("What is the object? Type:\n0 - Cube\n1 - Plane\n"))

switcher={
    0: "C:/Users/VISAGIO/Documents/CEFET-RJ/Computação Gráfica/sistema/ply/cube.ply",
    1: "C:/Users/VISAGIO/Documents/CEFET-RJ/Computação Gráfica/sistema/ply/plane.ply",
}

switcher2 = {
    0: 10,
    1: 100
}

look_at = switcher2.get(object, 'Not valid option. Try again.')

text = switcher.get(object, 'Not valid option. Try again.')
# print(text)

vertices, faces = read_ply_xyz(text)

if object == 1:
    for vertice in vertices:
        vertice[0] = vertice[0] / 50
        vertice[1] = vertice[1] / 50
        vertice[2] = vertice[2] / 50


def desenhaObj():
    # glColor3f(randint(0,1), randint(0,1), randint(0,1))
    glColor3f(uniform(0.0, 1.0), uniform(0.0, 1.0), uniform(0.0, 1.0))
    # glColor3f(0, 0.5, 0.0)
    glBegin(GL_TRIANGLE_STRIP)
    for face in faces:
        for vertice in face:
            # glTexCoord2f((j + 1)/n, i/n)
            # glVertex3fv((vertice[0], vertice[1], vertice[2]))
            # print(vertice)
            glVertex3fv(vertices[vertice])
            # print(vertices[vertice])
    glEnd()



def desenha():

    glPushMatrix()
    
    # glBindTexture(GL_TEXTURE_2D, texture[2])
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(xrot, 0.0, 1.0, 0.5)

    desenhaObj()

    glPopMatrix()
    






def InitGL(Width, Height):             
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    # Camera Virtual     De onde  Pra onde
    gluLookAt( look_at,0,0,  0,0,0,  0,1,0 )

def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 2000.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture

    glMatrixMode(GL_MODELVIEW)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    desenha()

    xrot = xrot + 0.5
    yrot = yrot + 0.5
    zrot = zrot + 0.5


    glutSwapBuffers()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)    
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Object")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    InitGL(800, 600)
    glutMainLoop()


main()
