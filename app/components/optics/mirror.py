# components/optics/mirror.py

from components.optics.optic import Optic

class Mirror(Optic):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)

    def render(self):
        """Render the mirror on the interactive image."""
        self.image = ui.image('assets/mirror_image.png').style(
            f'position: absolute; left: {self.x}px; top: {self.y}px; pointer-events: none;'
        ).classes('w-16')
