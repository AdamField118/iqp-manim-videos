"""
video_3/scene_6.py
Scene 6: Wrapping Up -- End Card (4:55--end)

Replaces: whiteboard presence + tapping the circled Wheeler quote.
Shows a callback to the Wheeler quote, then standard end card.

To render:
    python -m manim -pqh "video_3/scene_6.py" Scene6 --media_dir "./video_3/media"
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import StyledText, StyledTitle, create_logo, BACKGROUND_COLOR, ACCENT_COLOR


class Scene6(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        Scene6.wheeler_callback(self)
        Scene6.end_card(self)
        self.wait(3)

    def wheeler_callback(self):
        """
        Replaces: presenter tapping circled Wheeler quote on board.
        Duration: ~8 s
        """
        line1 = Text(
            '"Mass tells spacetime how to curve;',
            font_size=32, color=GREY_B,
        )
        line2 = Text(
            'curved spacetime tells matter how to move."',
            font_size=32, color=GREY_B,
        )
        line1.move_to(UP * 0.5)
        line2.next_to(line1, DOWN, buff=0.35)

        # Pulse highlight to simulate the board tap
        glow_box = SurroundingRectangle(
            VGroup(line1, line2),
            color=ACCENT_COLOR, buff=0.2, stroke_width=2.5, corner_radius=0.1,
        )

        self.play(FadeIn(line1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=0.6)
        self.wait(0.5)
        self.play(Create(glow_box), run_time=0.7)
        self.play(
            glow_box.animate.set_stroke(color=WHITE, opacity=0.0),
            run_time=1.0,
        )
        self.wait(1.5)
        self.play(FadeOut(line1), FadeOut(line2), FadeOut(glow_box), run_time=0.8)

    def end_card(self):
        """Standard end card matching Video 1 / Video 2."""
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
            FadeIn(subtitle, shift=UP * 0.2),
        )
        self.wait(0.5)
        self.play(FadeIn(thanks))
        self.wait(0.8)
        self.play(FadeIn(acknowledgment))
