from glm import vec3

from settings import *
from meshes.quad_mesh import QuadMesh
from meshes.cube_mesh import CubeMesh

class Scene:
    def __init__(self, app):
        self.app = app
        self.cube1 = CubeMesh(self.app, vec3(0, 5, 0))
        #self.quad = QuadMesh(self.app, vec3(0, 4, 0.5))

    def update(self):
        pass

    def render(self):
        self.cube1.render()
        #self.quad.render()
