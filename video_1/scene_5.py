"""
Scene 5: Wrapping Up (3:30-4:15)

The review dialogue in this scene is live-action. Manim provides only
the end card at the close.

From PDF transcript lines 187-218.
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
    StyledText,
    StyledTitle,
    create_logo,
    BACKGROUND_COLOR,
    ACCENT_COLOR,
    TEXT_COLOR,
    PRIMARY_COLOR
)


class Scene5(Scene):
    """
    Scene 5: Wrapping Up

    Live-action review, followed by:
    [MANIM: Fade to end card]

    Duration: 3:30-4:15 (45 seconds)
    From PDF lines 187-218

    To render this scene, run:
    python -m manim -pqh "video_1/scene_5.py" Scene5
    """

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        """All scene animation logic. Called by construct() and importable by full_video.py."""

        # Add persistent logo
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        # [MANIM: Fade to end card]
        Scene5.end_card(self)

        # Hold final frame
        self.wait(3)

    def end_card(self):
        """
        End card
        Lines 214-218: Fade to end card with channel/project info
        """
        large_logo = create_logo(scale=0.4)
        large_logo.shift(UP * 1.2)

        project_title = StyledTitle("Short Video Projects")
        project_title.scale(0.6)
        project_title.next_to(large_logo, DOWN, buff=0.8)

        subtitle = StyledText("Physics Education Series")
        subtitle.scale(0.6)
        subtitle.next_to(project_title, DOWN, buff=0.3)

        thanks = StyledText("Thanks for watching!")
        thanks.scale(0.7)
        thanks.shift(DOWN * 1.8)
        thanks.set_color(ACCENT_COLOR)

        acknowledgment = StyledText("With guidance from Prof. Noviello & Prof. Kafle")
        acknowledgment.scale(0.4)
        acknowledgment.to_edge(DOWN, buff=0.5)
        acknowledgment.set_opacity(0.7)

        self.play(FadeIn(large_logo, scale=0.8, run_time=1.5))
        self.play(
            Write(project_title, run_time=1),
            FadeIn(subtitle, shift=UP * 0.2)
        )
        self.wait(0.5)
        self.play(FadeIn(thanks))
        self.wait(0.8)
        self.play(FadeIn(acknowledgment))