# Voxel Engine

The Voxel Engine project is a 3D game engine that uses voxel generation to render complex terrains and objects. 

The engine supports multiple features necessary for a flexible gaming platform. These features include:

- Modern OpenGL rendering.
- Voxel based terrain generation.
- Efficient voxel handling to render large, detailed terrains.
  
The engine uses [Pygame](https://www.pygame.org/) as a foundation for rendering and event handling, along with [ModernGL](https://moderngl.readthedocs.io/en/latest/) for efficient graphics rendering.

## Key Classes
Several key classes are involved in running the engine, including:

### `VoxelEngine`

This class is the main game loop, responsible for initializing the game, handling events, and rendering the game.

### `ChunkSaver`

This class provides utilities for saving and loading game states by reading and writing chunk data to the disk.

### `Chunk`

This class represents a chunk, a 3D array of voxels. It includes logic for generating terrain based on noise functions.

### `World`

This class collaborates with the `Chunk` and `ChunkSaver` classes to manage the game world. 

## Usage
To use the engine, you simply need to create an instance of the `VoxelEngine` object, and then call its `run` method.
```python
from core import VoxelEngine

if __name__ == '__main__':
  app = VoxelEngine()
  app.run()
```

## Installation

**It is strongly recommended to ensure your graphics drivers are up-to-date to ensure that there are no issues with ModernGL**

To install the required packages for this project, you can use `pip`:

* Pygame
```sh
pip install pygame
```
* ModernGL
```sh
pip install moderngl
```
* Numba and NumPy
```sh
pip install numba numpy
```

## Future Updates

<li> Infinite terrain
<li> Player physics
<li> Player hotbar

<br><hr><br>

Please note that this engine was created using Python 3.12.1 and tested on Windows 11. So, it's more likely to perform best under similar conditions. Although it should work on most operating systems and Python 3.x versions, there may be slight variations or issues based on the development environment.
