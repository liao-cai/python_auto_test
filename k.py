import math
import tkinter as tk
import random

class Heart:
    def __init__(self):
        self.points = set()
        self.edge = set()
        self.inner = set()
        self.build(2000)

    def build(self, n):
        for _ in range(n):
            t = random.uniform(0, 2 * math.pi)
            x = 16 * math.sin(t) ** 3
            y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
            self.points.add((x,y))
        for x,y in self.points:
            for _ in range(3):
                nx = x + random.uniform(-0.3,0.3)
                ny = y + random.uniform(-0.3,0.3)
                self.edge.add((nx,ny))
        for x,y in self.points:
            for _ in range(12):
                nx = x * 0.82
                ny = y * 0.82
                self.inner.add((nx,ny))

def draw_heart():
    win = tk.Tk()
    win.title("heart")
    win.geometry("1000x1000")
    win.configure(bg="black")
    win.attributes('-topmost', True)
    canvas = tk.Canvas(win, bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)
    h = Heart()
    scale = 18
    cx = 500
    cy = 420
    for x,y in h.points:
        canvas.create_oval(cx+x*scale, cy-y*scale, cx+x*scale+3, cy-y*scale+3, fill="#ff69b4", outline="#ff69b4")
    for x,y in h.edge:
        canvas.create_oval(cx+x*scale, cy-y*scale, cx+x*scale+2, cy-y*scale+2, fill="#ff88bb", outline="#ff88bb")
    for x,y in h.inner:
        canvas.create_oval(cx+x*scale, cy-y*scale, cx+x*scale+2, cy-y*scale+2, fill="#ffb6c1", outline="#ffb6c1")

    # 雨滴效果
    drops = []
    for i in range(120):
        x = random.randint(0,1000)
        y = random.randint(-1000,0)
        speed = random.randint(8,20)
        drops.append([x,y,speed])

    def rain():
        for d in drops:
            d[1] += d[2]
            if d[1]>1000:
                d[1] = random.randint(-100,0)
                d[0] = random.randint(0,1000)
            canvas.create_line(d[0],d[1],d[0],d[1]+12, fill="#ff99cc", width=1)
        win.after(35, rain)
    rain()
    win.mainloop()

if __name__ == '__main__':
    draw_heart()