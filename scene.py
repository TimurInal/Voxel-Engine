from glm import vec3

from settings import *
from meshes.quad_mesh import QuadMesh
from meshes.cube_mesh import CubeMesh


class Scene:
    def __init__(self, app):
        self.app = app
        self.cubes = np.empty(WORLD_SIZE, dtype=object)

        self.create_world()

    def create_world(self):
        for x in range(self.cubes.shape[0]):
            for y in range(self.cubes.shape[1]):
                for z in range(self.cubes.shape[2]):
                    mesh = CubeMesh(app=self.app, world_position=(x, y, z))
                    self.cubes[x, y, z] = mesh
        print(f"Created world with {np.prod(self.cubes.shape)} voxels.")  # this counts total voxels

    def is_void(self, x, y, z):
        if x < 0 or x >= WORLD_SIZE[0] or y < 0 or y >= WORLD_SIZE[1] or z < 0 or z >= WORLD_SIZE[2]:
            return True

        if self.cubes[x, y, z] is None:
            return True
        return False

    def update(self):
        pass

    def render(self):
        for x in range(self.cubes.shape[0]):
            for y in range(self.cubes.shape[1]):
                for z in range(self.cubes.shape[2]):
                    if self.cubes[x, y, z] is not None:
                        try:
                            # front, back, left, right, bottom, top
                            render_sides = [True, True, True, True, True, True]

                            render_sides[0] = self.is_void(x, y, z + 1)
                            render_sides[1] = self.is_void(x, y, z - 1)
                            render_sides[2] = self.is_void(x - 1, y, z)
                            render_sides[3] = self.is_void(x + 1, y, z)
                            render_sides[4] = self.is_void(x, y - 1, z)
                            render_sides[5] = self.is_void(x, y + 1, z)

                            self.cubes[x, y, z].render(render_sides)

                        except AttributeError:
                            print(f"Object at indices {x}, {y}, {z} is not a CubeMesh instance.")
                    else:
                        print(f"Object at indices {x}, {y}, {z} is not a CubeMesh instance.")