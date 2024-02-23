from settings import *
from meshes.base_mesh import BaseMesh

class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.ctx = app.ctx
        self.program = app.shader_program.quad

        self.vbo = '3f 3f'
        self.attrs = ('in_position', 'in_colour')
        self.vao = self.get_vao()

    def get_vertex_data(self):
        vertices = np.array([
            (0.5, 0.5, 0.0), (-0.5, 0.5, 0.0), (-0.5, -0.5, 0.0),
            (0.5, 0.5, 0.0), (-0.5, -0.5, 0.0), (0.5, -0.5, 0.0)
        ], dtype=np.float32)
        colours = np.array([
            (0, 1, 0), (1, 0, 0), (1, 1, 0),
            (0, 1, 0), (1, 1, 0), (0, 0, 1)
        ], dtype=np.float32)
        vertex_data = np.hstack((vertices, colours))
        return vertex_data
