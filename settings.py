from numba import njit
import numpy as np
import glm
import math

# resolution
# WIN_RES = glm.vec2(1600, 900)
WIN_RES = glm.vec2(1920, 1080)

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)  # vertical fov
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)  # horizontal fov
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 0.002
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(0, 0, 1)
MOUSE_SENSITIVITY = 0.002

# colours
BG_COLOUR = glm.vec3(0.4745, 0.6275, 1.0)
LIGHT_COLOUR = glm.vec3(1, 1, 1)

# test params
WORLD_SIZE = (15, 1, 1)
