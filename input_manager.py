import pygame as pg

def get_key(key):
    key_state = pg.key.get_pressed()
    return key_state[key]