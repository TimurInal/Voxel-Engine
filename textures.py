import os
import sys

import pygame as pg
import moderngl as mgl


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Textures:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        # load texture
        self.texture_0 = self.load('frame.png')
        self.texture_atlas = self.load('texture_atlas.png', is_tex_array=True)

        # assign texture unit
        self.texture_0.use(location=0)
        self.texture_atlas.use(location=0)

    def load(self, file_name, is_tex_array=False):
        texture = pg.image.load(resource_path(f'assets/{file_name}'))
        texture = pg.transform.flip(texture, flip_x=True, flip_y=False)

        if is_tex_array:
            num_layers = 3 * texture.get_height() // texture.get_width()  # 3 textures per layer
            texture = self.app.ctx.texture_array(
                size=(texture.get_width(), texture.get_height() // num_layers, num_layers),
                components=4,
                data=texture.get_buffer().raw
            )
        else:
            texture = self.ctx.texture(
                size=texture.get_size(),
                components=4,
                data=pg.image.tostring(texture, 'RGBA', False)
            )
        texture.anisotropy = 32.0
        texture.build_mipmaps()
        texture.filter = (mgl.NEAREST, mgl.NEAREST)
        # texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        return texture
