from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width, height):
        self.root = Tk()
        self.root.title('Maze Solver')
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()


    def close(self):
        self.running = False



def main():
    win = Window(800, 600)  # Create a window of 800x600 pixels
    win.wait_for_close()    # Wait for it to be closed



if __name__ == "__main__":
    main()