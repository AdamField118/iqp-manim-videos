"""
video_3/scene_4.py
Scene 4: Einstein's Revolutionary Idea (2:51--~4:05)
FIXES:
  - Title scaled to fit screen.
  - Spacetime grid now warps visibly (custom grid built from Lines).
  - Green marble orbit centred on the mass and follows the warped geodesic.
  - Converging geodesics end at the mass centre.
"""

import sys
sys.path.append('..')
import numpy as np
from manim import *
from utils.objects import StyledText, create_logo, BACKGROUND_COLOR, ACCENT_COLOR, TEXT_COLOR

class Scene4(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)
        Scene4.gravity_equals_curved_spacetime(self)
        Scene4.spacetime_grid(self)
        Scene4.wheeler_quote(self)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def gravity_equals_curved_spacetime(self):
        word_gravity = Text("Gravity",  font_size=72, color=WHITE, weight=BOLD)
        word_equals  = Text("=",        font_size=72, color=ACCENT_COLOR, weight=BOLD)
        word_curved  = Text("Curved",   font_size=72, color=BLUE_B, weight=BOLD)
        word_space   = Text("Spacetime",font_size=72, color=BLUE_B, weight=BOLD)

        word_gravity.shift(UP * 0.3)
        word_equals.next_to(word_gravity, RIGHT, buff=0.4)
        word_curved.next_to(word_equals, RIGHT, buff=0.4)
        word_space.next_to(word_curved, RIGHT, buff=0.3)

        phrase = VGroup(word_gravity, word_equals, word_curved, word_space)
        phrase.center()
        phrase.scale_to_fit_width(config["frame_width"] - 1)

        self.play(FadeIn(word_gravity, scale=1.15), run_time=0.7)
        self.play(FadeIn(word_equals,  scale=1.15), run_time=0.4)
        self.play(FadeIn(word_curved,  scale=1.15), run_time=0.5)
        self.play(FadeIn(word_space,   scale=1.15), run_time=0.5)

        self.play(word_space.animate.set_color(LIGHT_PINK), run_time=0.4)
        self.play(word_space.animate.set_color(BLUE_B), run_time=0.4)

        self.wait(4.0)
        self.play(FadeOut(phrase, scale=0.9), run_time=0.8)

    # ── Helper: create a flat grid as a VGroup of Lines ────────────────────
    def create_flat_grid(self, size=5, step=0.5, color=BLUE_E, opacity=0.5):
        lines = VGroup()
        for x in np.arange(-size, size + step, step):
            lines.add(Line([x, -size, 0], [x, size, 0], stroke_color=color, stroke_opacity=opacity, stroke_width=0.8))
        for y in np.arange(-size, size + step, step):
            lines.add(Line([-size, y, 0], [size, y, 0], stroke_color=color, stroke_opacity=opacity, stroke_width=0.8))
        return lines

    def spacetime_grid(self):
        title = Text("Spacetime Curvature", font_size=30, color=ACCENT_COLOR, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.5)

        # Build flat grid
        flat_grid = self.create_flat_grid(size=4.5, step=0.5, color=BLUE_E)
        self.play(Create(flat_grid, lag_ratio=0.02), run_time=1.2)

        flat_label = Text("flat spacetime", font_size=22, color=GREY_B).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(flat_label), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(flat_label), run_time=0.3)

        mass = Circle(0.3, fill_color="#e8a000", fill_opacity=1, stroke_color=GOLD, stroke_width=3)
        mass.move_to(ORIGIN)
        mass_label = Text("mass", font_size=20, color=GOLD).next_to(mass, RIGHT, buff=0.25)
        self.play(GrowFromCenter(mass), FadeIn(mass_label), run_time=0.8)

        # Warp function – strong, clearly visible
        def warp(p):
            x, y, z = p[:3]
            r = np.sqrt(x**2 + y**2) + 0.01
            depression = 2.5 * np.exp(-r**2 / 1.5)   # deep and wide
            return np.array([x, y - depression, z])

        # Apply warp to a copy
        warped_grid = flat_grid.copy()
        warped_grid.apply_function(warp)

        curved_label = Text("curved spacetime", font_size=22, color=BLUE_B).to_edge(DOWN, buff=0.5)
        self.play(Transform(flat_grid, warped_grid), FadeIn(curved_label), run_time=2.0)
        self.wait(1.5)

        # Green marble on a geodesic – uses exactly the same warp
        def orb(t):
            p = np.array([2.0 * np.cos(t), 2.0 * np.sin(t), 0])
            return warp(p)
        orbit = ParametricFunction(orb, t_range=[-PI, PI], color=GREEN, stroke_width=2)
        small_obj = Dot(0.12, color=GREEN).move_to(orbit.get_start())

        self.play(FadeOut(curved_label), run_time=0.3)
        self.play(Create(orbit, run_time=0.6))
        self.play(FadeIn(small_obj), run_time=0.4)

        geodesic_label = Text("geodesic -- straightest path through curved geometry",
                              font_size=20, color=GREEN).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(geodesic_label), run_time=0.4)

        self.play(MoveAlongPath(small_obj, orbit), run_time=3.5, rate_func=linear)
        self.wait(0.5)

        # Two geodesics converge toward the mass
        self.play(FadeOut(orbit), FadeOut(small_obj), FadeOut(geodesic_label), run_time=0.6)

        conv_label = Text("Two geodesics converge toward the central mass",
                          font_size=20, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(conv_label), run_time=0.4)

        ball_a = Dot(0.14, color=YELLOW).move_to(UP * 1.8 + LEFT * 0.5)
        ball_b = Dot(0.14, color=YELLOW).move_to(UP * 1.8 + RIGHT * 0.5)
        geo_a = DashedLine(ball_a.get_center(), ORIGIN, color=YELLOW_A, stroke_width=1.8, dash_length=0.12)
        geo_b = DashedLine(ball_b.get_center(), ORIGIN, color=YELLOW_A, stroke_width=1.8, dash_length=0.12)

        self.play(FadeIn(ball_a), FadeIn(ball_b), Create(geo_a), Create(geo_b), run_time=0.8)
        self.play(ball_a.animate.move_to(ORIGIN), ball_b.animate.move_to(ORIGIN),
                  run_time=2.8, rate_func=rate_functions.ease_in_sine)
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in [title, flat_grid, mass, mass_label,
                                          ball_a, ball_b, geo_a, geo_b, conv_label]], run_time=0.8)

    def wheeler_quote(self):
        box = RoundedRectangle(
            width=10.5, height=3.2, corner_radius=0.3,
            fill_color="#111111", fill_opacity=1,
            stroke_color=ACCENT_COLOR, stroke_width=3
        ).move_to(ORIGIN)
        line1 = Text('"Mass tells spacetime how to curve;', font_size=34, color=WHITE).move_to(box.get_center() + UP * 0.45)
        line2 = Text('curved spacetime tells matter how to move."', font_size=34, color=WHITE).move_to(box.get_center() + DOWN * 0.45)
        attribution = Text("-- John Archibald Wheeler", font_size=22, color=GREY_B).next_to(box, DOWN, buff=0.3)

        self.play(FadeIn(box, scale=0.9), run_time=0.7)
        self.play(Write(line1, run_time=1.4))
        self.play(Write(line2, run_time=1.6))
        self.play(FadeIn(attribution, shift=UP * 0.1), run_time=0.6)
        self.wait(1.0)

        highlight = SurroundingRectangle(line2, color=ACCENT_COLOR, buff=0.15, stroke_width=2.5)
        self.play(Create(highlight), run_time=0.8)
        self.wait(4.0)
        self.play(FadeOut(highlight), run_time=0.3)
        self.wait(1.5)
        self.play(FadeOut(box), FadeOut(line1), FadeOut(line2), FadeOut(attribution), run_time=0.8)