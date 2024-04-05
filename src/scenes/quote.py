from manim import *
from ..classes.moving_camera_slide import MovingCameraSlide
from ..utils.zoom_loop import zoom_loop
from ..constants import FONT_SIZES

def quote(scene:MovingCameraSlide):
    
    quote_text = Text("\"Truth is much to complicated to\n allow anything but approximations.\"", font_size=FONT_SIZES["TITLE"])
    author = Text("- John von Neumann", color=GREEN_D , font_size=FONT_SIZES["SUBTITLE"])
    
    quote_group = VGroup(quote_text, author).arrange(DOWN, buff=0.25 , aligned_edge=RIGHT)
    
    scene.play(Write(quote_group))
    
    scene.next_slide()
    
    scene.play(Unwrite(quote_group))
    