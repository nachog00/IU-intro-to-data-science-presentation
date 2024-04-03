from manim import *
from ..classes.moving_camera_slide import MovingCameraSlide


def zoom_loop(
    scene: MovingCameraSlide,
    obj: VGroup,
    zoom_speed: float = None,
    scale_factor: float = 0.5,
    wait_time: float = None,
    next_slide: bool = False,
):
    """
    Zooms in on each object in the given VGroup using the MovingCameraSlide scene.

    Parameters:
        scene (MovingCameraSlide): The scene in which the zooming animation will be performed.
        obj (VGroup): The VGroup containing the objects to zoom in on.
        next_slide (bool, optional): Whether wait for the next slide after each zoom animation. Defaults to False.
        scale_factor (float, optional): The scale factor to apply to each object. Defaults to 0.5.
        wait_time (float, optional): The amount of time to wait after each zoom animation. Defaults to 1.
        zoom_speed (float, optional): The speed of the zoom animation. Defaults to 0.5.
    """
    scene.camera.frame.save_state()
    for item in obj:
        scene.play(
            scene.camera.frame.animate.scale(scale_factor).move_to(item),
            run_time=zoom_speed if zoom_speed else 1,
        )
        if next_slide:
            scene.next_slide()
        else:
            scene.wait(wait_time if wait_time else 1)
        scene.play(Restore(scene.camera.frame))
