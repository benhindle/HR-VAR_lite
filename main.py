from tkinter import Menu
import display
import actions
import globals

globals.init()

display.set_grid()

display.insert_figure()

actions.init_bottons(plot=False)

globals.root.mainloop()