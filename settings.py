import os
import time
from enum import Enum

class WorldType(Enum):
    NORMAL = 1
    FLAT = 2

from numba import njit
import numpy as np
import glm
import math
import random

# resolution
WIN_RES = glm.vec2(1600, 900)
# WIN_RES = glm.vec2(1920, 1080)

# world generation
SEED = 0
WORLD_TYPE = WorldType.FLAT

# ray casting
MAX_RAY_DST = 6

# chunk
CHUNK_SIZE = 48
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE
CHUNK_SPHERE_RADIUS = H_CHUNK_SIZE * math.sqrt(3)

# world
WORLD_W, WORLD_H = 2, 2
WORLD_D = WORLD_W
WORLD_AREA = WORLD_W * WORLD_D
WORLD_VOL = WORLD_AREA * WORLD_H

# world center
CENTER_XZ = WORLD_W * H_CHUNK_SIZE
CENTER_Y = WORLD_H * H_CHUNK_SIZE

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 65
V_FOV = glm.radians(FOV_DEG)  # vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)  # horizontal FOV
NEAR = 0.01
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(CENTER_XZ, WORLD_H * CHUNK_SIZE, CENTER_XZ)
MOUSE_SENSITIVITY = 0.002

# colors
BG_COLOR = glm.vec3(0.545, 0.659, 1.0)

# textures
BEDROCK = 1
GRASS_BLOCK = 2
DIRT = 3
STONE = 4
OAK_LOG = 5
OAK_LEAVES = 6
SNOW = 7
COBBLESTONE = 8
SAND = 9
IRON_ORE = 10
COAL_ORE = 11
LIGHT = 12

# terrain levels
SNOW_LVL = 68
STONE_LVL = 49
DIRT_LVL = 40
GRASS_LVL = 8
SAND_LVL = 7

IRON_CHANCE = 1
COAL_CHANCE = 10

# tree settings
TREE_PROBABILITY = 0.02
TREE_WIDTH, TREE_HEIGHT = 4, 8
TREE_H_WIDTH, TREE_H_HEIGHT = TREE_WIDTH // 2, TREE_HEIGHT // 2

# saving
PERSISTANT_FILE_PATH = os.path.join(os.getenv('LOCALAPPDATA'), 'Voxel Engine')
