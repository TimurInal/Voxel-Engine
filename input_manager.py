import pygame as pg

def key_pressed(key: pg.key):
    key_state = pg.key.get_pressed()
    return key_state[key]

def key_down(key: pg.key, event):
    if event.type == pg.KEYDOWN:
        if event.key == key:
            return True

def key_up(key: pg.key, event):
    if event.type == pg.KEYUP:
        if event.key == key:
            return True