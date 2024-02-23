import numpy as np


class BaseMesh:
    def __init__(self):
        # opengl context
        self.ctx = None
        # shader program
        self.program = None
        # vertex buffer data type formate: "3f 3f"
        self.vbo_format = None
        # attribute names according to the format: ("in_position", "in_colour")
        self.attrs: tuple[str, ...] = None
        # vertex array object
        self.vao = None

    def get_vertex_data(self, world_position) -> np.array: ...

    def get_vao(self, world_position):
        vertex_data = self.get_vertex_data(world_position)
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.simple_vertex_array(self.program, vbo, *self.attrs)
        return vao

    def render(self):
        self.vao.render()
