from manim import *
from ..classes.moving_camera_slide import MovingCameraSlide
from ..utils.zoom_loop import zoom_loop

def slide1(scene:MovingCameraSlide):
    slide_title = Text("Slide 1")
    scene.play(Write(slide_title))
    scene.next_slide(notes="Don't forget to tell about this!!!!!")
    scene.play(slide_title.animate.scale(0.5).to_edge(UP))
    
    header = scene.canvas["header"]
    content = VGroup().next_to(header, DOWN)
    
    content.add(Circle(color=BLUE))
    content.add(Circle(color=RED))
    content.add(Circle(color=GREEN))
    content.arrange(RIGHT, buff=2)
    
    
    scene.add(content)
    scene.play(Write(content))
    
    scene.next_slide()
    
    zoom_loop(scene, content)
    
    scene.wipe(Group(slide_title, content), direction=UP)