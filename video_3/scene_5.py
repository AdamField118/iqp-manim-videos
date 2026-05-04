"""
video_3/scene_5.py
Scene 5: Confirmation and Real-World Consequences (4:05--4:55)
FIXES:
  - Lensing geometry correct: source, sun, observer colinear; apparent line stays in frame.
  - All checkmark labels moved away from citation texts (spaced vertically).
  - Perihelion dot tracked analytically (rotation angle) instead of get_right()
    on the bounding box, which only moved horizontally.
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
        # Layout matches the JS demo: Observer (left) — Sun lens (centre) — Star (right)
        # all on the optical axis.  Light bows ABOVE the axis (attractive gravity).
        # Back-projected dashed line → apparent position directly above actual.
        axis_y = -0.4   # slightly below centre so arc has headroom above
        obs_p  = np.array([-6.0, axis_y, 0])
        src_p  = np.array([ 5.8, axis_y, 0])
        lens_p = np.array([ 0.0, axis_y, 0])
        bend   = 1.35   # control-point height above axis
        app_p  = np.array([src_p[0], axis_y + 2 * bend, 0])  # directly above actual

        # Warped spacetime grid pulled toward the Sun
        grid_lines = VGroup()
        n_pts, gstep, x_ext, y_ext = 30, 0.55, 6.8, 3.4
        def warp_bh(q):
            dx, dy = q[0] - lens_p[0], q[1] - lens_p[1]
            r  = np.sqrt(dx*dx + dy*dy) + 0.01
            pull = 1.6 / (r*r + 0.7)
            f  = pull / (1 + pull)
            return np.array([q[0] + (lens_p[0]-q[0])*f*0.65,
                             q[1] + (lens_p[1]-q[1])*f*0.65, 0])
        for xv in np.arange(-x_ext, x_ext + gstep, gstep):
            pts = [warp_bh([xv, yv, 0]) for yv in np.linspace(-y_ext, y_ext, n_pts)]
            vl  = VMobject(stroke_color=BLUE_E, stroke_opacity=0.22, stroke_width=0.7)
            vl.set_points_as_corners(pts)
            grid_lines.add(vl)
        for yv in np.arange(-y_ext, y_ext + gstep, gstep):
            pts = [warp_bh([xv, yv, 0]) for xv in np.linspace(-x_ext, x_ext, n_pts)]
            vl  = VMobject(stroke_color=BLUE_E, stroke_opacity=0.22, stroke_width=0.7)
            vl.set_points_as_corners(pts)
            grid_lines.add(vl)
        self.play(FadeIn(grid_lines), run_time=0.5)

        # Sun: plain yellow circle
        sun_lens = Circle(0.45, fill_color=YELLOW, fill_opacity=1,
                          stroke_color=GOLD, stroke_width=3)
        sun_lens.move_to(lens_p)
        self.play(GrowFromCenter(sun_lens), run_time=0.6)

        # Actual star (gold, right, on axis) + observer (left)
        star_actual = Dot(src_p, color=GOLD, radius=0.14)
        obs_dot     = Dot(obs_p, color=WHITE, radius=0.07)
        obs_lbl     = Text("Observer", font_size=17, color=GREY_B).next_to(obs_dot, DOWN, buff=0.12)
        self.play(FadeIn(star_actual), FadeIn(obs_dot), FadeIn(obs_lbl), run_time=0.4)

        # Light path: quadratic bezier bowing above the axis over the lens.
        # P(t) = (1-t)² src + 2t(1-t) cp + t² obs
        # Control point is directly above the lens at height +bend.
        cp_lensing = np.array([lens_p[0], axis_y + bend, 0])
        def arc_func(t):
            return (1-t)**2 * src_p + 2*t*(1-t)*cp_lensing + t**2 * obs_p
        ray_glow = ParametricFunction(arc_func, t_range=[0, 1],
                                      color=YELLOW, stroke_width=8, stroke_opacity=0.13)
        ray_path = ParametricFunction(arc_func, t_range=[0, 1],
                                      color=YELLOW_A, stroke_width=2.5)
        self.play(Create(ray_glow), Create(ray_path), run_time=1.2)

        # Back-projection dashed line: Observer looks backward along incoming ray.
        # For a symmetric bezier the apparent position is analytically at
        # (src_x, axis_y + 2*bend) — the line runs from obs through app and a
        # little beyond so the direction reads clearly.
        dash_end = app_p + normalize(app_p - obs_p) * 0.5
        apparent_line = DashedLine(obs_p, dash_end,
                                   color=GREY_B, stroke_width=1.7, dash_length=0.18)
        self.play(Create(apparent_line), run_time=0.8)

        # Apparent star directly above actual + thin vertical guide
        star_app   = Dot(app_p, color=GOLD, radius=0.13)
        app_label  = Text("Apparent", font_size=17, color=GOLD).next_to(star_app, RIGHT, buff=0.12)
        act_label  = Text("Actual",   font_size=17, color=GOLD).next_to(star_actual, RIGHT, buff=0.12)
        vert_guide = DashedLine(src_p, app_p, color=YELLOW_A,
                                stroke_width=0.9, stroke_opacity=0.28, dash_length=0.1)
        self.play(FadeIn(star_app), FadeIn(app_label), FadeIn(act_label),
                  Create(vert_guide), run_time=0.7)

        eddington_lbl = Text("Eddington, 1919", font_size=23, color=WHITE)
        eddington_lbl.to_edge(DOWN, buff=1.5)
        self.play(FadeIn(eddington_lbl), run_time=0.4)

        tick1, lbl1 = checkmark_label("light bending confirmed",
                                      eddington_lbl.get_center() + UP * 0.7)
        self.play(Create(tick1), FadeIn(lbl1), run_time=0.6)
        self.wait(3.5)
        self.play(FadeOut(grid_lines), FadeOut(sun_lens),
                  FadeOut(star_actual), FadeOut(obs_dot), FadeOut(obs_lbl),
                  FadeOut(ray_path), FadeOut(ray_glow), FadeOut(apparent_line),
                  FadeOut(star_app), FadeOut(app_label), FadeOut(act_label),
                  FadeOut(vert_guide), FadeOut(eddington_lbl),
                  FadeOut(tick1), FadeOut(lbl1), run_time=0.6)

        # ── 2. Mercury precession ─────────────────────────────────────────────
        sun2 = Circle(0.3, fill_color=YELLOW, fill_opacity=1, stroke_color=GOLD, stroke_width=2).move_to(LEFT*0.4+UP*0.3)
        obs_orbit = Ellipse(5.0, 3.0, color=GREEN, stroke_width=2.5).move_to(sun2.get_center()+RIGHT*0.55)
        peri_dot = Dot(obs_orbit.get_right(), color=RED, radius=0.08)
        peri_lbl = Text("perihelion", font_size=18, color=RED).next_to(peri_dot, UP, buff=0.15)

        obs_text = Text("Observed: 43 arcsec/century", font_size=22, color=WHITE).to_edge(DOWN, buff=1.5)
        self.play(FadeIn(sun2), Create(obs_orbit), FadeIn(peri_dot), FadeIn(peri_lbl), FadeIn(obs_text), run_time=0.8)

        # Mirror Manim's own rotate() call exactly: grab the initial tip from
        # get_right(), store its offset from the sun, then apply a 2-D rotation
        # matrix — identical to what rotate() does to the orbit itself.
        sun2_np     = np.array(sun2.get_center())
        peri_offset = np.array(obs_orbit.get_right()) - sun2_np
        for i in range(4):
            total_angle = PI/60 * (i+1)
            new_orbit = Ellipse(5.0, 3.0, color=GREEN, stroke_width=2.5).move_to(sun2.get_center()+RIGHT*0.55)
            new_orbit.rotate(total_angle, about_point=sun2.get_center())
            c, s = np.cos(total_angle), np.sin(total_angle)
            peri_pos = sun2_np + np.array([
                c * peri_offset[0] - s * peri_offset[1],
                s * peri_offset[0] + c * peri_offset[1],
                0,
            ])
            new_dot = Dot(peri_pos, color=RED, radius=0.08)
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