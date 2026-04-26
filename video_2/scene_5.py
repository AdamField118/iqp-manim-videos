"""
Scene 5: Putting It Together (4:10--4:50)

Transcript Manim tag:
- Show g = GM/R² with M replaced by 2M_⊕, arriving at g' = 2g ≈ 19.6 m/s²
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import (
    StyledText, create_logo,
    BACKGROUND_COLOR, ACCENT_COLOR
)

class Scene5(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        Scene5.question_2_answer(self)

        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def question_2_answer(self):
        """
        Q2: Planet with twice Earth's mass, same radius. What is g?
        Show g = GM/R^2 with M replaced by 2M_oplus, arriving at g' = 2g ~ 19.6 m/s^2.
        Equations are stacked with tight spacing so the note does not overlap.
        """
        base_formula = MathTex(
            r"g = \frac{G M_\oplus}{R_\oplus^2}",
            font_size=48
        )
        base_formula.shift(UP * 2.2)

        self.play(FadeIn(base_formula, scale=1.1))
        self.wait(0.5)

        sub_formula = MathTex(
            r"g' = \frac{G \cdot 2M_\oplus}{R_\oplus^2}",
            font_size=48
        )
        sub_formula.next_to(base_formula, DOWN, buff=0.45)

        self.play(FadeIn(sub_formula, shift=UP * 0.2))
        self.wait(0.5)

        factor_formula = MathTex(
            r"g' = 2 \cdot \frac{G M_\oplus}{R_\oplus^2}",
            font_size=48
        )
        factor_formula.next_to(sub_formula, DOWN, buff=0.45)

        self.play(FadeIn(factor_formula, shift=UP * 0.2))
        self.wait(0.5)

        result = MathTex(
            r"g' = 2g \approx 19.6\;\text{m/s}^2",
            font_size=56,
            color=ACCENT_COLOR
        )
        result.next_to(factor_formula, DOWN, buff=0.45)

        self.play(FadeIn(result, scale=1.1))
        self.wait(1)

        note = StyledText("M changed: nothing cancels it this time.")
        note.scale(0.55).set_color(WHITE)
        note.next_to(result, DOWN, buff=0.45)
        self.play(FadeIn(note))
        self.wait(3)