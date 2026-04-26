"""
Scene 3: Back to the Cliffhanger (2:20--3:30)

Transcript Manim tags:
- F = GM_⊕m/r² fades in; label M_⊕, m, r
- Two falling objects side by side: large m_heavy (bigger force arrow),
  small m_light (smaller force arrow). Pose: two different forces, same acceleration?
- Step by step: GM_⊕m/r² = ma → m cancels → a = GM_⊕/r²
  Highlight absence of m. Hold on screen.
- Plug in Earth's mass and radius: g = GM_⊕/R_⊕² ≈ 9.8 m/s²
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import (
    StyledText, create_logo,
    BACKGROUND_COLOR, ACCENT_COLOR, TEXT_COLOR
)
from utils.physics_objects import create_fbd_force_arrows, create_ball

class Scene3(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        Scene3.recall_gravity_formula(self)
        Scene3.two_falling_objects(self)
        Scene3.mass_cancellation(self)
        Scene3.derive_g(self)

        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def recall_gravity_formula(self):
        """
        F = GM_oplus m / r^2 fades in.
        Each variable is color-highlighted with a text label,
        matching the visual style of the rest of the series.
        Indices: [0]="F = G {"  [1]=M_oplus  [2]=m  [3]=over  [4]="r^2}"
        """
        formula = MathTex(
            r"F = G {",
            r"M_\oplus \,",
            r"m",
            r"\over",
            r"r^2}",
            font_size=72
        )
        formula.shift(UP * 1.0)

        self.play(FadeIn(formula, scale=1.1), run_time=1.2)
        self.wait(0.5)

        # Highlight M_oplus
        earth_label = StyledText("Earth's mass")
        earth_label.scale(0.45).set_color(BLUE)
        earth_label.next_to(formula, DOWN, buff=0.7).shift(LEFT * 1.8)

        self.play(formula[1].animate.set_color(BLUE), FadeIn(earth_label))
        self.wait(0.8)

        # Highlight m
        m_label = StyledText("falling object's mass")
        m_label.scale(0.45).set_color(GREEN)
        m_label.next_to(formula, DOWN, buff=0.7)

        self.play(formula[2].animate.set_color(GREEN), FadeIn(m_label))
        self.wait(0.8)

        # Highlight r^2
        r_label = StyledText("distance from Earth's center")
        r_label.scale(0.45).set_color(YELLOW)
        r_label.next_to(formula, UP, buff=0.5)

        self.play(formula[4].animate.set_color(YELLOW), FadeIn(r_label))
        self.wait(1.5)

        self.play(
            formula[1].animate.set_color(WHITE),
            formula[2].animate.set_color(WHITE),
            formula[4].animate.set_color(WHITE),
            FadeOut(earth_label), FadeOut(m_label), FadeOut(r_label),
            FadeOut(formula),
            run_time=0.8
        )

    def two_falling_objects(self):
        """
        Large m_heavy and small m_light side by side.
        Larger downward force arrow on heavy, smaller on light.
        Pose: two different forces — same acceleration?
        """
        heavy = Circle(radius=0.55, fill_color=BLUE, fill_opacity=0.8,
                       stroke_color=WHITE, stroke_width=2)
        heavy_label = MathTex(r"m_\text{heavy}", font_size=36, color=WHITE)
        heavy_label.next_to(heavy, UP, buff=0.2)
        heavy_group = VGroup(heavy, heavy_label)
        heavy_group.shift(LEFT * 2.5)

        light = Circle(radius=0.3, fill_color=RED_C, fill_opacity=0.8,
                       stroke_color=WHITE, stroke_width=2)
        light_label = MathTex(r"m_\text{light}", font_size=28, color=WHITE)
        light_label.next_to(light, UP, buff=0.2)
        light_group = VGroup(light, light_label)
        light_group.shift(RIGHT * 2.5)

        self.play(FadeIn(heavy_group, scale=0.5), FadeIn(light_group, scale=0.5))
        self.wait(0.5)

        # Larger force arrow on heavy, smaller on light
        heavy_arrow = Arrow(
            heavy.get_center(),
            heavy.get_center() + DOWN * 1.6,
            color=YELLOW, stroke_width=10, buff=0,
            max_tip_length_to_length_ratio=0.15
        )
        heavy_F_label = MathTex("F_{big}", font_size=36, color=YELLOW)
        heavy_F_label.next_to(heavy_arrow, LEFT, buff=0.15)

        light_arrow = Arrow(
            light.get_center(),
            light.get_center() + DOWN * 0.8,
            color=YELLOW, stroke_width=5, buff=0,
            max_tip_length_to_length_ratio=0.25
        )
        light_F_label = MathTex("F_{small}", font_size=36, color=YELLOW)
        light_F_label.next_to(light_arrow, RIGHT, buff=0.15)

        self.play(
            Create(heavy_arrow), FadeIn(heavy_F_label),
            Create(light_arrow), FadeIn(light_F_label)
        )
        self.wait(1)

        question = StyledText("Two different forces, same acceleration?")
        question.scale(0.65).set_color(ACCENT_COLOR)
        question.to_edge(DOWN, buff=1.0)
        self.play(Write(question, run_time=1.2))
        self.wait(2)

        self.play(
            FadeOut(heavy_group), FadeOut(heavy_arrow), FadeOut(heavy_F_label),
            FadeOut(light_group), FadeOut(light_arrow), FadeOut(light_F_label),
            FadeOut(question),
            run_time=0.8
        )

    def mass_cancellation(self):
        """
        Step-by-step:
          GM_⊕m/r² = ma
          Animate m crossing out on both sides simultaneously
          Result: a = GM_⊕/r²
          Highlight absence of m. Hold on screen.
        """
        # Use \over so each substring is valid standalone LaTeX
        combined = MathTex(
            "G", "{M_{\\oplus} \\cdot", "m", "\\over", "r^2}", "=", "m", "\\cdot a",
            font_size=56
        )
        combined.shift(UP * 0.8)

        self.play(Write(combined, run_time=1.5))
        self.wait(1)

        # Box and cross out both m's simultaneously
        m_num = combined[2]   # m in numerator
        m_rhs = combined[6]   # m on right side

        box1 = SurroundingRectangle(m_num, color=RED, stroke_width=3, buff=0.1)
        box2 = SurroundingRectangle(m_rhs, color=RED, stroke_width=3, buff=0.1)

        self.play(Create(box1), Create(box2), run_time=0.6)

        cross1 = VGroup(
            Line(box1.get_corner(DL), box1.get_corner(UR), color=RED, stroke_width=4),
            Line(box1.get_corner(UL), box1.get_corner(DR), color=RED, stroke_width=4)
        )
        cross2 = VGroup(
            Line(box2.get_corner(DL), box2.get_corner(UR), color=RED, stroke_width=4),
            Line(box2.get_corner(UL), box2.get_corner(DR), color=RED, stroke_width=4)
        )

        self.play(Create(cross1), Create(cross2))
        self.wait(1)

        # Result: a = GM_⊕/r²
        result = MathTex(
            r"a = \frac{G M_\oplus}{r^2}",
            font_size=64,
            color=ACCENT_COLOR
        )
        result.next_to(combined, DOWN, buff=1.0)

        no_m = StyledText("No m: mass of the falling object is gone!")
        no_m.scale(0.55).set_color(ACCENT_COLOR)
        no_m.next_to(result, DOWN, buff=0.4)

        self.play(FadeIn(result, scale=1.1))
        self.play(FadeIn(no_m))
        self.wait(3)

        self.play(
            FadeOut(combined), FadeOut(box1), FadeOut(box2),
            FadeOut(cross1), FadeOut(cross2), FadeOut(no_m),
            result.animate.move_to(UP * 2).scale(0.85),
            run_time=1
        )

        self.result_eq = result

    def derive_g(self):
        """
        Plug in Earth's mass and radius numerically:
          g = GM_⊕ / R_⊕² ≈ 9.8 m/s²
        """
        plug_in = MathTex(
            r"g = \frac{G M_\oplus}{R_\oplus^2}",
            font_size=56
        )
        plug_in.next_to(self.result_eq, DOWN, buff=0.7)

        self.play(FadeIn(plug_in, shift=UP * 0.3))
        self.wait(1)

        equals_arrow = Arrow(
            plug_in.get_right(),
            plug_in.get_right() + RIGHT * 1.2,
            color=WHITE, stroke_width=3, buff=0.1
        )
        g_value = MathTex(
            r"\approx 9.8\;\text{m/s}^2",
            font_size=56,
            color=GREEN
        )
        g_value.next_to(equals_arrow, RIGHT, buff=0.2)

        self.play(Create(equals_arrow), FadeIn(g_value))
        self.wait(1)

        same_for_all = StyledText("Same for every object near Earth's surface.")
        same_for_all.scale(0.6).set_color(WHITE)
        same_for_all.next_to(g_value, DOWN, buff=0.6)

        self.play(Write(same_for_all, run_time=1.2))
        self.wait(3)

        self.play(
            FadeOut(self.result_eq), FadeOut(plug_in),
            FadeOut(equals_arrow), FadeOut(g_value), FadeOut(same_for_all),
            run_time=0.8
        )