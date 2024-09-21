# main.py

from nicegui import ui
from components.optic_manager import OpticManager

# Create an instance of the OpticManager to manage all optics
optic_manager = OpticManager()

# Create labels to display the current mouse position and last dragged position
x_position_label = ui.label('Current Mouse Position: 0px')
last_position_label = ui.label('Last Dragged Position: 0px')

# Create an interactive image with mouse events
src = 'https://picsum.photos/id/565/640/360'
ii = ui.interactive_image(src, on_mouse=lambda e: optic_manager.handle_mouse_event(e, x_position_label, last_position_label), 
                          events=['mousedown', 'mousemove', 'mouseup'], cross=True)

# Add buttons to add and remove optics
ui.button('Add Lens', on_click=lambda: optic_manager.add_optic('lens', x=100, y=100))
ui.button('Add Mirror', on_click=lambda: optic_manager.add_optic('mirror', x=200, y=100))
ui.button('Remove Last Optic', on_click=lambda: optic_manager.remove_optic(optic_manager.optics[-1].id if optic_manager.optics else None))

# Create the table below the interactive image to display and edit optic data
optic_manager.create_table()

ui.run()
