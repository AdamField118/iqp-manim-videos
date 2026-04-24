"""
Scene 4: Connection to Falling (2:45-3:30)

This is a bridging scene that connects gravitational force to acceleration
and previews the mass cancellation that will be covered in Video 2.

From PDF transcript lines 167-185.
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


class Scene4(Scene):
    """
    Scene 4: Connection to Falling (2:45-3:30)

    Bridges gravitational force to the question of why objects fall at the same rate.
    Previews the mass cancellation derivation from Video 2.

    From PDF lines 167-185:
    - Restate: we know the force, but why do the balls fall at the same rate?
    - Preview: set F_gravity = F_Newton to show mass cancellation is coming
    - Tease Video 2

    Duration: 2:45-3:30 (45 seconds)

    To render this scene, run:
    python -m manim -pqh "video_1/scene_4.py" Scene4
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

        # PART 1: Restate the question (lines 169-175)
        Scene4.restate_question(self)

        # PART 2: Preview the mass cancellation (lines 176-184)
        Scene4.preview_mass_cancellation(self)

        # PART 3: Tease Video 2 (line 185)
        Scene4.tease_next_video(self)

        # Hold final frame
        self.wait(2)

        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def restate_question(self):
        """
        Part 1: Restate the original question
        Lines 169-175: "We know gravity pulls harder on the heavier ball.
        But why do they still hit the ground at the same time?"
        """
        # Show both balls side by side
        basketball = create_ball(radius=0.45, color=ORANGE, pattern=True)
        basketball.shift(LEFT * 2.5)

        tennis_ball = create_ball(radius=0.25, color=GREEN, pattern=True)
        tennis_ball.shift(RIGHT * 2.5)

        bb_label = StyledText("Basketball")
        bb_label.scale(0.5)
        bb_label.next_to(basketball, DOWN, buff=0.3)

        tb_label = StyledText("Tennis ball")
        tb_label.scale(0.5)
        tb_label.next_to(tennis_ball, DOWN, buff=0.3)

        self.play(
            FadeIn(basketball, scale=0.5),
            FadeIn(tennis_ball, scale=0.5),
            FadeIn(bb_label),
            FadeIn(tb_label)
        )
        self.wait(0.5)

        # Show FBD arrows: bigger arrow on basketball (more force)
        # Basketball: larger force arrow (bigger mass)
        bb_arrow = Arrow(
            basketball.get_center(),
            basketball.get_bottom() + DOWN * 1.2,
            color=YELLOW,
            stroke_width=10,
            buff=0
        )
        tb_arrow = Arrow(
            tennis_ball.get_center(),
            tennis_ball.get_bottom() + DOWN * 0.6,
            color=YELLOW,
            stroke_width=5,
            buff=0
        )

        bb_force_label = MathTex("F_{big}", font_size=36, color=YELLOW)
        bb_force_label.next_to(bb_arrow, LEFT, buff=0.15)
        tb_force_label = MathTex("F_{small}", font_size=36, color=YELLOW)
        tb_force_label.next_to(tb_arrow, RIGHT, buff=0.15)

        self.play(
            Create(bb_arrow),
            Create(tb_arrow),
            FadeIn(bb_force_label),
            FadeIn(tb_force_label)
        )
        self.wait(0.5)

        # The question
        question = StyledText("Earth pulls harder on the basketball...")
        question.scale(0.65)
        question.to_edge(UP, buff=0.5)
        self.play(Write(question, run_time=1.2))
        self.wait(1)

        question2 = StyledText("So why do they fall at the SAME rate?")
        question2.scale(0.65)
        question2.next_to(question, DOWN, buff=0.3)
        question2.set_color(ACCENT_COLOR)
        self.play(Write(question2, run_time=1.2))
        self.wait(1.5)

        self.play(
            *[FadeOut(mob) for mob in [
                basketball, tennis_ball, bb_label, tb_label,
                bb_arrow, tb_arrow, bb_force_label, tb_force_label,
                question, question2
            ]],
            run_time=0.8
        )

    def preview_mass_cancellation(self):
        """
        Part 2: Preview mass cancellation animation (lines 176-184)
        [MANIM: Preview animation showing the mass cancellation that will be covered in Video 2]

        Shows both equations side by side, hints that setting them equal
        causes the mass to cancel — but doesn't fully derive it yet.
        """
        title = StyledText("Here's the key insight...")
        title.scale(0.7)
        title.to_edge(UP, buff=0.5)
        title.set_color(ACCENT_COLOR)
        self.play(FadeIn(title))

        # Show gravity equation: F = G * M_Earth * m / r²
        gravity_eq = MathTex(
            "F_{gravity} = G \\frac{M_{Earth} \\cdot m}{r^2}",
            font_size=48
        )
        gravity_eq.shift(UP * 0.8 + LEFT * 0.5)

        gravity_eq_label = StyledText("Gravitational Force")
        gravity_eq_label.scale(0.45)
        gravity_eq_label.next_to(gravity_eq, DOWN, buff=0.2)
        gravity_eq_label.set_color(GREY_A)

        self.play(Write(gravity_eq, run_time=1.2))
        self.play(FadeIn(gravity_eq_label))
        self.wait(0.8)

        # Show Newton's 2nd law: F = m * a
        newton_eq = MathTex(
            "F = m \\cdot a",
            font_size=48
        )
        newton_eq.shift(DOWN * 0.5 + LEFT * 0.5)

        newton_eq_label = StyledText("Newton's Second Law")
        newton_eq_label.scale(0.45)
        newton_eq_label.next_to(newton_eq, DOWN, buff=0.2)
        newton_eq_label.set_color(GREY_A)

        self.play(Write(newton_eq, run_time=1.2))
        self.play(FadeIn(newton_eq_label))
        self.wait(0.8)

        # Draw brace/arrow showing they can be set equal
        set_equal_text = StyledText("Set these equal →")
        set_equal_text.scale(0.55)
        set_equal_text.shift(RIGHT * 3.5 + UP * 0.15)
        set_equal_text.set_color(YELLOW)

        self.play(FadeIn(set_equal_text))
        self.wait(0.5)

        # Preview the combined equation: G * M * m / r² = m * a
        # Use \over pattern so each substring is valid standalone LaTeX
        # (splitting \frac across substrings causes LaTeX compilation errors)
        combined_preview = MathTex(
            "G", "{M_{Earth} \\cdot", "m", "\\over", "r^2}", "=", "m", "\\cdot a",
            font_size=52
        )
        combined_preview.shift(DOWN * 2.5)

        self.play(
            FadeOut(gravity_eq_label),
            FadeOut(newton_eq_label),
            FadeOut(set_equal_text),
            Write(combined_preview, run_time=1.2)
        )
        self.wait(0.5)

        # Box and cross out both m's
        m1 = combined_preview[2]  # m in numerator (index 2 with \over split)
        m2 = combined_preview[6]  # m on right side (index 6)

        m1_box = SurroundingRectangle(m1, color=RED, stroke_width=3, buff=0.1)
        m2_box = SurroundingRectangle(m2, color=RED, stroke_width=3, buff=0.1)

        self.play(Create(m1_box), Create(m2_box), run_time=0.8)

        cross1 = VGroup(
            Line(m1_box.get_corner(DL), m1_box.get_corner(UR), color=RED, stroke_width=4),
            Line(m1_box.get_corner(UL), m1_box.get_corner(DR), color=RED, stroke_width=4)
        )
        cross2 = VGroup(
            Line(m2_box.get_corner(DL), m2_box.get_corner(UR), color=RED, stroke_width=4),
            Line(m2_box.get_corner(UL), m2_box.get_corner(DR), color=RED, stroke_width=4)
        )

        self.play(Create(cross1), Create(cross2))
        self.wait(0.8)

        # Result: a = G * M_Earth / r² (no m!)
        result = MathTex(
            "a = G \\frac{M_{Earth}}{r^2}",
            font_size=56,
            color=ACCENT_COLOR
        )
        result.next_to(combined_preview, RIGHT, buff=0.8)

        no_m_text = StyledText("No m !")
        no_m_text.scale(0.6)
        no_m_text.next_to(result, DOWN, buff=0.3)
        no_m_text.set_color(ACCENT_COLOR)

        self.play(
            FadeIn(result, scale=1.1),
            FadeIn(no_m_text)
        )
        self.wait(2)

        self.play(
            *[FadeOut(mob) for mob in [
                title, gravity_eq, newton_eq,
                combined_preview, m1_box, m2_box,
                cross1, cross2, result, no_m_text
            ]],
            run_time=0.8
        )

    def tease_next_video(self):
        """
        Part 3: Tease Video 2 (line 185)
        "We're going to explore that in the next video, where we'll discover
        the value of g—the acceleration due to gravity."
        """
        tease_title = StyledText("Coming up in Video 2:")
        tease_title.scale(0.8)
        tease_title.to_edge(UP, buff=0.5)
        tease_title.set_color(ACCENT_COLOR)

        self.play(FadeIn(tease_title))

        # Show g equation as a preview
        g_equation = MathTex(
            "g = G \\frac{M_{Earth}}{R_{Earth}^2} \\approx 9.8 \\, m/s^2",
            font_size=56
        )
        g_equation.shift(UP * 0.3)

        self.play(FadeIn(g_equation, scale=1.1))
        self.wait(0.5)

        subtitle = StyledText(
            "We'll derive this — and understand exactly\nwhy all objects fall at the same rate."
        )
        subtitle.scale(0.6)
        subtitle.next_to(g_equation, DOWN, buff=0.7)

        self.play(Write(subtitle, run_time=1.5))
        self.wait(2)

        self.play(
            FadeOut(tease_title),
            FadeOut(g_equation),
            FadeOut(subtitle),
            run_time=0.8
        )