from PyQt5.QtWidgets import QWidget

import lines
import planets
from uis.python_files.animation_widget import Ui_animation_widget
from uis.python_files.options_widget import Ui_options_widget


class AnimationWidget(QWidget, Ui_animation_widget):
    def __init__(self, parent: QWidget):
        super(AnimationWidget, self).__init__(parent)
        self.setupUi(self)
        self.connect_events()

    def connect_events(self):
        self.option_pushButton.clicked.connect(
            self.parentWidget().show_options_widget)
        self.start_pushButton.clicked.connect(
            self.canvas_widget.start_animation)
        self.stop_pushButton.clicked.connect(self.canvas_widget.stop_animation)
        self.reset_pushButton.clicked.connect(self.reset_canvas)

    def reset_canvas(self):
        """Resets Canvas to saved state"""
        planets.Planet.reset_planets()
        self.canvas_widget.reload_lines()


class OptionsWidget(QWidget, Ui_options_widget):
    def __init__(self, parent: QWidget):
        super(OptionsWidget, self).__init__(parent)
        self.setupUi(self)
        self.connect_events()
        self.selected_line = self.canvas_widget.all_lines[
            0]  # type: lines.DraggablePlanetLines
        self.set_LineEdit()

    def connect_events(self):
        self.exit_pushButton.clicked.connect(
            self.parentWidget().show_animation_widget)
        self.save_pushButton.clicked.connect(self.save)
        self.reset_pushButton.clicked.connect(self.reset_canvas)
        self.velx_lineEdit.textEdited.connect(self.update_LineEdit)
        self.vely_lineEdit.textEdited.connect(self.update_LineEdit)
        self.mass_lineEdit.textEdited.connect(self.update_LineEdit)

    def save(self):
        self.canvas_widget.save()
        self.nativeParentWidget().show_animation_widget()

    def reset_canvas(self):
        """Resets Canvas to saved state"""
        planets.Planet.reset_planets()
        self.canvas_widget.reload_lines()

    def set_selected_line(self, line):
        self.selected_line = line  # type: lines.DraggablePlanetLines
        self.set_LineEdit()

    def set_LineEdit(self):
        self.name_lineEdit.setText(str(self.selected_line.planet.name))
        self.velx_lineEdit.setText(str(round(self.selected_line.planet.vel[0], 5)))
        self.vely_lineEdit.setText(str(round(self.selected_line.planet.vel[1], 5)))
        self.mass_lineEdit.setText(f'{self.selected_line.planet.mass:.2e}')

    def update_LineEdit(self):
        self.selected_line.test_planet.set_vel(
            [self.velx_lineEdit.text(), self.vely_lineEdit.text()])
        self.selected_line.test_planet.set_mass(self.mass_lineEdit.text())
        self.canvas_widget.clear()
        self.canvas_widget.calc_path()
        self.canvas_widget.draw()
