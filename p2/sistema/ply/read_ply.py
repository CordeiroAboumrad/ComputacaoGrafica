from plyfile import PlyData
import numpy as np
import os

transform = []

def read_ply_xyz(filename):
    """ read XYZ point cloud from filename PLY file """
    assert(os.path.isfile(filename))
    with open(filename, 'rb') as f:
        plydata = PlyData.read(f)
        num_verts = plydata['vertex'].count
        num_faces = plydata['face'].count
        # print(num_faces)
        vertices = np.zeros(shape=[num_verts, 3], dtype=np.float32)
        vertices[:,0] = plydata['vertex'].data['x']
        vertices[:,1] = plydata['vertex'].data['y']
        vertices[:,2] = plydata['vertex'].data['z']
        
        faces = np.array([f[0] for f in plydata["face"].data])
        
        # print(faces)
        # print(vertices)


    return vertices, faces

read_ply_xyz("C:/Users/VISAGIO/Documents/CEFET-RJ/Computação Gráfica/sistema/ply/cube.ply")
