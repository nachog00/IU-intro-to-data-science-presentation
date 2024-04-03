import subprocess


def render_slides(scenes):
    try:
        # Run the manim render CLI command
        subprocess.run(["manim", "render", "presentation.py", "-ql", *scenes])
    except FileNotFoundError:
        print("Manim is not installed. Please install it using 'pip install manim'.")


def generate_html_presentation(scenes, output_file):
    try:
        # Run the manim-slides convert CLI command
        subprocess.run(["manim-slides", "convert", "--use-template" , "src\\template.html" , *scenes, output_file ])
        # print("HTML presentation generated successfully!")
    except FileNotFoundError:
        print(
            "manim-slides is not installed. Please install it using 'pip install manim-slides'."
        )


if __name__ == "__main__":
    scenes = ["Presentation"]
    render_slides(scenes)
    generate_html_presentation(scenes, "_site/index.html")
