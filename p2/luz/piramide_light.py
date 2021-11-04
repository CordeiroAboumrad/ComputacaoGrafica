from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
from math import *
import sys
import numpy as np
from random import uniform
import math

n = 3
r = 3

base = []
vertices = []
faces = []
face_base = [abs((x + 1) - n) for x in range(n)]
cores = []

for angle in np.arange(0.0, 2 * math.pi, 2 * math.pi / n):
    x = math.cos(angle) * r
    y = math.sin(angle) * r
    vertices.append([x, y, 0])

vertice_topo = [0, 0, 3]
vertices.append(vertice_topo)

print(f'Vértices: {vertices}')

num_vertices = len(vertices)


for i in range(n):
    print(i)
    if i != n-1:
        faces.append([i, i + 1, n])
    else:
        faces.append([i, 0, i+1])

faces.append(face_base)

print(f'Faces: {faces}')

for j in range(n + 1):
    cores.append([uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)])

print(f'Cores: {cores}')


def Piramide():
    glBegin(GL_TRIANGLES)
    for face in faces:
        glNormal3fv(calculaNormalFace(face))
        for vertex in face:
            glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()


a = 0


def desenhaPiramide():
    glPushMatrix()
    glRotatef(-a, 1, 1, 1)
    Piramide()
    glPopMatrix()


def calculaNormalFace(face):
    x = 0
    y = 1
    z = 2
    if len(face) == 3:
        v0 = vertices[face[0]]
        v1 = vertices[face[1]]
        v2 = vertices[face[2]]

        U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
        V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
        N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
        NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
        return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)


    else:
        v0 = vertices[face[0]]
        v1 = vertices[face[1]]
        v2 = vertices[face[2]]

        v3 = vertices[face[2]]
        v4 =vertices[face[3]]
        v5 = vertices[face[0]]
    
        U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
        V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
        N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))

        U2= ( v5[x]-v3[x], v5[y]-v3[y], v5[z]-v3[z] )
        V2= ( v4[x]-v3[x], v4[y]-v3[y], v4[z]-v3[z] )
        N2= ( (U2[y]*V2[z]-U2[z]*V2[y]),(U2[z]*V2[x]-U2[x]*V2[z]),(U2[x]*V2[y]-U2[y]*V2[x]))

        NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
        
        NLength2 = sqrt(N2[x]*N2[x]+N2[y]*N2[y]+N2[z]*N2[z])
        
        return ( (N[x]/NLength + N2[x]/NLength2)/2, (N[y]/NLength + N2[y]/NLength2)/2, (N[z]/NLength + N2[z]/NLength2)/2)
    
    
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,3,2)
    desenhaPiramide()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Camera Virtual
    #          onde    Pra onde 
    gluLookAt( 10,2,2, 0,0,0,     0,1,0 )

def init():
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 1.0, 1.0, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (60,)
    light_position = (1, 1, 0)
    glClearColor(0.0,0.0,0.0,0.0)
#    glShadeModel(GL_FLAT)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Cubo")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()