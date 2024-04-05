from manim import *
from ..classes.moving_camera_slide import MovingCameraSlide
from ..utils.zoom_loop import zoom_loop
from ..utils.LinearRegressionPlus import LinearRegressionPlus

def slide2(scene:MovingCameraSlide):
    slide_title = Text("Linear Regression")
    scene.play(Write(slide_title))
    scene.next_slide(notes="")
    scene.play(slide_title.animate.scale(0.5).to_edge(UP))
    
    header = scene.canvas["header"]
    
    content = VGroup().next_to(header, DOWN)
    
    lr_graph = LinearRegressionPlus()
    
    content_height = config.frame_height - header.get_height()
    
    content.add(
        lr_graph.get_graph()
    ).scale_to_fit_height(content_height*.8
                          ).next_to(header, DOWN, buff=0.5)
    
    content[0].render_animated(scene)
    
    scene.next_slide(notes="Explain the formulas")
    
    # scene.wipe()