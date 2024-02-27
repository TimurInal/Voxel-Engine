import os.path
from settings import *
import pickle
import ctypes

class ChunkSaver:
    def __init__(self, world):
        self.app = world.app
        self.world = world

    @staticmethod
    def save_chunk(chunk, path):
        path = os.path.join(path, 'chunks')
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path + f'/{chunk.position}.bin', 'wb') as f:
                pickle.dump(chunk.voxels, f, pickle.HIGHEST_PROTOCOL)
        except PermissionError:
            print('Permission denied. Chunk will not be saved.')
