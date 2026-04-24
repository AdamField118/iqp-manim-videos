"""
Scene 5: Wrapping Up (3:30-4:15)

This scene reviews the key concepts learned and previews the next video.

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
from utils.physics_objects import (
    create_mass,
    create_earth,
    create_ball,
    create_fbd_force_arrows
)


class Scene5(Scene):
    """
    Scene 5: Wrapping Up

    Reviews key concepts:
    - Gravity is universal
    - Depends on mass and distance (inverse square law)
    - Preview: mass cancels, explored in Video 2

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

        # PART 1: Review title (line 192)
        Scene5.review_title(self)
        self.wait(2)

        # PART 2: Key points (lines 193-206)
        Scene5.key_points(self)
        self.wait(2)

        # PART 3: Show the equation one more time (lines 200-201)
        Scene5.show_equation_recap(self)
        self.wait(2)

        # PART 4: End card (lines 214-218)
        Scene5.end_card(self)

        # Hold final frame
        self.wait(3)

    def review_title(self):
        """
        Part 1: Review title
        Line 192: "Let's review what we've learned today"
        """
        title = StyledTitle("What We Learned")
        title.scale(0.7)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title, run_time=1.2))
        self.wait(0.5)

        self.title = title

    def key_points(self):
        """
        Part 2: Show key points with icons
        Lines 193-206: Three main concepts from transcript
        """
        # Point 1: Gravity is universal (lines 195-197)
        icon1_circle1 = Circle(radius=0.2, color=BLUE, fill_opacity=0.5)
        icon1_circle2 = Circle(radius=0.15, color=RED, fill_opacity=0.5).shift(RIGHT * 0.5 + UP * 0.3)
        icon1 = VGroup(
            Circle(radius=0.2, color=BLUE, fill_opacity=0.5),
            Circle(radius=0.15, color=RED, fill_opacity=0.5).shift(RIGHT * 0.5 + UP * 0.3),
            create_fbd_force_arrows(
                icon1_circle1,
                icon1_circle2,
                arrow_length=0.25,
                color=YELLOW,
                stroke_width=4
            )
        )
        icon1.shift(LEFT * 4 + UP * 0.8)

        text1 = StyledText("Gravity is a universal\nforce of attraction")
        text1.scale(0.5)
        text1.next_to(icon1, RIGHT, buff=0.5)

        point1 = VGroup(icon1, text1)

        # Point 2: Inverse square law (lines 198-201)
        icon2 = MathTex("F \\propto \\frac{m_1 m_2}{r^2}", font_size=36, color=ACCENT_COLOR)
        icon2.shift(LEFT * 4 + DOWN * 0.3)

        text2 = StyledText("Inverse square law:\ndouble distance → ¼ force")
        text2.scale(0.5)
        text2.next_to(icon2, RIGHT, buff=0.5)

        point2 = VGroup(icon2, text2)

        # Point 3: All objects fall at same rate (lines 202-206)
        icon3_ball1 = create_ball(radius=0.15, color=ORANGE, pattern=False)
        icon3_ball2 = create_ball(radius=0.1, color=GREEN, pattern=False)
        icon3_ball1.shift(LEFT * 0.2)
        icon3_ball2.shift(RIGHT * 0.2)
        icon3_arrow = Arrow(UP * 0.3, DOWN * 0.3, color=YELLOW, stroke_width=3, buff=0)
        icon3 = VGroup(icon3_ball1, icon3_ball2, icon3_arrow)
        icon3.shift(LEFT * 4 + DOWN * 1.4)

        text3 = StyledText("All objects fall at\nthe SAME rate!")
        text3.scale(0.5)
        text3.next_to(icon3, RIGHT, buff=0.5)
        text3.set_color(ACCENT_COLOR)

        point3 = VGroup(icon3, text3)

        self.play(
            LaggedStart(
                FadeIn(point1, shift=RIGHT * 0.3),
                FadeIn(point2, shift=RIGHT * 0.3),
                FadeIn(point3, shift=RIGHT * 0.3),
                lag_ratio=0.5,
                run_time=3
            )
        )
        self.wait(2)

        self.play(
            FadeOut(self.title),
            FadeOut(point1),
            FadeOut(point2),
            FadeOut(point3),
            run_time=0.8
        )

    def show_equation_recap(self):
        """
        Part 3: Show the gravitational force equation one more time
        Lines 200-201: [MANIM: Show the equation again]
        """
        title = StyledText("The Law of Universal Gravitation:")
        title.scale(0.65)
        title.to_edge(UP, buff=0.5)
        title.set_color(ACCENT_COLOR)

        self.play(FadeIn(title))

        equation = MathTex(
            "F = G \\frac{m_1 m_2}{r^2}",
            font_size=72
        )
        equation.shift(UP * 0.3)

        self.play(FadeIn(equation, scale=1.1))
        self.wait(0.5)

        inverse_sq = StyledText("Double the distance → Force is ¼ as strong")
        inverse_sq.scale(0.6)
        inverse_sq.next_to(equation, DOWN, buff=0.6)
        inverse_sq.set_color(WHITE)

        self.play(FadeIn(inverse_sq))
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(equation),
            FadeOut(inverse_sq),
            run_time=0.8
        )

    def end_card(self):
        """
        Part 4: End card
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