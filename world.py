from chunk_saver import ChunkSaver
from settings import *
from world_objects.chunk import Chunk
from voxel_handler import VoxelHandler


class World:
    def __init__(self, app):
        self.app = app
        self.chunks = [None for _ in range(WORLD_VOL)]
        self.voxels = np.empty([WORLD_VOL, CHUNK_VOL], dtype='uint8')
        self.chunk_saver = ChunkSaver(self)
        self.build_chunks()
        self.build_chunk_mesh()
        self.voxel_handler = VoxelHandler(self)

    def update(self):
        self.voxel_handler.update()

    def build_chunks(self):
        for x in range(WORLD_W):
            for y in range(WORLD_H):
                for z in range(WORLD_D):
                    chunk = Chunk(self, position=(x, y, z))
                    chunk_index = x + WORLD_W * z + WORLD_AREA * y  # get chunk index for both cases

                    if os.path.exists(os.path.join(PERSISTANT_FILE_PATH, 'chunks', f'{(x, y, z)}.bin')) and 1 == 2:
                        chunk.voxels = self.chunk_saver.load_chunk(PERSISTANT_FILE_PATH, (x, y, z))
                        chunk.is_empty = False
                        chunk.build_mesh()  # build the mesh first
                        chunk.rebuild_mesh()  # rebuild the mesh after
                    else:
                        # put the chunk voxels in a separate array
                        self.voxels[chunk_index] = chunk.build_voxels()

                        # get pointer to voxels
                        chunk.voxels = self.voxels[chunk_index]
                        chunk.build_mesh()  # build new chunks as before

                    # assign to chunk array regardless of if it's from disk or new
                    self.chunks[chunk_index] = chunk

    def build_chunk_mesh(self):
        for chunk in self.chunks:
            chunk.build_mesh()

    def render(self):
        for chunk in self.chunks:
            chunk.render()
