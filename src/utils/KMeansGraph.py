from manim import *
import numpy as np

COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, PINK]

class KMeansGraph():
    def __init__(self):
        
        np.random.seed(8)
        self.n = 40
        self.k = 3
        self.min = -1
        self.max = 1
        
        self.axes = self.get_axes()
        self.centroids = self.get_centroids()
        self.points = self.get_random_points()
        
    def get_axes(self):
        return Axes(
            x_range=[self.min, self.max, 1],
            y_range=[self.min, self.max, 1],
            axis_config={"include_tip": False},
            x_length=6,
            y_length=6,
        ).set_opacity(0.6)
    
    def get_centroids(self):
        angle = 2*np.pi/self.k
        radius = 0.5
        # generate the points, and add them within the axes coordinates
        return VGroup(*[Dot(self.axes.c2p(*[np.cos(angle * i) * radius , np.sin(angle * i) * radius , 1]) , radius=0.05 , color=COLORS[i]) for i in range(self.k)])
    
    def get_random_points(self):
        # generate the points, and add them within the axes coordinates
        points = []
        # iterate over the centroids and generate n/k points for each centroid
        for i in range(self.k):
            centroid = self.centroids[i].get_center()
            group = VGroup(*[Dot(centroid + self.axes.c2p(*np.random.normal(0,0.15,2)) , radius=0.05 , fill_opacity=0.8 , color=COLORS[i]) for j in range(self.n)])
            points.append(group)
            
        return VGroup(*points)
    
    
    def render_animated( self , scene ):
        scene.play(Write(self.axes))
        scene.play(Write(self.centroids) , Write(self.points))
        
        
    def render_static( self, scene ):
        scene.add(self.axes , self.centroids , self.points)
        
    def get_graph(self):
        graph = VGroup(self.axes , self.centroids , self.points)
        graph.render_animated = self.render_animated
        return graph