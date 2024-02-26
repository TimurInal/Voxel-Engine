import pygame as pg

def key_pressed(key: pg.key):
    key_state = pg.key.get_pressed()
    return key_state[key]
