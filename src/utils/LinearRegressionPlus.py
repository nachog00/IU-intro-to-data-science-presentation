from manim import *
import numpy as np
from ..classes.moving_camera_slide import MovingCameraSlide
from ..constants import FONT_SIZES


class LinearRegressionPlus:
    def __init__(self, scene: MovingCameraSlide):
        # scene is the scene where the graph will be rendered
        self.scene = scene

        max_x = 5
        n = 8
        fc = lambda x: 1 + 0.4 * x + np.random.normal(0, 0.6, n)
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
                    DashedLine(
                        self.dots[i].get_center(),
                        self.axes.c2p(self.x[i], self.func(self.x[i])),
                        stroke_width=1.5,
                    )
                    for i in range(len(self.x))
                ]
            )
        ).set_color(YELLOW)

        self.error_text = (
            VGroup(
                VGroup(
                    Text("Slope: ", font_size=FONT_SIZES["SUBTITLE"]),
                    DecimalNumber(self.actual_slope).add_updater(
                        lambda x: x.set_value(self.slope.get_value())
                    ),
                ).arrange(RIGHT, buff=0.5),
                                VGroup(
                    Text("Intercept: ", font_size=FONT_SIZES["SUBTITLE"]),
                    DecimalNumber(self.actual_intercept).add_updater(
                        lambda x: x.set_value(self.intercept.get_value())
                    ),
                ).arrange(RIGHT, buff=0.5),
                Text("Mean Squared Error: ", font_size=FONT_SIZES["SUBTITLE"]),
                DecimalNumber(self.get_mse()).add_updater(
                    lambda x: x.set_value(self.get_mse())
                ),
            )
            .set_color(GREEN_D)
            .arrange(DOWN, buff=0.5)
        )

        self.graph_group = VGroup(self.axes, self.dots, self.line, self.error_lines)

        self.layout = VGroup(self.graph_group, self.error_text).arrange_in_grid(
            rows=1, cols=2, buff=0.5
        )

    def get_regression_params(self):
        return np.polyfit(self.x, self.y, 1)

    def get_mse(self):
        return np.mean((self.y - self.func(self.x)) ** 2)

    def render_animated(self):
        self.scene.play(Write(self.axes))
        self.scene.play(Write(self.dots))
        self.scene.play(Write(self.line))
        self.scene.play(Write(self.error_lines), Write(self.error_text))

        # animate the slope and intercept
        self.scene.play(
            self.slope.animate.set_value(self.actual_slope * 1.3),
            self.intercept.animate.set_value(self.actual_intercept * 0.8),
        )
        self.scene.play(
            self.slope.animate.set_value(self.actual_slope / 0.8),
            self.intercept.animate.set_value(self.actual_intercept / 2),
        )
        self.scene.play(
            self.slope.animate.set_value(self.actual_slope),
            self.intercept.animate.set_value(self.actual_intercept),
        )

        # self.scene.play(
        #     Indicate(self.error_lines)
        # )

    def render_static(self):
        self.scene.add(self.axes)
        self.scene.add(self.dots)
        self.scene.add(self.line)
        self.scene.add(self.error_lines)

    def get_graph(self):
        graph = self.layout
        graph.render_animated = self.render_animated
        return graph
