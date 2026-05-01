"""
video_3/scene_2.py
Scene 2: The First Crack -- Gravity Can't Be Instant (0:27--~1:17)

FIXES:
  - Planets orbit around the sun, never crossing its interior.
  - Einstein's wavefront is larger and timed to overtake the planet as it continues along the orbit.
"""

import sys
sys.path.append('..')
import numpy as np
from manim import *
from utils.objects import StyledText, create_logo, BACKGROUND_COLOR, ACCENT_COLOR, TEXT_COLOR

class Scene2(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)
        Scene2.sun_instant_comparison(self)
        Scene2.speed_of_light_card(self)
        Scene2.mercury_precession(self)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    # ── C.1 ──────────────────────────────────────────────────────────────────
    def sun_instant_comparison(self):
        divider = Line(UP * 3.2, DOWN * 3.2, color=GREY_C, stroke_width=1.5)
        # Labels
        newton_lbl = Text("Newton", font_size=30, color=YELLOW, weight=BOLD).move_to(LEFT * 3.5 + UP * 3.1)
        einstein_lbl = Text("Einstein", font_size=30, color=BLUE_B, weight=BOLD).move_to(RIGHT * 3.5 + UP * 3.1)

        # Sun and planet positions
        sun_N = Circle(0.45, color=GOLD, fill_opacity=1, stroke_width=3).move_to(LEFT * 3.5 + UP * 0.5)
        sun_E = Circle(0.45, color=GOLD, fill_opacity=1, stroke_width=3).move_to(RIGHT * 3.5 + UP * 0.5)
        earth_N = Circle(0.2, color=BLUE, fill_opacity=1, stroke_width=2)
        earth_E = Circle(0.2, color=BLUE, fill_opacity=1, stroke_width=2)

        # Start planets below the sun (angle 3π/2)
        start_angle = 3 * PI / 2
        orbit_radius = 1.2
        earth_N.move_to(sun_N.get_center() + orbit_radius * (np.cos(start_angle) * RIGHT + np.sin(start_angle) * UP))
        earth_E.move_to(sun_E.get_center() + orbit_radius * (np.cos(start_angle) * RIGHT + np.sin(start_angle) * UP))

        # Build a quarter‑circle arc (centre at sun) from start_angle to 0 (right)
        arc_N = Arc(radius=orbit_radius, arc_center=sun_N.get_center(),
                    start_angle=start_angle, angle=TAU/4, color=WHITE, stroke_width=0)
        arc_E = Arc(radius=orbit_radius, arc_center=sun_E.get_center(),
                    start_angle=start_angle, angle=TAU/4, color=WHITE, stroke_width=0)

        self.play(Create(divider), FadeIn(newton_lbl), FadeIn(einstein_lbl),
                  FadeIn(sun_N), FadeIn(sun_E), FadeIn(earth_N), FadeIn(earth_E), run_time=0.8)
        self.wait(0.3)

        # Simultaneous orbital motion
        self.play(MoveAlongPath(earth_N, arc_N), MoveAlongPath(earth_E, arc_E),
                  run_time=1.5, rate_func=linear)
        self.wait(0.2)

        # Both suns explode
        flash_N = Flash(sun_N.get_center(), color=YELLOW, flash_radius=0.7)
        flash_E = Flash(sun_E.get_center(), color=YELLOW, flash_radius=0.7)
        self.play(FadeOut(sun_N), FadeOut(sun_E), flash_N, flash_E, run_time=0.5)

        # Newton: instant straight up (tangent at rightmost point)
        self.play(earth_N.animate.shift(UP * 2.5), run_time=1.2, rate_func=linear)

        # Einstein: wavefront expands while planet continues along the orbit
        wavefront = Circle(radius=0.2, color=ORANGE, stroke_width=4, fill_opacity=0)
        wavefront.move_to(sun_E.get_center())
        # Planet continues from angle 0 to angle π/3 (60°) while wavefront grows
        arc_continue = Arc(radius=orbit_radius, arc_center=sun_E.get_center(),
                           start_angle=0, angle=PI/3, color=WHITE, stroke_width=0)
        # Compute final position for the planet after this extra motion
        final_angle = PI/3
        final_pos = sun_E.get_center() + orbit_radius * (np.cos(final_angle)*RIGHT + np.sin(final_angle)*UP)
        self.play(
            MoveAlongPath(earth_E, arc_continue),
            GrowFromCenter(wavefront, rate_func=linear),
            run_time=1.8
        )
        # Wavefront reaches the planet → tangent flight
        tangent_dir = UP * np.cos(final_angle) + RIGHT * np.sin(final_angle)
        self.play(
            earth_E.animate.shift(tangent_dir * 2.0),
            wavefront.animate.set_stroke(opacity=0),
            run_time=1.2, rate_func=linear
        )
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in [divider, newton_lbl, einstein_lbl,
                                          earth_N, earth_E, wavefront]], run_time=0.8)

    # ── Speed-of-light fact card (unchanged) ─────────────────────────────────
    def speed_of_light_card(self):
        title = Text("Key Facts:", font_size=34, color=ACCENT_COLOR, weight=BOLD).shift(UP * 2.2)
        eq1 = MathTex(r"c = 3.0 \times 10^8 \text{ m/s}", font_size=52, color=WHITE).next_to(title, DOWN, buff=0.6)
        eq2 = MathTex(r"\Delta t_{\odot \to \oplus} \approx 8 \text{ minutes}", font_size=52, color=WHITE).next_to(eq1, DOWN, buff=0.55)
        note = Text("Gravity cannot outrun light.", font_size=28, color=GREY_B).next_to(eq2, DOWN, buff=0.6)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)
        self.play(Write(eq1), run_time=1.0)
        self.play(Write(eq2), run_time=1.0)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(3.5)
        self.play(*[FadeOut(m) for m in [title, eq1, eq2, note]], run_time=0.8)

    # ── C.2 Mercury precession (unchanged, already correct) ──────────────────
    def mercury_precession(self):
        sun = Circle(0.35, fill_color=YELLOW, fill_opacity=1, stroke_color=GOLD, stroke_width=3).move_to(LEFT * 0.6 + DOWN * 0.1)
        newton_orbit = Ellipse(5.5, 3.2, color=GREY_C, stroke_width=2).move_to(sun.get_center() + RIGHT * 0.55)
        newton_label = Text("Newton: closed orbit", font_size=22, color=GREY_C).to_edge(DOWN, buff=1.1).shift(LEFT * 1.5)
        observed_orbit = Ellipse(5.5, 3.2, color=YELLOW, stroke_width=2.5).move_to(sun.get_center() + RIGHT * 0.55)
        observed_label = Text("Observed: slow precession", font_size=22, color=YELLOW).next_to(newton_label, RIGHT, buff=0.4)
        perihelion_dot = Dot(observed_orbit.get_right(), color=RED, radius=0.1)
        perihelion_label = Text("perihelion", font_size=18, color=RED).next_to(perihelion_dot, UP, buff=0.15)
        title = Text("Mercury's Anomalous Precession", font_size=28, color=ACCENT_COLOR).to_edge(UP, buff=0.5)

        self.play(FadeIn(title), FadeIn(sun), Create(newton_orbit), FadeIn(newton_label), run_time=1.0)
        self.wait(0.5)
        self.play(Create(observed_orbit), FadeIn(observed_label), FadeIn(perihelion_dot), FadeIn(perihelion_label), run_time=0.8)
        self.wait(1.0)

        annotation = MathTex(r"43 \text{ arcsec / century -- unexplained by Newton}", font_size=26, color=RED).to_edge(UP, buff=1.3)
        for i in range(5):
            new_orbit = Ellipse(5.5, 3.2, color=YELLOW, stroke_width=2.5).move_to(sun.get_center() + RIGHT * 0.55)
            new_orbit.rotate(PI/30 * (i+1), about_point=sun.get_center())
            new_dot = Dot(new_orbit.get_right(), color=RED, radius=0.1)
            new_lbl = Text("perihelion", font_size=18, color=RED).next_to(new_dot, UP, buff=0.15)
            self.play(FadeOut(observed_orbit), FadeOut(perihelion_dot), FadeOut(perihelion_label),
                      Create(new_orbit), FadeIn(new_dot), FadeIn(new_lbl), run_time=0.3)
            observed_orbit, perihelion_dot, perihelion_label = new_orbit, new_dot, new_lbl
            if i == 0:
                self.play(FadeIn(annotation), run_time=0.2)
        self.wait(3.0)
        self.play(*[FadeOut(m) for m in [title, sun, newton_orbit, newton_label,
                                          observed_orbit, observed_label,
                                          perihelion_dot, perihelion_label, annotation]], run_time=0.8)