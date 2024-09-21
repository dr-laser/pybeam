# components/optics/optic.py

from abc import ABC, abstractmethod
from nicegui import ui

class Optic(ABC):
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.image = None
        self.dragging = False

    @abstractmethod
    def render(self):
        """Render the optic on the interactive image."""
        pass

    def update_position(self):
        """Update the visual position of the optic based on its coordinates."""
        if self.image:
            self.image.style(f'left: {self.x}px; top: {self.y}px;')

    def is_within_threshold(self, mouse_x, mouse_y, x_threshold=20, y_threshold=300):
        """Check if the mouse is within the drag threshold of the optic."""
        return abs(mouse_x - self.x) <= x_threshold and abs(mouse_y - self.y) <= y_threshold

    def start_dragging(self):
        """Start dragging the optic."""
        self.dragging = True

    def stop_dragging(self):
        """Stop dragging the optic."""
        self.dragging = False

    def set_position(self, x):
        """Set a new x position for the optic."""
        self.x = x
        self.update_position()
