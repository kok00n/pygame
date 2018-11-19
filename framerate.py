import pygame


class FpsView(object):

    def __init__(self, width=640, height=400, fps=30):
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.playtime = 0.0
        self.font = pygame.font.SysFont("mono", 20, bold=True)

    def run(self):
        mainloop = True
        while mainloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mainloop = False

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
            #self.draw_text(f"FPS: {self.clock.get_fps():02.2f} Playtime: {self.playtime:4.2f}")

            # Big pink circle in the middle of the screen
            radius = int(min((self.width, self.height)))
            self.draw_circle(where=((self.width - radius) // 2, (self.height - radius) // 2), radius=int(radius / 2) , color=(255, 192, 203))

            pygame.display.update()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()

    def draw_text(self, text):
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))

    def draw_circle(self, where, radius=25, color=(0, 0, 255)):
        surface = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(surface, color, (radius, radius), radius)
        self.screen.blit(surface, where)


if __name__ == '__main__':
    FpsView().run()
