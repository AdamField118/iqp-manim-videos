"""
video_3/scene_3.py
Scene 3: The Second Crack -- Differential / Tidal Gravity (1:17--~2:45)
FIX: All Rectangle calls now use width= and height= keywords.
"""

import sys
sys.path.append('..')
import numpy as np
from manim import *
from utils.objects import StyledText, create_logo, BACKGROUND_COLOR, ACCENT_COLOR, TEXT_COLOR
from utils.question_utils import show_stop_sign

class Scene3(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)
        Scene3.tidal_forces_diagram(self)
        Scene3.question_1_card(self)
        Scene3.spaghettification(self)
        Scene3.elevator_demo(self)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    # ── Tidal forces diagram ────────────────────────────────────────────────
    def tidal_forces_diagram(self):
        title = Text("Tidal / Differential Gravity", font_size=32,
                     color=ACCENT_COLOR, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)

        earth = Circle(1.3, fill_color=BLUE, fill_opacity=0.75,
                       stroke_color=BLUE_E, stroke_width=3).move_to(LEFT * 3.5 + UP * 0.3)
        earth_label = Text("Earth", font_size=24, color=WHITE).next_to(earth, DOWN, buff=0.25)
        moon = Circle(0.5, fill_color=GREY_C, fill_opacity=0.85,
                      stroke_color=WHITE, stroke_width=2).move_to(RIGHT * 4.2 + UP * 0.3)
        moon_label = Text("Moon", font_size=24, color=WHITE).next_to(moon, DOWN, buff=0.25)

        self.play(FadeIn(earth, scale=0.8), FadeIn(earth_label),
                  FadeIn(moon, scale=0.8), FadeIn(moon_label), run_time=1.0)
        self.wait(0.5)

        near_start = earth.get_center() + RIGHT * 1.3
        ctr_start  = earth.get_center()
        far_start  = earth.get_center() + LEFT * 1.3

        arrow_near = Arrow(near_start, near_start + RIGHT * 2.2, color=RED, stroke_width=7, buff=0,
                           max_tip_length_to_length_ratio=0.12)
        arrow_ctr  = Arrow(ctr_start, ctr_start + RIGHT * 1.5, color=ORANGE, stroke_width=5, buff=0,
                           max_tip_length_to_length_ratio=0.15)
        arrow_far  = Arrow(far_start, far_start + RIGHT * 0.8, color=YELLOW, stroke_width=4, buff=0,
                           max_tip_length_to_length_ratio=0.2)

        lbl_near = Text("stronger", font_size=20, color=RED).next_to(arrow_near, UP, buff=0.12)
        lbl_ctr  = Text("average",  font_size=20, color=ORANGE).next_to(arrow_ctr, DOWN, buff=0.12)
        lbl_far  = Text("weaker",   font_size=20, color=YELLOW).next_to(arrow_far, DOWN, buff=0.12)

        intro_text = Text("Moon's pull is not uniform across Earth", font_size=22, color=GREY_B).to_edge(DOWN, buff=1.3)
        self.play(FadeIn(intro_text), run_time=0.5)
        self.wait(0.5)

        self.play(Create(arrow_near), FadeIn(lbl_near), run_time=0.7)
        self.wait(0.3)
        self.play(Create(arrow_ctr), FadeIn(lbl_ctr), run_time=0.7)
        self.wait(0.3)
        self.play(Create(arrow_far), FadeIn(lbl_far), run_time=0.7)
        self.wait(1.5)

        tidal_text = Text("The difference stretches Earth along the Earth-Moon line.",
                          font_size=21, color=WHITE).to_edge(DOWN, buff=0.6)
        self.play(FadeOut(intro_text), FadeIn(tidal_text), run_time=0.5)

        tidal_earth = Ellipse(3.0, 2.2, fill_color=BLUE, fill_opacity=0.75,
                              stroke_color=BLUE_E, stroke_width=3).move_to(earth.get_center())
        self.play(Transform(earth, tidal_earth), run_time=1.5)
        self.wait(1.5)

        formula = MathTex(r"F_{\text{tidal}} \propto {M \over r^3}", font_size=58)
        formula.next_to(tidal_text, UP, buff=0.5)
        self.play(FadeIn(formula, scale=1.1), run_time=0.8)

        m_box = SurroundingRectangle(formula[0][8], color=YELLOW, buff=0.08)
        r_box = SurroundingRectangle(formula[0][10:12], color=RED, buff=0.08)
        cube_note = Text("cube -- falls off faster than gravity itself",
                         font_size=20, color=RED).next_to(formula, UP, buff=0.3)
        self.play(Create(m_box), Create(r_box), run_time=0.6)
        self.play(FadeIn(cube_note), run_time=0.5)
        self.wait(4.0)

        self.play(*[FadeOut(m) for m in [title, earth, earth_label, moon, moon_label,
                                          arrow_near, arrow_ctr, arrow_far,
                                          lbl_near, lbl_ctr, lbl_far,
                                          tidal_text, formula, m_box, r_box, cube_note]], run_time=0.8)

    # ── Question 1 ──────────────────────────────────────────────────────────
    def question_1_card(self):
        question_title = StyledText("Question 1:").scale(0.8).to_edge(UP, buff=0.5).set_color(ACCENT_COLOR)
        self.play(FadeIn(question_title))
        question_text = StyledText(
            "If you were falling feet-first toward a black hole,\n"
            "what would the tidal forces do to your body?"
        ).scale(0.65).next_to(question_title, DOWN, buff=0.5)
        self.play(Write(question_text, run_time=2))
        show_stop_sign(self, thinking_seconds=3.5)
        self.play(FadeOut(question_title), FadeOut(question_text), run_time=0.5)
        self.wait(0.3)

    # ── C.3 Spaghettification ───────────────────────────────────────────────
    def spaghettification(self):
        title = Text("Spaghettification", font_size=34, color=ACCENT_COLOR, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.6)

        compact_mass = Circle(0.3, fill_color=BLACK, fill_opacity=1.0,
                              stroke_color=WHITE, stroke_width=3).move_to(DOWN * 3.5)
        mass_label = Text("compact mass", font_size=20, color=WHITE).next_to(compact_mass, RIGHT, buff=0.3)

        head = Circle(radius=0.22, fill_color=LIGHT_GREY, fill_opacity=0.85,
                      stroke_color=WHITE, stroke_width=2)
        body = Rectangle(width=0.38, height=0.75, fill_color=BLUE_D, fill_opacity=0.85,
                         stroke_color=WHITE, stroke_width=2).next_to(head, DOWN, buff=0.05)
        figure = VGroup(head, body).move_to(UP * 1.5)

        self.play(FadeIn(compact_mass), FadeIn(mass_label), run_time=0.6)
        self.play(FadeIn(figure), run_time=0.6)
        self.wait(0.5)

        # Stretch steps – all Rectangles now with keywords
        stretched_head1 = Ellipse(width=0.20, height=0.26,
                                  fill_color=LIGHT_GREY, fill_opacity=0.85,
                                  stroke_color=WHITE, stroke_width=2)
        stretched_body1 = Rectangle(width=0.30, height=1.2,
                                    fill_color=BLUE_D, fill_opacity=0.85,
                                    stroke_color=WHITE, stroke_width=2)
        stretched_body1.next_to(stretched_head1, DOWN, buff=0.04)
        figure_s1 = VGroup(stretched_head1, stretched_body1).move_to(UP * 1.2)

        stretched_head2 = Ellipse(width=0.13, height=0.24,
                                  fill_color=LIGHT_GREY, fill_opacity=0.85,
                                  stroke_color=WHITE, stroke_width=2)
        stretched_body2 = Rectangle(width=0.18, height=2.0,
                                    fill_color=BLUE_D, fill_opacity=0.85,
                                    stroke_color=WHITE, stroke_width=2)
        stretched_body2.next_to(stretched_head2, DOWN, buff=0.03)
        figure_s2 = VGroup(stretched_head2, stretched_body2).move_to(UP * 0.8)

        stretched_head3 = Ellipse(width=0.07, height=0.18,
                                  fill_color=LIGHT_GREY, fill_opacity=0.85,
                                  stroke_color=WHITE, stroke_width=2)
        stretched_body3 = Rectangle(width=0.08, height=2.8,
                                    fill_color=BLUE_D, fill_opacity=0.85,
                                    stroke_color=WHITE, stroke_width=2)
        stretched_body3.next_to(stretched_head3, DOWN, buff=0.02)
        figure_s3 = VGroup(stretched_head3, stretched_body3).move_to(UP * 0.4)

        self.play(Transform(figure, figure_s1), run_time=1.2)
        self.play(Transform(figure, figure_s2), run_time=1.2)
        self.play(Transform(figure, figure_s3), run_time=1.2)

        spag_label = Text("spaghettification", font_size=28, color=RED).next_to(figure, RIGHT, buff=0.5)
        self.play(FadeIn(spag_label), run_time=0.5)
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [title, compact_mass, mass_label, figure, spag_label]], run_time=0.8)

    # ── C.4 Elevator demo ────────────────────────────────────────────────────
    def elevator_demo(self):
        title = Text("Tidal Forces in Free Fall", font_size=30, color=ACCENT_COLOR, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(title), run_time=0.6)

        box = Rectangle(width=3.8, height=3.2, stroke_color=WHITE, stroke_width=3,
                        fill_opacity=0).move_to(ORIGIN + UP * 0.5)
        ball_L = Dot(0.18, color=YELLOW).move_to(box.get_center() + LEFT * 0.85)
        ball_R = Dot(0.18, color=YELLOW).move_to(box.get_center() + RIGHT * 0.85)

        earth_center = DOWN * 6.0
        dash_L = DashedLine(ball_L.get_center(), earth_center, color=GREY_B,
                            stroke_width=1.5, dash_length=0.15)
        dash_R = DashedLine(ball_R.get_center(), earth_center, color=GREY_B,
                            stroke_width=1.5, dash_length=0.15)
        conv_label = Text("converging paths", font_size=20, color=GREY_B).move_to(DOWN * 2.8)

        self.play(Create(box), run_time=0.6)
        self.play(FadeIn(ball_L), FadeIn(ball_R), run_time=0.5)
        self.play(Create(dash_L), Create(dash_R), FadeIn(conv_label), run_time=0.8)
        self.wait(1.5)

        self.play(ball_L.animate.shift(RIGHT * 0.7), ball_R.animate.shift(LEFT * 0.7),
                  run_time=3.5, rate_func=rate_functions.ease_in_sine)

        conclusion = Text("Tidal forces can't be erased by free fall.",
                          font_size=26, color=RED, weight=BOLD).to_edge(DOWN, buff=1.0)
        self.play(FadeIn(conclusion, scale=1.05), run_time=0.8)
        self.wait(4.0)

        self.play(*[FadeOut(m) for m in [title, box, ball_L, ball_R,
                                          dash_L, dash_R, conv_label, conclusion]], run_time=0.8)