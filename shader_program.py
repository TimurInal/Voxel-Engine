from settings import *


class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.player = app.player
        # Shaders
        self.quad = self.get_program(shader_name='quad')
        self.cube = self.get_program(shader_name='cube')

        self.set_uniforms_on_init()
        self.set_global_variables()

    def set_uniforms_on_init(self):
        self.quad['m_proj'].write(self.player.m_proj)
        self.quad['m_model'].write(glm.mat4())

        self.cube['m_proj'].write(self.player.m_proj)
        self.cube['m_model'].write(glm.mat4())

    def set_global_variables(self):
        # set vec3 lightColour on frag shaders
        self.cube['lightColour'].value = LIGHT_COLOUR

    def update(self):
        self.quad['m_view'].write(self.player.m_view)

        self.cube['m_view'].write(self.player.m_view)

    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
