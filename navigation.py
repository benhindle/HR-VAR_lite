from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class NavigationToolbar(NavigationToolbar2Tk):
    # only display required buttons
    toolitems = [t for t in NavigationToolbar2Tk.toolitems if
                 t[0] in ('Home', 'Pan', 'Zoom', 'Save')]
    
    def set_message(self, msg):
        pass