import pygame as pg
from camera import Camera
from settings import *
import input_manager as im


class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)

        self.speed = PLAYER_SPEED

    def update(self):
        self.keyboard_control()
        self.mouse_control()
        super().update()

    def handle_event(self, event):
        # adding and removing voxels with clicks
        if event.type == pg.MOUSEBUTTONDOWN:
            voxel_handler = self.app.scene.world.voxel_handler
            try:
                if event.button == 1:
                    voxel_handler.remove_voxel()
                if event.button == 3:
                    voxel_handler.add_voxel()
            except AttributeError:
                print('Could not add block.')
                return
        if im.key_down(pg.K_LSHIFT, event):
            self.speed = 0.002 * 20
        if im.key_up(pg.K_LSHIFT, event):
            self.speed = 0.002


    def mouse_control(self):
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        if mouse_dx:
            self.rotate_yaw(delta_x=mouse_dx * MOUSE_SENSITIVITY)
        if mouse_dy:
            self.rotate_pitch(delta_y=mouse_dy * MOUSE_SENSITIVITY)

    def keyboard_control(self):
        vel = self.speed * self.app.delta_time
        if im.key_pressed(pg.K_w):
            self.move_forward(vel)
        if im.key_pressed(pg.K_s):
            self.move_back(vel)
        if im.key_pressed(pg.K_d):
            self.move_right(vel)
        if im.key_pressed(pg.K_a):
            self.move_left(vel)
        if im.key_pressed(pg.K_e):
            self.move_up(vel)
        if im.key_pressed(pg.K_q):
            self.move_down(vel)
















































