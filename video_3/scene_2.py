"""
video_3/scene_2.py
Scene 2: The First Crack -- Gravity Can't Be Instant (0:27--~1:17)

FIXES:
  - Planets orbit around the sun, never crossing its interior.
  - Einstein wavefront explicitly grows from tiny to orbit_radius via Transform,
    so it visually reaches the planet at the end of the animation.
  - Tangent direction at fly-off uses the correct CCW formula:
    (-sin θ, cos θ) instead of the erroneous (sin θ, cos θ) that was
    sending the planet radially outward.
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
        newton_lbl  = Text("Newton",  font_size=30, color=YELLOW, weight=BOLD).move_to(LEFT  * 3.5 + UP * 3.1)
        einstein_lbl = Text("Einstein", font_size=30, color=BLUE_B,  weight=BOLD).move_to(RIGHT * 3.5 + UP * 3.1)

        # Store sun centres as plain vectors so they're still valid after FadeOut
        sun_center_N = LEFT  * 3.5 + UP * 0.5
        sun_center_E = RIGHT * 3.5 + UP * 0.5

        sun_N = Circle(0.45, color=GOLD, fill_opacity=1, stroke_width=3).move_to(sun_center_N)
        sun_E = Circle(0.45, color=GOLD, fill_opacity=1, stroke_width=3).move_to(sun_center_E)

        orbit_radius = 1.3
        start_angle  = 3 * PI / 2   # bottom of orbit

        earth_N = Circle(0.2, color=BLUE, fill_opacity=1, stroke_width=2)
        earth_E = Circle(0.2, color=BLUE, fill_opacity=1, stroke_width=2)
        earth_N.move_to(sun_center_N + orbit_radius * np.array([np.cos(start_angle), np.sin(start_angle), 0]))
        earth_E.move_to(sun_center_E + orbit_radius * np.array([np.cos(start_angle), np.sin(start_angle), 0]))

        # Quarter-circle CCW: bottom (3π/2) → right (0 / 2π)
        arc_N = Arc(radius=orbit_radius, arc_center=sun_center_N,
                    start_angle=start_angle, angle=TAU / 4, color=WHITE, stroke_width=0)
        arc_E = Arc(radius=orbit_radius, arc_center=sun_center_E,
                    start_angle=start_angle, angle=TAU / 4, color=WHITE, stroke_width=0)

        self.play(Create(divider), FadeIn(newton_lbl), FadeIn(einstein_lbl),
                  FadeIn(sun_N), FadeIn(sun_E), FadeIn(earth_N), FadeIn(earth_E), run_time=0.8)
        self.wait(0.3)

        # Both planets orbit together (CCW quarter-circle)
        self.play(MoveAlongPath(earth_N, arc_N), MoveAlongPath(earth_E, arc_E),
                  run_time=1.5, rate_func=linear)
        self.wait(0.2)

        # Suns suddenly disappear
        flash_N = Flash(sun_center_N, color=YELLOW, flash_radius=0.7)
        flash_E = Flash(sun_center_E, color=YELLOW, flash_radius=0.7)
        self.play(FadeOut(sun_N), FadeOut(sun_E), flash_N, flash_E, run_time=0.5)

        # ── Newton side: force vanishes instantly ────────────────────────────
        # Planet is now at angle 0 (rightmost point).
        # CCW tangent at θ=0 is (-sin 0, cos 0) = (0, 1) = straight UP.
        self.play(earth_N.animate.shift(UP * 2.5), run_time=1.2, rate_func=linear)

        # ── Einstein side: wavefront travels at c while planet keeps orbiting ─
        # Planet is at angle 0 (rightmost point); it will continue along the
        # orbit for extra_angle while the wavefront expands to reach it.

        extra_angle = PI / 3          # ~60° of additional orbit
        final_angle = 0 + extra_angle  # = π/3

        # Wavefront starts tiny at the old sun position, grows to orbit_radius
        wavefront_start = Circle(
            radius=0.05, color=ORANGE, stroke_width=4, fill_opacity=0
        ).move_to(sun_center_E)
        wavefront_end = Circle(
            radius=orbit_radius, color=ORANGE, stroke_width=2, fill_opacity=0
        ).move_to(sun_center_E)

        self.add(wavefront_start)

        # Planet continues orbiting from angle 0 to final_angle (CCW)
        arc_continue = Arc(
            radius=orbit_radius, arc_center=sun_center_E,
            start_angle=0, angle=extra_angle, color=WHITE, stroke_width=0
        )

        # Animate simultaneously: planet orbits, wavefront expands to orbit_radius.
        # Both finish at the same instant — wavefront just reaches the planet.
        self.play(
            MoveAlongPath(earth_E, arc_continue),
            Transform(wavefront_start, wavefront_end),
            run_time=1.8,
            rate_func=linear
        )

        # Now the wavefront has reached the planet.  Planet flies off tangentially.
        # CCW tangent at angle θ = (-sin θ, cos θ, 0)
        tangent_dir = np.array([-np.sin(final_angle), np.cos(final_angle), 0])

        self.play(
            earth_E.animate.shift(tangent_dir * 2.2),
            wavefront_start.animate.set_stroke(opacity=0),
            run_time=1.2,
            rate_func=linear,
        )
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in [
            divider, newton_lbl, einstein_lbl,
            earth_N, earth_E, wavefront_start,
        ]], run_time=0.8)

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

    # ── C.2 Mercury precession (unchanged) ───────────────────────────────────
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
        # Mirror Manim's own rotate() call: take the exact initial tip reported
        # by get_right(), store its offset from the sun, then apply a 2-D
        # rotation matrix for each cumulative angle.  This is pixel-perfect
        # because we're doing the identical transform Manim does to the orbit.
        sun_np_2    = np.array(sun.get_center())
        peri_offset = np.array(observed_orbit.get_right()) - sun_np_2
        for i in range(5):
            total_angle = PI/30 * (i+1)
            new_orbit = Ellipse(5.5, 3.2, color=YELLOW, stroke_width=2.5).move_to(sun.get_center() + RIGHT * 0.55)
            new_orbit.rotate(total_angle, about_point=sun.get_center())
            c, s = np.cos(total_angle), np.sin(total_angle)
            peri_pos = sun_np_2 + np.array([
                c * peri_offset[0] - s * peri_offset[1],
                s * peri_offset[0] + c * peri_offset[1],
                0,
            ])
            new_dot = Dot(peri_pos, color=RED, radius=0.1)
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