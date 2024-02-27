import pygame

pygame.init()


class UIRenderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)  # You can replace None with your font file path

    def draw_button(self, text, x, y, w, h, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(x, y, w, h))
        text_surface = self.font.render(text, True, (0, 0, 0))  # text, antialias, color
        self.screen.blit(text_surface, (
        x + (w - text_surface.get_width()) // 2, y + (h - text_surface.get_height()) // 2))  # center the text

    def draw_text(self, text, x, y, size, color):
        font = pygame.font.Font(None, size)  # Use the default font, and size given by parameter "size"
        text_surface = font.render(text, True, color)  # Render the text
        self.screen.blit(text_surface, (x, y))  # Draw text surface onto the screen at position x, y

    def check_click(self, x, y, w, h):
        mouse_pos = pygame.mouse.get_pos()
        return pygame.Rect(x, y, w, h).collidepoint(mouse_pos)
