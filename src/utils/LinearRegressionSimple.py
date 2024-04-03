from manim import *
import numpy as np
from ..classes.moving_camera_slide import MovingCameraSlide

class LinearRegressionSimple():
    def __init__(self, scene:MovingCameraSlide):
        # scene is the scene where the graph will be rendered 
        self.scene = scene
        
        max_x = 5
        n = 10
        fc = lambda x: x + np.random.normal(0, 0.6, n)
        x = np.linspace(0.1, max_x, n)
        y = fc(x)
        
        self.axes = Axes(
            x_range=[0, max_x, 1],
            y_range=[0, y[-1], 1],
            axis_config={"include_tip": False},
            x_length=5,
            y_length=5,
            tips=False
        )
        
        self.dots = VGroup(*[Dot(self.axes.c2p(x[i], y[i])) for i in range(len(x))])
        
        reg_params = self.get_regression_params(x,y)
        
        self.func = lambda x: reg_params[0]*x + reg_params[1]
        
        self.line = self.axes.plot(self.func, color=RED, stroke_width=1.5)
        
        self.error_lines = VGroup(*[Line(self.dots[i].get_center(), self.axes.c2p(x[i], self.func(x[i])), stroke_width=1) for i in range(len(x))])
        
    def get_regression_params(self, x, y):
        return np.polyfit(x, y, 1)
    
    def render_animated(self):
        self.scene.play(Write(self.axes))
        self.scene.play(Write(self.dots))
        self.scene.play(Write(self.line))
        self.scene.play(Write(self.error_lines))
        
    def render_static(self):
        self.scene.add(self.axes)
        self.scene.add(self.dots)
        self.scene.add(self.line)
        self.scene.add(self.error_lines)
        
    def get_graph(self):
        graph = VGroup(self.axes, self.dots, self.line, self.error_lines)
        graph.render_animated = self.render_animated
        return graph