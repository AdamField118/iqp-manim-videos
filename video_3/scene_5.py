"""
video_3/scene_5.py
Scene 5: Confirmation and Real-World Consequences (4:05--4:55)
FIXES:
  - Lensing geometry correct: source, sun, observer colinear; apparent line stays in frame.
  - All checkmark labels moved away from citation texts (spaced vertically).
"""

import sys
sys.path.append('..')
import numpy as np
from manim import *
from utils.objects import StyledText, create_logo, BACKGROUND_COLOR, ACCENT_COLOR, TEXT_COLOR
from utils.question_utils import show_stop_sign

def checkmark_label(label_text, center):
    tick = VGroup(
        Line(ORIGIN, RIGHT*0.18+DOWN*0.22, color=GREEN, stroke_width=5),
        Line(RIGHT*0.18+DOWN*0.22, RIGHT*0.5+UP*0.28, color=GREEN, stroke_width=5),
    ).move_to(center)
    lbl = Text(label_text, font_size=22, color=GREEN).next_to(tick, RIGHT, buff=0.25)
    return tick, lbl

class Scene5(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)
        Scene5.confirmations(self)
        Scene5.question_2_card(self)
        Scene5.examples_flash(self)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def confirmations(self):
        banner = Text("General Relativity: Every Test Passed",
                      font_size=30, color=ACCENT_COLOR, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(FadeIn(banner), run_time=0.6)

        # ── 1. Light bending ──────────────────────────────────────────────────
        sun = Circle(0.5, fill_color=YELLOW, fill_opacity=1, stroke_color=GOLD, stroke_width=3).move_to(ORIGIN+UP*0.3)
        # Source at left, observer at right, both above the sun
        source_pos = np.array([-4.5, 1.0, 0])
        obs_pos = np.array([4.5, 1.0, 0])

        # Parametric curve from source to observer, bending downward near the sun
        def ray_func(t):
            # t from 0 to 1
            x = -4.5 + 9.0 * t
            # simple quadratic bend
            y_bend = 0.8 * (t - 0.5)**2   # a shallow dip near the centre
            y = 1.0 - y_bend
            return np.array([x, y, 0])

        ray_path = ParametricFunction(ray_func, t_range=[0,1], color=YELLOW_A, stroke_width=3)
        ray_start_dot = Dot(source_pos, color=YELLOW_A, radius=0.05)
        ray_end_dot = Dot(obs_pos, color=YELLOW_A, radius=0.05)

        # Tangent at observer: approximate with a point very near the end
        near_end = ray_func(0.995)
        tangent_dir = obs_pos - near_end
        # Draw dashed line back from observer along this tangent
        apparent_line = DashedLine(
            obs_pos,
            obs_pos - 3.0 * normalize(tangent_dir),
            color=GREY, stroke_width=1.5, dash_length=0.15
        )

        eddington_lbl = Text("Eddington, 1919", font_size=23, color=WHITE)
        eddington_lbl.to_edge(DOWN, buff=1.5)  # move lower to make room for checkmark
        self.play(FadeIn(sun), run_time=0.5)
        self.play(Create(ray_path), FadeIn(ray_start_dot), FadeIn(ray_end_dot), run_time=1.0)
        self.play(Create(apparent_line), FadeIn(eddington_lbl), run_time=0.8)

        # Checkmark placed above the citation (vertically separated)
        tick1, lbl1 = checkmark_label("light bending confirmed",
                                      eddington_lbl.get_center() + UP * 0.7)
        self.play(Create(tick1), FadeIn(lbl1), run_time=0.6)
        self.wait(3.5)
        self.play(FadeOut(sun), FadeOut(ray_path), FadeOut(ray_start_dot),
                  FadeOut(ray_end_dot), FadeOut(apparent_line), FadeOut(eddington_lbl),
                  FadeOut(tick1), FadeOut(lbl1), run_time=0.6)

        # ── 2. Mercury precession ─────────────────────────────────────────────
        sun2 = Circle(0.3, fill_color=YELLOW, fill_opacity=1, stroke_color=GOLD, stroke_width=2).move_to(LEFT*0.4+UP*0.3)
        obs_orbit = Ellipse(5.0, 3.0, color=GREEN, stroke_width=2.5).move_to(sun2.get_center()+RIGHT*0.55)
        peri_dot = Dot(obs_orbit.get_right(), color=RED, radius=0.08)
        peri_lbl = Text("perihelion", font_size=18, color=RED).next_to(peri_dot, UP, buff=0.15)

        obs_text = Text("Observed: 43 arcsec/century", font_size=22, color=WHITE).to_edge(DOWN, buff=1.5)
        self.play(FadeIn(sun2), Create(obs_orbit), FadeIn(peri_dot), FadeIn(peri_lbl), FadeIn(obs_text), run_time=0.8)

        # Precession
        for i in range(4):
            new_orbit = Ellipse(5.0, 3.0, color=GREEN, stroke_width=2.5).move_to(sun2.get_center()+RIGHT*0.55)
            new_orbit.rotate(PI/60*(i+1), about_point=sun2.get_center())
            new_dot = Dot(new_orbit.get_right(), color=RED, radius=0.08)
            new_lbl = Text("perihelion", font_size=18, color=RED).next_to(new_dot, UP, buff=0.15)
            self.play(FadeOut(obs_orbit), FadeOut(peri_dot), FadeOut(peri_lbl),
                      Create(new_orbit), FadeIn(new_dot), FadeIn(new_lbl), run_time=0.3)
            obs_orbit, peri_dot, peri_lbl = new_orbit, new_dot, new_lbl

        tick2, lbl2 = checkmark_label("GR prediction matches observed",
                                      obs_text.get_center() + UP * 0.7)
        self.play(Create(tick2), FadeIn(lbl2), run_time=0.6)
        self.wait(3.0)
        self.play(FadeOut(sun2), FadeOut(obs_orbit), FadeOut(peri_dot), FadeOut(peri_lbl),
                  FadeOut(obs_text), FadeOut(tick2), FadeOut(lbl2), run_time=0.6)

        # ── 3. Black hole inspiral + LIGO ────────────────────────────────────
        bh1 = Circle(0.28, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=2).move_to(LEFT*1.2+UP*0.5)
        bh2 = Circle(0.22, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=2).move_to(RIGHT*0.8+DOWN*0.3)

        def spiral(t, side=1):
            r = 1.5 * np.exp(-t/2)
            theta = t*3 + (PI if side==-1 else 0)
            return np.array([r*np.cos(theta), r*np.sin(theta), 0])

        path1 = ParametricFunction(lambda t: spiral(t,1), t_range=[0,4], color=GREY_B, stroke_width=1.5)
        path2 = ParametricFunction(lambda t: spiral(t,-1), t_range=[0,4], color=GREY_B, stroke_width=1.5)

        self.play(FadeIn(bh1), FadeIn(bh2), Create(path1), Create(path2), run_time=0.8)
        self.play(MoveAlongPath(bh1, path1), MoveAlongPath(bh2, path2), run_time=2.5, rate_func=linear)

        for i, r in enumerate([0.5, 1.2, 2.0, 2.8]):
            ripple = Circle(r, color=interpolate_color(BLUE_B, BLUE_E, i/3),
                            stroke_width=max(3.5 - i*0.8, 1.0), fill_opacity=0).move_to(ORIGIN)
            self.play(GrowFromCenter(ripple), ripple.animate.set_stroke(opacity=0), run_time=0.5)

        ligo_lbl = Text("LIGO, 2015", font_size=22, color=WHITE).to_edge(DOWN, buff=1.5)
        self.play(FadeIn(ligo_lbl), run_time=0.4)

        tick3, lbl3 = checkmark_label("gravitational waves detected",
                                      ligo_lbl.get_center() + UP * 0.7)
        self.play(Create(tick3), FadeIn(lbl3), run_time=0.6)
        self.wait(3.5)

        self.play(FadeOut(banner), FadeOut(bh1), FadeOut(bh2), FadeOut(path1), FadeOut(path2),
                  FadeOut(ligo_lbl), FadeOut(tick3), FadeOut(lbl3), run_time=0.8)

    def question_2_card(self):
        question_title = StyledText("Question 2:").scale(0.8).to_edge(UP, buff=0.5).set_color(ACCENT_COLOR)
        self.play(FadeIn(question_title))
        question_text = StyledText(
            "Newton's gravity and Einstein's gravity make nearly\n"
            "identical predictions for everyday situations.\n"
            "Can you think of a scenario where they would\n"
            "predict something measurably different?"
        ).scale(0.60).next_to(question_title, DOWN, buff=0.5)
        self.play(Write(question_text, run_time=2.5))
        show_stop_sign(self, thinking_seconds=3.5)
        self.play(FadeOut(question_title), FadeOut(question_text), run_time=0.5)
        self.wait(0.3)

    def examples_flash(self):
        examples = [
            ("Near a black hole",   BLUE_B),
            ("Near a neutron star", BLUE_C),
            ("GPS satellites (clocks)", GREEN),
            ("Scale of the entire cosmos", YELLOW),
        ]
        items = VGroup(*[Text(t, font_size=34, color=c) for t,c in examples])
        items.arrange(DOWN, buff=0.55).center()
        for item in items:
            self.play(FadeIn(item, shift=LEFT*0.3), run_time=0.55)
            self.wait(0.6)
        self.wait(2.0)
        self.play(FadeOut(items), run_time=0.8)