from gui import Gui
from image_viewer import ImageViewer
from data_viewer import DataViewer

def main():
    gui = Gui()
    image_viewer = gui.image_viewer
    data_viewer = gui.data_viewer

    # Update the time slider with the maximum time (replace with your actual max time)
    max_time = 10
    image_viewer.update_time_slider(max_time)

    # Add code for displaying data and creating graphs
    # (You need to integrate this with your specific implementation)

    gui.mainloop()

if __name__ == "__main__":
    main()
