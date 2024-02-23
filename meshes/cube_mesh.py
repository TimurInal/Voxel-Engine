from glm import vec3

from settings import *
from meshes.base_mesh import BaseMesh

colour = (0.4667, 0.2627, 0.2588)

class CubeMesh(BaseMesh):
    def __init__(self, app, world_position):
        super().__init__()

        self.app = app
        self.ctx = app.ctx
        self.program = app.shader_program.cube

        self.vbo = '3f 3f'
        self.attrs = ('in_position', 'in_colour')
        self.world_position = world_position
        self.render_sides = {'front': True, 'back': True, 'left': True, 'right': True, 'bottom': True, 'top': True}

    def get_vertex_data(self, world_position, render_sides):
        # render_sides is a list or tuple of booleans [front, back, left, right, bottom, top]

        faces = [
            [  # front face
                (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5),
                (-0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)
            ],
            [  # back face
                (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5),
                (-0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5)
            ],
            [  # left face
                (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5),
                (-0.5, -0.5, -0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5)
            ],
            [  # right face
                (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, 0.5),
                (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5)
            ],
            [  # bottom face
                (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5),
                (-0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5)
            ],
            [  # top face
                (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5),
                (-0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5)
            ]
        ]

        # Filter faces to render
        faces_to_render = [face for face, render in zip(faces, render_sides) if render]

        offsetVertices = [
            (x + world_position[0], y + world_position[1], z + world_position[2])
            for face in faces_to_render for x, y, z in face
        ]

        offsetColours = [colour for face, render in zip(faces, render_sides) if render for _ in face]

        vertices = np.array(offsetVertices, dtype=np.float32)
        colours = np.array(offsetColours, dtype=np.float32)

        vertex_data = np.hstack((vertices, colours))

        return vertex_data

    def render(self, render_sides=None):
        if render_sides is not None:
            self.render_sides = render_sides
        vertex_data = self.get_vertex_data(self.world_position, self.render_sides)

        # Skip if no vertices to render
        if vertex_data.size == 0:
            return

        vbo = self.ctx.buffer(vertex_data)
        if self.vao is not None:
            self.vao.release()
        self.vao = self.ctx.simple_vertex_array(self.program, vbo, *self.attrs)
        self.vao.render()
