from glm import vec3

from settings import *
from meshes.base_mesh import BaseMesh

class CubeMesh(BaseMesh):
    def __init__(self, app, world_position):
        super().__init__()

        self.app = app
        self.ctx = app.ctx
        self.program = app.shader_program.quad

        self.vbo = '3f 3f'
        self.attrs = ('in_position', 'in_colour')
        self.vao = self.get_vao(world_position)

    def get_vertex_data(self, world_position):
        # A 3D box has 6 faces and each face has 6 vertices (as 2 triangles), so totally 36 vertices

        offsetVertices = [
            (x + world_position.x, y + world_position.y, z + world_position.z)
            for x, y, z in [
                # front face
                (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5),
                (-0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5),

                # back face
                (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5),
                (-0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5),

                # left face
                (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5),
                (-0.5, -0.5, -0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5),

                # right face
                (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, 0.5),
                (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5),

                # bottom face
                (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5),
                (-0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),

                # top face
                (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5),
                (-0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5)
            ]
        ]

        vertices = np.array(offsetVertices, dtype=np.float32)

        colours = np.array([
            (1, 0, 0), (1, 0, 0), (1, 0, 0),
            (1, 0, 0), (1, 0, 0), (1, 0, 0),

            (1, 1, 0), (1, 1, 0), (1, 1, 0),
            (1, 1, 0), (1, 1, 0), (1, 1, 0),

            (0, 1, 0), (0, 1, 0), (0, 1, 0),
            (0, 1, 0), (0, 1, 0), (0, 1, 0),

            (0, 1, 1), (0, 1, 1), (0, 1, 1),
            (0, 1, 1), (0, 1, 1), (0, 1, 1),

            (0, 0, 1), (0, 0, 1), (0, 0, 1),
            (0, 0, 1), (0, 0, 1), (0, 0, 1),

            (0, 0, 0), (0, 0, 0), (0, 0, 0),
            (0, 0, 0), (0, 0, 0), (0, 0, 0)
        ], dtype=np.float32)
        vertex_data = np.hstack((vertices, colours))
        return vertex_data
