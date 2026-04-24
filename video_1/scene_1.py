"""
Scene 1: Title Card - Universal Gravitation

This is the opening title card for Video 1 of the IQP Physics Education project.
The title card introduces the topic "Universal Gravitation" with an elegant animation.

From the transcript (lines 38-40), this scene appears after the live-action hook
where balls are dropped, transitioning into the manim animation portion.
"""

import sys
sys.path.append('..')

from manim import *
from utils.transitions import (
    fade_in_from_bottom,
    fade_in_with_scale,
    staggered_fade_in
)
from utils.objects import (
    TitleCard,
    create_logo,
    BACKGROUND_COLOR
)


class Scene1(Scene):
    """
    Scene 1: Title Card - "Universal Gravitation"

    From PDF transcript lines 38-40:
    [VISUAL: Fade to manim animation]
    [MANIM: Title card with "Universal Gravitation" animates in]

    Duration: ~5 seconds total

    To render this scene, run:
    python -m manim -pqh "video_1/scene_1.py" Scene1
    """

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        """All scene animation logic. Called by construct() and importable by full_video.py."""

        # Create the title card - "Universal Gravitation" from PDF
        title_card = TitleCard(
            "Universal Gravitation",
            "Short Video Projects on Physics Education"
        )

        # Add logo in bottom right corner
        logo = create_logo(scale=0.2)
        logo.to_corner(DR, buff=0.5)

        # Position title card in center
        title_card.move_to(ORIGIN)

        # 1. Fade in logo from bottom
        self.play(fade_in_from_bottom(logo, run_time=1))
        self.wait(0.3)

        # 2. Animate in the title card elements with stagger
        if len(title_card) == 3:
            title_elements = [title_card[0], title_card[1], title_card[2]]
            self.play(staggered_fade_in(title_elements, lag_ratio=0.4, run_time=2))
        else:
            self.play(fade_in_with_scale(title_card, run_time=1.5))

        # 3. Hold on the title card
        self.wait(2.5)

        # 4. Fade out before next scene
        self.play(
            FadeOut(title_card),
            FadeOut(logo),
            run_time=1
        )