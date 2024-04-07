from manim import *
from ..classes.moving_camera_slide import MovingCameraSlide
from ..utils.zoom_loop import zoom_loop
from ..utils.LinearRegressionPlus import LinearRegressionPlus


def slide3(scene: MovingCameraSlide):
    slide_title = Text("Conclusion")
    scene.play(Write(slide_title))
    scene.next_slide(notes="")
    scene.play(slide_title.animate.scale(0.5).to_edge(UP))

    header = scene.canvas["header"]

    content = VGroup().next_to(header, DOWN)

    texts = [
        {
            "first": "Linear regression",
            "second": "Science",
            "color": GREEN,
        },
        {
            "first": "is a projection of",
            "second": "is a projection of",
            "color": WHITE,
        },
        {
            "first": "sample events",
            "second": "reality",
            "color": RED,
        },
        {
            "first": "onto the",
            "second": "onto",
            "color": WHITE,
        },
        {
            "first": "linear functions space",   
            "second": "our mental models",
            "color": PINK,
        },
    ]

    def get_text(item, which):
        return Text(item[which], color=item["color"]).scale(0.5).next_to(content, DOWN)
    
    # Render all the first texts
    first_texts = VGroup()
    for i,item in enumerate(texts):
        first_text = get_text(item, "first")
        first_texts.add(first_text).arrange(DOWN, buff=0.2)
        # if not i == 0:
        #     shift_up_animation = first_text[i-1].animate.shift(UP)
    
    scene.play(Write(first_texts))

    # Transform the first texts onto the new texts
    second_texts = VGroup()
    for i, item in enumerate(texts):
        second_text = get_text(item, "second").move_to(first_texts[i])
        second_texts.add(second_text)
        
    second_texts.arrange(DOWN, buff=0.2)
    
    scene.play(Transform(first_texts, second_texts))
