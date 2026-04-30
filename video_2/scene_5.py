"""
video_2/scene_5.py
Scene 5: Putting It Together (4:10 -- 4:50)
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import StyledText, create_logo, BACKGROUND_COLOR, ACCENT_COLOR
from utils.question_utils import show_stop_sign


class Scene5(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        Scene5.question_2_card(self)
        Scene5.question_2_answer(self)

        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def question_2_card(self):
        question_title = StyledText("Question:")
        question_title.scale(0.8).to_edge(UP, buff=0.5).set_color(ACCENT_COLOR)
        self.play(FadeIn(question_title))

        question_text = StyledText(
            "If you stood on a planet with twice Earth's mass\n"
            "but the same radius, what would g be there?"
        )
        question_text.scale(0.65).next_to(question_title, DOWN, buff=0.5)
        self.play(Write(question_text, run_time=2))

        show_stop_sign(self, thinking_seconds=3.5)

        self.play(FadeOut(question_title), FadeOut(question_text), run_time=0.5)
        self.wait(0.3)

    def question_2_answer(self):
        base_formula = MathTex(r"g = \frac{G M_\oplus}{R_\oplus^2}", font_size=48)
        base_formula.shift(UP * 2.2)
        self.play(FadeIn(base_formula, scale=1.1))
        self.wait(3.0)

        sub_formula = MathTex(r"g' = \frac{G \cdot 2M_\oplus}{R_\oplus^2}", font_size=48)
        sub_formula.next_to(base_formula, DOWN, buff=0.45)
        self.play(FadeIn(sub_formula, shift=UP * 0.2))
        self.wait(3.0)

        factor_formula = MathTex(r"g' = 2 \cdot \frac{G M_\oplus}{R_\oplus^2}", font_size=48)
        factor_formula.next_to(sub_formula, DOWN, buff=0.45)
        self.play(FadeIn(factor_formula, shift=UP * 0.2))
        self.wait(3.0)

        result = MathTex(r"g' = 2g \approx 19.6\;\text{m/s}^2", font_size=56, color=ACCENT_COLOR)
        result.next_to(factor_formula, DOWN, buff=0.45)
        self.play(FadeIn(result, scale=1.1))
        self.wait(3.0)

        note = StyledText("M changed: nothing cancels it this time.")
        note.scale(0.55).set_color(WHITE).next_to(result, DOWN, buff=0.45)
        self.play(FadeIn(note))
        self.wait(3)