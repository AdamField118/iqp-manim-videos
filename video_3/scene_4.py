"""
video_3/scene_4.py
Scene 4: Einstein's Revolutionary Idea (2:51--~4:05)
FIXES:
  - Title scaled to fit screen.
  - Spacetime grid uses multi-point VMobjects (not Lines) so apply_function
    warps every intermediate sample and curvature is actually visible.
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

    # ── Helper: build grid as multi-point VMobjects ─────────────────────────
    # Each grid line is a VMobject with n_pts corner samples rather than a
    # plain Line (which has only 2 anchor points).  apply_function then warps
    # every intermediate sample, making the curvature clearly visible.
    def create_flat_grid(self, size=4.5, step=0.5, color=BLUE_E, opacity=0.5):
        lines = VGroup()
        n_pts = 60   # samples per line – more = smoother curve after warp
        for x in np.arange(-size, size + step, step):
            pts = [np.array([x, y, 0]) for y in np.linspace(-size, size, n_pts)]
            vmo = VMobject(stroke_color=color, stroke_opacity=opacity, stroke_width=0.8)
            vmo.set_points_as_corners(pts)
            lines.add(vmo)
        for y in np.arange(-size, size + step, step):
            pts = [np.array([x, y, 0]) for x in np.linspace(-size, size, n_pts)]
            vmo = VMobject(stroke_color=color, stroke_opacity=opacity, stroke_width=0.8)
            vmo.set_points_as_corners(pts)
            lines.add(vmo)
        return lines

    def spacetime_grid(self):
        title = Text("Spacetime Curvature", font_size=30, color=ACCENT_COLOR, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.5)

        # Perspective-projection parameters
        
        # We fake a 3D gravity-well by mapping every grid point (x, y) to a
        # 3D position (x, y, z_3d) where z_3d is the funnel depression, then
        # projecting onto the screen with a tilt angle phi:
        #   x_screen = x
        #   y_screen = y·sin(phi) + z_3d·cos(phi)
        # phi = 90° means looking straight down (no tilt, z invisible).
        # phi = 0°  means looking edge-on (grid collapses to a line).
        # phi ~ 55° gives a nice oblique view where the funnel reads clearly.
        phi   = 55 * DEGREES
        A     = 2.4   # funnel depth
        sigma = 1.6   # funnel width (Gaussian σ²)
        GRID  = 3.2   # grid half-extent (units)
        SHIFT = UP * 0.55  # nudge whole grid upward so funnel stays in frame

        def flat_proj(p):
            """Tilt-only projection (z_3d = 0, i.e. flat sheet viewed at angle)."""
            x, y = p[0], p[1]
            return np.array([x, y * np.sin(phi), 0])

        def warp_proj(p):
            """Gravity-well depression + same tilt projection."""
            x, y = p[0], p[1]
            r     = np.sqrt(x**2 + y**2) + 0.01
            z_3d  = -A * np.exp(-r**2 / sigma)
            return np.array([x, y * np.sin(phi) + z_3d * np.cos(phi), 0])

        # Build source grid once; create two projected copies from it so that
        # Transform() can interpolate point-for-point between them.
        source = Scene4.create_flat_grid(self, size=GRID, step=0.42, color=BLUE_E)
        grid_flat   = source.copy().apply_function(flat_proj)
        grid_warped = source.copy().apply_function(warp_proj)
        grid_flat.shift(SHIFT)
        grid_warped.shift(SHIFT)

        # Show flat (tilted) grid
        flat_label = Text("flat spacetime", font_size=22, color=GREY_B).to_edge(DOWN, buff=0.5)
        self.play(Create(grid_flat, lag_ratio=0.02), run_time=1.5)
        self.play(FadeIn(flat_label), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(flat_label), run_time=0.3)

        # Mass sits at the flat-grid centre before the warp
        mass_flat_pos   = flat_proj(np.array([0, 0, 0])) + SHIFT
        mass_warped_pos = warp_proj(np.array([0, 0, 0])) + SHIFT   # bottom of funnel

        mass = Circle(0.28, fill_color="#e8a000", fill_opacity=1, stroke_color=GOLD, stroke_width=3)
        mass.move_to(mass_flat_pos)
        mass_label = Text("mass", font_size=20, color=GOLD).next_to(mass, RIGHT, buff=0.25)
        self.play(GrowFromCenter(mass), FadeIn(mass_label), run_time=0.8)

        # Transform flat -> warped (grid bends into the funnel)
        curved_label = Text("curved spacetime", font_size=22, color=BLUE_B).to_edge(DOWN, buff=0.5)
        self.play(
            Transform(grid_flat, grid_warped),
            mass.animate.move_to(mass_warped_pos),
            FadeIn(curved_label),
            run_time=2.0,
        )
        self.wait(1.5)

        # Green marble orbiting the well (geodesic)
        r_orb = 2.2   # orbital radius in grid-plane coords
        z_orb = -A * np.exp(-r_orb**2 / sigma)   # constant z_3d on this ring

        def orb(t):
            x     = r_orb * np.cos(t)
            y_raw = r_orb * np.sin(t)
            return np.array([x, y_raw * np.sin(phi) + z_orb * np.cos(phi), 0]) + SHIFT

        orbit     = ParametricFunction(orb, t_range=[-PI, PI], color=GREEN, stroke_width=2)
        small_obj = Dot(0.12, color=GREEN).move_to(orbit.get_start())

        self.play(FadeOut(curved_label), run_time=0.3)
        self.play(Create(orbit), run_time=0.6)
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

        # Start above the funnel on the grid surface; converge to the well bottom
        start_a = mass_warped_pos + LEFT * 0.6 + UP * 1.6
        start_b = mass_warped_pos + RIGHT * 0.6 + UP * 1.6
        ball_a = Dot(0.14, color=YELLOW).move_to(start_a)
        ball_b = Dot(0.14, color=YELLOW).move_to(start_b)
        geo_a = DashedLine(start_a, mass_warped_pos, color=YELLOW_A, stroke_width=1.8, dash_length=0.12)
        geo_b = DashedLine(start_b, mass_warped_pos, color=YELLOW_A, stroke_width=1.8, dash_length=0.12)

        self.play(FadeIn(ball_a), FadeIn(ball_b), Create(geo_a), Create(geo_b), run_time=0.8)
        self.play(ball_a.animate.move_to(mass_warped_pos), ball_b.animate.move_to(mass_warped_pos),
                  run_time=2.8, rate_func=rate_functions.ease_in_sine)
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in [title, grid_flat, mass, mass_label,
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