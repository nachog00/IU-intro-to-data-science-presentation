from manim import *
from src.classes.moving_camera_slide import MovingCameraSlide
from manim_slides import Slide
from src.config import config
from src.scenes.intro import intro
from src.scenes.quote import quote
from src.scenes.slide1 import slide1
from src.scenes.slide2 import slide2

class Presentation(MovingCameraSlide):
    def construct(self):
        config(self)
        # INTRO
        intro(self)
        # SLIDE 1
        quote(self)
        