"""
Scene 6: Wrapping Up (4:50--5:30)

Transcript Manim tag: [MANIM: Fade to end card.]
Live-action review precedes this — no other Manim content in this scene.
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import (
    StyledText, StyledTitle, create_logo,
    BACKGROUND_COLOR, ACCENT_COLOR
)

class Scene6(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        Scene6.end_card(self)
        self.wait(3)

    def end_card(self):
        large_logo = create_logo(scale=0.4)
        large_logo.shift(UP * 1.2)

        project_title = StyledTitle("Short Video Projects")
        project_title.scale(0.6)
        project_title.next_to(large_logo, DOWN, buff=0.8)

        subtitle = StyledText("Physics Education Series")
        subtitle.scale(0.6)
        subtitle.next_to(project_title, DOWN, buff=0.3)

        thanks = StyledText("Thanks for watching!")
        thanks.scale(0.7).shift(DOWN * 1.8)
        thanks.set_color(ACCENT_COLOR)

        acknowledgment = StyledText("With guidance from Prof. Noviello & Prof. Kafle")
        acknowledgment.scale(0.4).to_edge(DOWN, buff=0.5).set_opacity(0.7)

        self.play(FadeIn(large_logo, scale=0.8, run_time=1.5))
        self.play(
            Write(project_title, run_time=1),
            FadeIn(subtitle, shift=UP * 0.2)
        )
        self.wait(0.5)
        self.play(FadeIn(thanks))
        self.wait(0.8)
        self.play(FadeIn(acknowledgment))
