from manim import config
from .classes.moving_camera_slide import MovingCameraSlide
def config(scene:MovingCameraSlide):
    # scene.camera.background_color = "#ece6e2"
    scene.small_wait = lambda : scene.wait(0.5)
    scene.medium_wait = lambda : scene.wait(1)
    scene.long_wait = lambda : scene.wait(2)
