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
        while self.running:
            self.redraw()


    def close(self):
        self.running = False


    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


# New Code Here

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:

    def __init__(self, point01, point02):
        self.point01 = point01
        self.point02 = point02


    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point01.x, self.point01.y, self.point02.x, self.point02.y, fill=fill_color, width=2
        )













def main():
    win = Window(800, 600)  # Create a window of 800x600 pixels

    # Creating Points and Line
    point01 = Point(100, 150)  # Use values that fit your canvas!
    point02 = Point(400, 300)
    line = Line(point01, point02)

    # Drawing the Line
    win.draw_line(line, "red")  # Pass a color like "red"

    # Wait for the window to be closed
    win.wait_for_close()



if __name__ == "__main__":
    main()