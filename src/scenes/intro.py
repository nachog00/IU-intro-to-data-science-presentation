from manim import *
from manim_slides import Slide
from ..constants import FONT_SIZES, STYLE, PRESENTATION_DETAILS

from ..classes.moving_camera_slide import MovingCameraSlide

def intro(scene: MovingCameraSlide):
    
    #  TODO: try and make logos appear first, then shift to the side and give place to the texts
    
    logo_iu = SVGMobject("src/assets/iu-logo.svg").scale(0.5)
    
    module_name = Text(
        PRESENTATION_DETAILS["MODULE_NAME"],
        font_size=FONT_SIZES["TITLE"],
        # font=STYLE["FONT_FAMILY"],
    ).next_to(logo_iu, RIGHT, buff=0.2)
    module_code = Text(
        PRESENTATION_DETAILS["MODULE_CODE"],
        font_size=FONT_SIZES["SUBTITLE"],
        
        # font=STYLE["FONT_FAMILY"],
    ).next_to(module_name, DOWN)
    
    module_group = VGroup(module_name, module_code).arrange(DOWN, buff=0.2).align_to(logo_iu, ORIGIN)
    header_right = VGroup(module_group, logo_iu).arrange(RIGHT, buff=0.5)
    # animate logo_ui moving to its place within header_rigth
    scene.play(Write(logo_iu))
    scene.play(Write(module_group))

    scene.next_slide()
    scene.play(header_right.animate.scale(0.4).to_corner(UR))
    
    initials = Text("IG", font_size=FONT_SIZES["TITLE"], color=BLUE)
    circle = Circle(color=BLUE, radius=0.5).move_to(initials)
    logo = VGroup(initials, circle)
    title = Text(
        PRESENTATION_DETAILS["TITLE"],
        font_size=FONT_SIZES["TITLE"],
        # font=STYLE["FONT_FAMILY"],
    )
    subtitle = Text(
        PRESENTATION_DETAILS["SUBTITLE"],
        font_size=FONT_SIZES["SUBTITLE"],
        # font=STYLE["FONT_FAMILY"],
    ).next_to(title, DOWN)

    titles = VGroup(title, subtitle).arrange(DOWN, buff=0.2)
    header_left = VGroup(logo, titles).arrange(RIGHT, buff=0.2)
    
    scene.play(Write(initials), DrawBorderThenFill(circle), Write(titles))
    scene.next_slide()
    scene.play(header_left.animate.scale(0.4).to_corner(UL))

    header = VGroup(header_left, header_right)
    scene.add_to_canvas(header=header)

    header.save_state()
    scene.play(header.animate.set_opacity(0.5))


class TestScene(Slide):
    def construct(self):
        intro(self)


if __name__ == "__main__":
    subprocess.RUN(["manim", "-p", "ql", "src/slides/intro.py", "TestScene"])
