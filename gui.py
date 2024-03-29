import tkinter.messagebox
import datetime
import tkinter as tk
from tkinter import filedialog
from image_viewer import ImageViewer
from data_viewer import DataViewer

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Analysis Interface")
        self.geometry("1200x800")
        self.configure(bg='white')  # Set default background color to white
        
        # Create a menu bar
        menubar = tk.Menu(self)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Upload file...", accelerator="Ctrl+U", command=self.open_file)

        # Open Recent menu
        self.open_recent_menu = tk.Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label="Open Recent", menu=self.open_recent_menu)

        file_menu.add_command(label="New Window", accelerator="Ctrl+N", command=self.new_window)
        file_menu.add_separator()
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save)
        file_menu.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=self.save_as)
        file_menu.add_command(label="Save All", accelerator="Ctrl+K", command=self.save_all)
        file_menu.add_separator()
        file_menu.add_command(label="Close Window", accelerator="Alt+F4", command=self.close_window)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+E", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Store the file_menu as an instance variable
        self.file_menu = file_menu
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        # Preferences menu
        preferences_menu = tk.Menu(menubar, tearoff=0)
        preferences_menu.add_command(label="Mode", command=self.show_preferences)
        menubar.add_cascade(label="Preferences", menu=preferences_menu)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)
        
        # Container for DataViewer, ImageViewer, and GraphFrame
        main_container = tk.Frame(self)
        main_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.data_viewer = DataViewer(main_container)
        self.data_viewer.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        self.image_viewer = ImageViewer(main_container)
        self.image_viewer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.graph_frame = tk.Frame(main_container)  # Frame for the graph
        self.graph_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        
        # Variable to track night mode
        self.night_mode = tk.BooleanVar()
        self.night_mode.set(False)
        
        # Bind shortcut keys
        self.bind_shortcuts()
        
        # List to store recently used files
        self.recent_files = []  

    def bind_shortcuts(self):
        self.bind("<Control-U>", lambda event: self.open_file())
        self.bind("<Control-N>", lambda event: self.new_window())
        self.bind("<Control-S>", lambda event: self.save())
        self.bind("<Control-Shift-S>", lambda event: self.save_as())
        self.bind("<Control-K>", lambda event: self.save_all())
        self.bind("<Alt-F4>", lambda event: self.close_window())
        self.bind("<Control-E>", lambda event: self.quit())
        self.bind("<Control-R>", lambda event: self.open_recent_file(self.recent_files[0]) if self.recent_files else None)
        
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tiff;*.tif")])
        if file_path:
            self.image_viewer.load_image(file_path)
            self.update_recent_files(file_path)
            
    def update_recent_files(self, file_path):
        # Update the list of recent files
        if file_path in self.recent_files:
            self.recent_files.remove(file_path)
        self.recent_files.insert(0, file_path)

        # Keep only the five most recent files
        self.recent_files = self.recent_files[:5]
    
        # Update the "Open Recent" menu
        self.update_open_recent_menu()
        
    def update_open_recent_menu(self):
        # Clear the current menu items
        self.open_recent_menu.delete(0, tk.END)

        # Add the recent files to the menu
        for i, file_path in enumerate(self.recent_files):
            accelerator = f"Ctrl+{i + 1}" if i < 9 else ""  # You can customize the accelerator
            self.open_recent_menu.add_command(
                label=f"Recent File {i + 1}",
                accelerator=accelerator,
                command=lambda path=file_path: self.open_recent_file(path)
            )
            
    def open_recent_file(self, file_path):
        self.image_viewer.load_image(file_path)
        self.update_recent_files(file_path)
    
    
    def show_preferences(self):
        # Create a preferences dialog with a night mode toggle
        preferences_dialog = tk.Toplevel(self)
        preferences_dialog.title("Mode")

        night_mode_checkbox = tk.Checkbutton(preferences_dialog, text="Night Mode",
                                             variable=self.night_mode, command=self.toggle_night_mode)
        night_mode_checkbox.pack(padx=10, pady=10)

    def toggle_night_mode(self):
        # Toggle night mode
        if self.night_mode.get():
            self.configure(bg='black')
            self.image_viewer.configure(bg='black')
            self.data_viewer.configure(bg='black')
            self.graph_frame.configure(bg='black')
        else:
            self.configure(bg='white')
            self.image_viewer.configure(bg='white')
            self.data_viewer.configure(bg='white')
            self.graph_frame.configure(bg='white')

    def new_window(self):
        # Implement the logic for opening a new window
        pass

    def save(self):
        # Implement the logic for saving
        pass

    def save_as(self):
        # Implement the logic for save as
        pass

    def save_all(self):
        # Implement the logic for saving all
        pass

    def close_window(self):
        # Implement the logic for closing the window
        pass
    
    def show_about(self):
        about_info = (
            "Image Analysis Interface\n\n"
            "Author: Aya, Carlos, Marc, Tom\n"
            "Version: 1.0\n"
            f"Date: {datetime.date.today()}\n"
            "Copyright © 2024 PE BMD. All rights reserved."
        )

        tkinter.messagebox.showinfo("About", about_info)

def main():
    gui = Gui()
    gui.mainloop()

if __name__ == "__main__":
    main()
