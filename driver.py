from manim import *
from src.scenes.slide3 import slide3 as scene
from src.classes.moving_camera_slide import MovingCameraSlide
import subprocess

class TestClass(MovingCameraSlide):

    def construct(self):
        header = Rectangle(width=5, height=2, color=BLUE).to_edge(UP)
        self.add_to_canvas(header=header)    
        scene(self)

if __name__ == "__main__":
    proccess = subprocess.run(["manim", "render", "-ql", "driver.py", "TestClass"])
    # proccess = subprocess.run(["manim-slides", "convert", "TestClass" , "_site/test.html"])