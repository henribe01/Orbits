import matplotlib.pyplot as plt


class DraggableRectangle:
    def __init__(self, line: plt.Line2D, name: str = None):
        self.line = line
        self.press = None
        self.name = name

    def connect(self):
        """Connect to all the events we need."""
        self.cidpress = self.line.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.line.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.line.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        """Check whether mouse is over us; if so, store some data."""
        if event.inaxes != self.line.axes:
            return
        contains, attrd = self.line.contains(event)
        if not contains:
            return
        self.press = *self.line.get_xydata(), (event.xdata, event.ydata)
        self.line.figure.canvas.set_selected(self.line)

    def on_motion(self, event):
        """Move the rectangle if the mouse is over us."""
        if self.press is None or event.inaxes != self.line.axes:
            return
        (x0, y0), (xpress, ypress) = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        # print(f'x0={x0}, xpress={xpress}, event.xdata={event.xdata}, '
        #       f'dx={dx}, x0+dx={x0+dx}')
        self.line.set_xdata(x0 + dx)
        self.line.set_ydata(y0 + dy)

        self.line.figure.canvas.draw()

    def on_release(self, event):
        """Clear button press information."""
        self.press = None
        self.line.figure.canvas.draw()
        self.line.figure.canvas.calc_path()

    def disconnect(self):
        """Disconnect all callbacks."""
        self.line.figure.canvas.mpl_disconnect(self.cidpress)
        self.line.figure.canvas.mpl_disconnect(self.cidrelease)
        self.line.figure.canvas.mpl_disconnect(self.cidmotion)
