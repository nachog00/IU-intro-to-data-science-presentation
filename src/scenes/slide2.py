from manim import *
from ..classes.moving_camera_slide import MovingCameraSlide
from ..utils.zoom_loop import zoom_loop

def slide2(scene:MovingCameraSlide):
    slide_title = Text("Slide 2")
    scene.play(Write(slide_title))
    scene.next_slide(notes="Don't forget to tell about this!!!!!")
    scene.play(slide_title.animate.scale(0.5).to_edge(UP))
    
    header = scene.canvas["header"]
    content = VGroup().next_to(header, DOWN)
    
    content.add(Square(color=BLUE))
    content.add(Square(color=RED))
    content.add(Square(color=GREEN))
    content.arrange(RIGHT, buff=2)
    
    scene.add(content)
    scene.play(Write(content))
    
    scene.next_slide()
    
    zoom_loop(scene, content, next_slide=True)
    
    # scene.wipe()