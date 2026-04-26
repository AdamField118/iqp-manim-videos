"""
Scene 1: Title Card - Acceleration Due to Gravity

From transcript: [MANIM: Title card: "Acceleration Due to Gravity" animates in.]

Duration: ~5 seconds
"""

import sys
sys.path.append('..')

from manim import *
from utils.transitions import fade_in_from_bottom, fade_in_with_scale, staggered_fade_in
from utils.objects import TitleCard, create_logo, BACKGROUND_COLOR

class Scene1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        title_card = TitleCard(
            "Acceleration Due to Gravity",
            "Short Video Projects on Physics Education"
        )
        title_card.move_to(ORIGIN)

        logo = create_logo(scale=0.2)
        logo.to_corner(DR, buff=0.5)

        self.play(fade_in_from_bottom(logo, run_time=1))
        self.wait(0.3)

        if len(title_card) == 3:
            self.play(staggered_fade_in(
                [title_card[0], title_card[1], title_card[2]],
                lag_ratio=0.4, run_time=2
            ))
        else:
            self.play(fade_in_with_scale(title_card, run_time=1.5))

        self.wait(2.5)

        self.play(FadeOut(title_card), FadeOut(logo), run_time=1)
