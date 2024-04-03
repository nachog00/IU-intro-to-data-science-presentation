from manim import *
from src.scenes.slide1 import slide1 as scene
from manim_slides import Slide
import subprocess

class TestClass(Slide):

    def construct(self):
        header = Rectangle(width=5, height=2, color=BLUE).to_edge(UP)
        scene.add_to_canvas(header=header)    
        scene(self)

if __name__ == "__main__":
    proccess = subprocess.run(["manim", "render", "driver.py", "-ql", "TestClass"])
    # proccess = subprocess.run(["manim-slides", "convert", "TestClass" , "_site/test.html"])
    