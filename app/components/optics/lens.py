# components/optics/lens.py

from components.optics.optic.py import Optic

class Lens(Optic):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)

    def render(self):
        """Render the lens on the interactive image."""
        self.image = ui.image('assets/lens_image.png').style(
            f'position: absolute; left: {self.x}px; top: {self.y}px; pointer-events: none;'
        ).classes('w-16')
