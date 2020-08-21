from manim import *
import math


class FractalTriangle(Scene):
    # Sierpiński triangle
    def construct(self):
        t = Triangle(stroke_width=1, fill_opacity=1, color=BLUE).scale(4)
        n = 8
        self.tris = [[] for _ in range(n)]
        self.draw(t.get_bottom(), t.get_width(), 2, n)
        self.add(t)
        for x in self.tris[::-1]:
            self.play(*[GrowFromCenter(t) for t in x], run_time=2)
        self.wait(3)

    def draw(self, xb, length, scale, depth):
        if depth == 0:
            return
        self.tris[depth-1] += [Triangle(stroke_width=1, fill_opacity=1, color=BLACK, stroke_color=BLUE).scale(scale).flip(
            RIGHT).move_to(xb).align_to(xb, DOWN)]
        self.draw(xb+[-length/4, 0, 0], length/2, scale/2, depth-1)
        self.draw(xb+[length/4, 0, 0], length/2, scale/2, depth-1)
        self.draw(xb+[0, ((length*length-length*length/4)**0.5)/2, 0],
                  length/2, scale/2, depth-1)
