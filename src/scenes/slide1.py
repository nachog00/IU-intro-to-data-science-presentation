from manim import *
from ..classes.moving_camera_slide import MovingCameraSlide
from ..utils.zoom_loop import zoom_loop
from ..utils.LinearRegressionSimple import LinearRegressionSimple
from ..utils.KMeansGraph import KMeansGraph
from ..constants import FONT_SIZES


def slide1(scene: MovingCameraSlide):
    slide_title = Text("ML Paradigms")
    scene.play(Write(slide_title))
    scene.next_slide(notes="Don't forget to tell about this!!!!!")
    scene.play(slide_title.animate.scale(0.5).to_edge(UP))

    header = scene.canvas["header"]
    sections_data = [
        {
            "title": "Supervised\nLearning",
            "sub": LinearRegressionSimple(scene),
            "texts": [
                "Has target outcomes",
                "Aims to predict outcomes",
                "Minimizes Loss Function",
                "$\mathcal{L} = \sum_{i=1}^{n} (y_i - \hat{y_i})^2$",
            ],
        },
        {
            "title": "Unsupervised\nLearning",
            "sub": KMeansGraph(scene),
            "texts": [
                "No target outcomes",
                "Aims to find patterns",
                "Minimizes some Distance Function",
            ],
        },
        {
            "title": "Semi-Supervised\nLearning",
            "sub": LinearRegressionSimple(scene),
            "texts": [
                "Has some target outcome data",
                "Iteratively adds labels to unlabeled data",
                "Mix of supervised and unsupervised learning",
            ],
        },
    ]

    def section_obj(data):
        return VGroup(
            Text(data["title"], font_size=FONT_SIZES["TITLE"], color=WHITE),
            data["sub"].get_graph(),
            VGroup(
                *map(
                    lambda text: Tex(text, font_size=FONT_SIZES["TITLE"], color=WHITE),
                    data["texts"],
                )
            ).arrange(DOWN),
        ).arrange(DOWN, buff=0.5)

    sections = (
        VGroup(*map(section_obj, sections_data))
        .arrange(RIGHT, buff=3)
        .scale_to_fit_width(10)
    ).next_to(header, DOWN, buff=1)
    
    def animation (section):
        title, graph, texts = section
        scene.play(Write(title))
        graph.render_animated()
        scene.play(Write(texts))

    scene.next_slide()

    zoom_loop(scene, sections, animation, next_slide=True)
    
    scene.next_slide()
    
    scene.wipe(sections, slide_title )
