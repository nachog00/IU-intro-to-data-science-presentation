from manim import *
import numpy as np

COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, PINK]


class SemiSupervisedGraph:
    def __init__(self):

        np.random.seed(8)
        self.n = 40
        self.k = 2
        self.min = -1
        self.max = 1
        self.num_flying_points = 5

        self.axes = self.get_axes()
        self.centroids = self.get_centroids()
        self.points = self.get_random_points()
        self.middle_line = self.get_middle_line()
        self.flying_points_cluster = self.get_flying_points()

    def get_axes(self):
        return Axes(
            x_range=[self.min, self.max, 1],
            y_range=[self.min, self.max, 1],
            axis_config={"include_tip": False},
            x_length=6,
            y_length=6,
        ).set_opacity(0.6)

    def get_centroids(self):
        angle = 2 * np.pi / self.k
        radius = 0.5
        # generate the points, and add them within the axes coordinates
        return VGroup(
            *[
                Dot(
                    self.axes.c2p(
                        *[np.cos(angle * i) * radius, np.sin(angle * i) * radius, 1]
                    ),
                    radius=0.05,
                    color=COLORS[i],
                )
                for i in range(self.k)
            ]
        )

    def get_random_points(self):
        # generate the points, and add them within the axes coordinates
        points = []
        # iterate over the centroids and generate n/k points for each centroid
        for i in range(self.k):
            centroid = self.centroids[i].get_center()
            group = VGroup(
                *[
                    Dot(
                        centroid + self.axes.c2p(*np.random.normal(0, 0.1, 2)),
                        radius=0.05,
                        fill_opacity=0.8,
                        color=COLORS[i],
                    )
                    for j in range(self.n)
                ]
            )
            points.append(group)

        return VGroup(*points)

    def get_middle_line(self):
        self.upper_point = self.axes.c2p(0, 1)
        self.lower_point = self.axes.c2p(0, -1)
        return DashedLine(
            self.upper_point, self.lower_point, color=WHITE, stroke_width=1.5
        )

    def get_flying_points(self):
        # create a cluster of points that come from the upper middle line into either of the clusters
        self.flying_points = [
            Dot(
                self.upper_point + self.axes.c2p(*np.random.normal(0, 0.05, 2)),
                radius=0.05,
                fill_opacity=0.8,
                color=WHITE,
            )
            for j in range(self.num_flying_points)
        ]
        return VGroup(*self.flying_points)

    def assign_flying_points(self):
        # assign the flying points to a random centroid
        for point in self.flying_points:
            point.target = self.centroids[
                np.random.randint(0, self.k)
            ].get_center() + self.axes.c2p(*np.random.normal(0, 0.03, 2))

    def move_flying_points(self, scene):
        self.assign_flying_points()
        # move the flying points to their target
        for point in self.flying_points:
            scene.play(
                MoveAlongPath(point, ArcBetweenPoints(point.get_center(), point.target))
            )

    def render_animated(self, scene):
        # scene.play(Write(self.axes))
        scene.play(FadeIn(self.middle_line))
        scene.play(
            Write(self.centroids), Write(self.points), Write(self.flying_points_cluster)
        )
        self.move_flying_points(scene)

    def render_static(self, scene):
        scene.add(
            self.middle_line, self.centroids, self.points, self.flying_points_cluster
        )

    def get_graph(self):
        graph = VGroup(
            self.centroids, self.points, self.flying_points_cluster, self.middle_line
        )
        graph.render_animated = self.render_animated
        return graph
