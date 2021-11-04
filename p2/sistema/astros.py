import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png
import math
import pyautogui

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\033'

# Number of the glut window.
window = 0

# Rotations
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0


r_sol = 8
r_terra = 4
r_lua = 1

n = 50
halfpi = math.pi/2

x0 = 0
xn = 1

y0 = 0
yn = 1

dx2 = (xn - x0)/n
dy2 = (yn - y0)/n

def f(u, v, r):
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x, y, z


def f2(u, v, r2):
    theta = (u*math.pi/(n-1))-halfpi
    phi = (v*2*math.pi)/(n-1)
    x = r2 * math.cos(theta)*math.cos(phi)
    y = r2 * math.sin(theta)
    z = r2 * math.cos(theta)*math.sin(phi)
    return x, y, z


def desenhaEsfera(r):
    for j in range(n):
        glBegin(GL_TRIANGLE_STRIP)
        for i in range(n):
                glTexCoord2f((j + 1)/n, i/n); glVertex3fv(f2(i, j + 1, r))
                glTexCoord2f(j/n, i/n); glVertex3fv(f(i, j, r))
        glEnd()



def desenhaSol():

    glPushMatrix()

    glBindTexture(GL_TEXTURE_2D, texture[1])
    glRotatef(xrot, 0.0, 1.0, 0.0)

    desenhaEsfera(r_sol)

    desenhaTerra()

    glPopMatrix()



def desenhaTerra():

    glPushMatrix()

    glBindTexture(GL_TEXTURE_2D, texture[0])
    glTranslatef(0.0, 0.0, 40.0)
    glRotatef(xrot * 2, 0.0, 1.0, 0.0)

    desenhaEsfera(r_terra)

    desenhaLua()

    glPopMatrix()



def desenhaLua():

    glPushMatrix()
    
    glBindTexture(GL_TEXTURE_2D, texture[2])
    glTranslatef(0.0, 0.0, 10.0)
    glRotatef(xrot * 2, 0.0, 1.0, 0.0)

    desenhaEsfera(r_lua)

    glPopMatrix()
    





def LoadTextures():
    global texture
    texture = [ glGenTextures(1), glGenTextures(1), glGenTextures(1) ]

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='mapa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
    ################################################################################

    glBindTexture(GL_TEXTURE_2D, texture[1])
    reader = png.Reader(filename='sol.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


    #################################################################################
    
    glBindTexture(GL_TEXTURE_2D, texture[2])
    reader = png.Reader(filename='lua.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def InitGL(Width, Height):             
    LoadTextures()
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
    gluLookAt( 100,0,0,  0,0,0,  0,1,0 )

def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 200.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture

    glMatrixMode(GL_MODELVIEW)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0,0.0,0.0,0.0)

    desenhaSol()

    xrot = xrot + 0.5
    yrot = yrot + 0.5
    zrot = zrot + 0.5


    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == b'x' or tecla == b'X':
        dx = 1.0
        dy = 0
        dz = 0   
    elif tecla == b'y' or tecla == b'Y':
        dx = 0
        dy = 1.0
        dz = 0   
    elif tecla == b'z' or tecla == b'Z':
        dx = 0
        dy = 0
        dz = 1.0

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print ("ESQUERDA")
        xrot -= dx                # X rotation
        yrot -= dy                 # Y rotation
        zrot -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        print ("DIREITA")
        xrot += dx                # X rotation
        yrot += dy                 # Y rotation
        zrot += dz                     
    elif tecla == GLUT_KEY_UP:
        print ("CIMA")
    elif tecla == GLUT_KEY_DOWN:
        print ("BAIXO")

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)    
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Astros")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    glutSpecialFunc(teclaEspecialPressionada)
    InitGL(800, 600)
    glutMainLoop()


main()
