
from os import system
from manimlib import *

class geometry(Scene):
    def construct(self):
        circle = Circle(
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=GREEN,
            stroke_opacity=0.9,
            stroke_width=8,
            gloss=1.0
        )

        self.add(circle)


if __name__ == "__main__":
    system("manimgl src/base/circle_example.py geometry")
