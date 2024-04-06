from manim import *
import numpy as np
from ..classes.moving_camera_slide import MovingCameraSlide
from ..constants import FONT_SIZES


class LinearRegressionPlus:
    def __init__(self):
        
        np_gen = np.random.default_rng(seed=29)
        max_x = 5
        n = 8
        fc = lambda x: 0 + 0.8 * x + np_gen.normal(0, 0.4, n) * x
        self.x = np.linspace(0.5, max_x - 0.5, n)
        self.y = fc(self.x)

        self.axes = Axes(
            x_range=[0, max_x, 1],
            y_range=[0, self.y[-1] * 1.5, 1],
            axis_config={"include_tip": False},
            x_length=5,
            y_length=5,
            tips=False,
        )

        y_label = self.axes.get_y_axis_label("y", edge=LEFT, direction=LEFT)
        x_label = self.axes.get_x_axis_label("x")
        self.labels = VGroup(x_label, y_label)

        self.dots = VGroup(
            *[Dot(self.axes.c2p(self.x[i], self.y[i])) for i in range(len(self.x))]
        )

        reg_params = self.get_regression_params()

        self.actual_slope = reg_params[0]
        self.actual_intercept = reg_params[1]

        self.slope = ValueTracker(self.actual_slope)
        self.intercept = ValueTracker(self.actual_intercept)
        self.func = lambda x: self.slope.get_value() * x + self.intercept.get_value()

        self.line = always_redraw(
            lambda: self.axes.plot(self.func, color=RED, stroke_width=1.5)
        )

        self.error_lines = always_redraw(
            lambda: VGroup(
                *[
                    Line(
                        self.dots[i].get_center(),
                        self.axes.c2p(self.x[i], self.func(self.x[i])),
                        stroke_width=2,
                        color=YELLOW,
                    )
                    for i in range(len(self.x))
                ]
            )
        ).set_color(YELLOW)

        min_mse = self.get_mse()

        self.error_text = (
            VGroup(
                # y = mx + b
                Text(
                    f"y(x) = {self.slope.get_value():.2}x + {self.intercept.get_value():.2}",
                    font_size=FONT_SIZES["SUBTITLE"],
                    color=RED,
                ),
                VGroup(
                    Tex(
                        "MSE =",
                        font_size=FONT_SIZES["SUBTITLE"],
                        color=YELLOW,
                    ),
                    DecimalNumber(
                        self.get_mse(), num_decimal_places=4, color=YELLOW
                    ).add_updater(
                        lambda x: x.set_value(self.get_mse()).set_font_size(
                            FONT_SIZES["SUBTITLE"] * min(self.get_mse() / min_mse, 2)
                        )
                    ),
                ).arrange(RIGHT, buff=0.5),
            ).arrange(DOWN, buff=0.5)
        ).add_updater(
            lambda x: x[0].become(
                Text(
                    f"y(x) = {self.slope.get_value():.2}x + {self.intercept.get_value():.2}",
                    font_size=FONT_SIZES["SUBTITLE"],
                    color=RED,
                ).next_to(x[1], UP, buff=0.5)
            )
        )

        self.graph_group = VGroup(
            self.axes, self.labels, self.dots, self.line, self.error_lines
        )

        self.layout = VGroup(self.graph_group, self.error_text).arrange_in_grid(
            rows=1, cols=2, buff=1
        )

    def get_regression_params(self):
        return np.polyfit(self.x, self.y, 1)

    def get_mse(self):
        return np.mean((self.y - self.func(self.x)) ** 2)

    def render_animated(self, scene):
        scene.play(Write(self.axes), Write(self.labels))
        scene.play(Write(self.dots))
        scene.next_slide()
        scene.play(Write(self.line), Write(self.error_text[0]))
        scene.next_slide()
        scene.play(Write(self.error_lines), Write(self.error_text[1]))

        scene.next_slide(notes="Showcase the error changing as the line changes")

        # animate the slope and intercept
        scene.play(
            self.slope.animate.set_value(self.actual_slope * 1.3),
            self.intercept.animate.set_value(self.actual_intercept - 0.5),
        )
        scene.next_slide()
        scene.play(
            self.slope.animate.set_value(-0.4),
            self.intercept.animate.set_value(self.actual_intercept + 2),
        )
        scene.next_slide()
        scene.play(
            self.slope.animate.set_value(self.actual_slope),
            self.intercept.animate.set_value(self.actual_intercept),
        )
        scene.next_slide()
        self.moddify_to_example(scene)

    def moddify_to_example(self, scene):
        # change the labels from y and x to real world examples
        scene.play(Transform(self.labels[0], self.axes.get_x_axis_label("x [mm]")))
        scene.play(Transform(self.labels[1], self.axes.get_y_axis_label("F [kN]")))
        
        # formula_text = Text(
        #             f"F(x) = {self.slope.get_value():.2}x + {self.intercept.get_value():.2}",
        #             font_size=FONT_SIZES["SUBTITLE"],
        #             color=RED,
        #         )
        # k_text = Tex(
        #             "k={:.2}".format(self.slope.get_value()),
        #         )
        
        scene.next_slide(notes="")
        
        scene.play(
            Transform(
                self.error_text[0],
                Tex(
                    fr"$F(x) = {self.slope.get_value():.2} \frac{{kN}}{{mm}}x + {self.intercept.get_value():.2} kN$",
                    font_size=FONT_SIZES["SUBTITLE"],
                    color=RED,
                ).next_to(self.error_text[1], UP, buff=0.5)
            ),
        )

    def FadeOut(self, scene):
        self.error_text.clear_updaters()
        scene.play(FadeOut(self.graph_group), FadeOut(self.error_text))

    def render_static(self, scene):
        scene.add(self.axes)
        scene.add(self.dots)
        scene.add(self.line)
        scene.add(self.error_lines)

    def get_graph(self):
        graph = self.layout
        graph.render_animated = self.render_animated
        graph.fade_out = self.FadeOut
        return graph
