# components/optic_manager.py

from nicegui import ui
from components.optics.lens import Lens
from components.optics.mirror import Mirror
from nicegui.events import MouseEventArguments

class OpticManager:
    def __init__(self):
        self.optics = []
        self.selected_optic = None
        self.optic_counter = 0  # To keep track of unique optic IDs
        self.table = None  # Placeholder for the table object

    def add_optic(self, optic_type, x, y):
        """Add a new optic to the interactive image and the table."""
        new_optic = None
        if optic_type == 'lens':
            new_optic = Lens(self.optic_counter, x, y)
        elif optic_type == 'mirror':
            new_optic = Mirror(self.optic_counter, x, y)

        if new_optic:
            self.optic_counter += 1
            self.optics.append(new_optic)
            new_optic.render()  # Render the optic on the screen
            self.update_table()

    def remove_optic(self, optic_id):
        """Remove an optic by its ID and update the table."""
        optic_to_remove = next((optic for optic in self.optics if optic.id == optic_id), None)
        if optic_to_remove:
            optic_to_remove.image.delete()
            self.optics.remove(optic_to_remove)
            self.update_table()

    def handle_mouse_event(self, e: MouseEventArguments, x_position_label, last_position_label):
        """Handle mouse events for the interactive image."""
        if e.type == 'mousedown':
            # Check if any optic is being clicked within the threshold
            for optic in self.optics:
                if optic.is_within_threshold(e.image_x, e.image_y):
                    optic.start_dragging()
                    self.selected_optic = optic
                    break

        if e.type == 'mouseup' and self.selected_optic:
            # Stop dragging the selected optic
            self.selected_optic.stop_dragging()
            last_position_label.set_text(f'Optic {self.selected_optic.id} Last Dragged Position: {self.selected_optic.x}px')
            self.selected_optic = None

        # Update the x-position of the selected optic if dragging (constrained to x-axis only)
        if self.selected_optic and self.selected_optic.dragging:
            self.selected_optic.x = e.image_x  # Update only the x-position
            self.selected_optic.update_position()  # Apply new position to the image
            self.update_table()

        # Update the x-position label with the current mouse position
        x_position_label.set_text(f'Current Mouse Position: {e.image_x}px')

    def update_table(self):
        """Update the table to reflect the current optic data."""
        if self.table:
            self.table.rows.clear()
            for optic in self.optics:
                self.table.add_row(
                    [optic.id, optic.x],
                    editable=True,
                    on_edit=lambda e, optic=optic: self.on_table_edit(e, optic)
                )

    def on_table_edit(self, e, optic):
        """Handle updates to the table and change optic position accordingly."""
        try:
            new_x = int(e.value)
            optic.set_position(new_x)
        except ValueError:
            # Revert to the previous value if the input is invalid
            e.element.set_text(str(optic.x))

    def create_table(self):
        """Create the table and store its reference."""
        self.table = ui.table(columns=['ID', 'X Position'], rows=[], editable=True, cell_padding='10px')
        self.update_table()
