import os.path
from settings import *
import pickle


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
                data = chunk.voxels
                pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        except PermissionError:
            print('Permission denied. Chunk will not be saved.')

    def load_chunk(self, path, chunk_position=(0, 0, 0)):
        path = os.path.join(path, 'chunks', f'{chunk_position}.bin')
        if not os.path.exists(path):
            raise FileNotFoundError('No chunk file found!')
        with open(path, 'rb') as f:
            pickled_data = pickle.load(f)
            print(f'Loaded chunk at position {chunk_position}')
            return pickled_data
