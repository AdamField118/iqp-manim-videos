"""
video_3/scene_1.py
Scene 1: Title Card + Newton Crack (0:00--~0:27)

Replaces: whiteboard writing of "Newton's Gravity" + underline + crack symbol.

Part A: Title card "Beyond Newton: Einstein's Revolution"
Part B: Newton plaque with crack lines (cut in at ~00:21, "That's how good it was.")

To render this scene:
    python -m manim -pqh "video_3/scene_1.py" Scene1 --media_dir "./video_3/media"
"""

import sys
sys.path.append('..')

from manim import *
from utils.transitions import fade_in_from_bottom, fade_in_with_scale, staggered_fade_in
from utils.objects import TitleCard, create_logo, BACKGROUND_COLOR, ACCENT_COLOR, TEXT_COLOR


class Scene1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        Scene1.title_card(self)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def title_card(self):
        """
        Opening title card matching Video 1 / Video 2 style.
        Duration: ~5 s
        """
        title_card = TitleCard(
            "Beyond Newton: Einstein's Gravity",
            "Short Video Projects on Physics Education"
        )
        title_card[0].scale_to_fit_width(config["frame_width"] - 2)
        title_card.move_to(ORIGIN)

        if len(title_card) == 3:
            self.play(staggered_fade_in(
                [title_card[0], title_card[1], title_card[2]],
                lag_ratio=0.4, run_time=2
            ))
        else:
            self.play(fade_in_with_scale(title_card, run_time=1.5))

        self.wait(2.5)
        self.play(FadeOut(title_card), run_time=0.8)