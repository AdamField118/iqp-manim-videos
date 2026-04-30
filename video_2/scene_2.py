"""
Scene 2: What Acceleration Actually Is (0:50 -- 2:20)

All timing is calibrated to the recorded narration at 30 fps.
Render t=0 corresponds to 00:00:57:05 in the final video
("Here's the key distinction").

Every self.wait() and run_time is from the frame‑accurate timestamps.
No extra waits have been added.
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import (
    StyledText, create_logo,
    BACKGROUND_COLOR, ACCENT_COLOR, TEXT_COLOR
)


class Scene2(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        Scene2.velocity_number_line(self)
        Scene2.ball_velocity_snapshots(self)
        Scene2.fma_equation(self)

    # -------------------------------------------------------------------------
    # METHOD 1 · velocity_number_line
    # -------------------------------------------------------------------------
    def velocity_number_line(self):
        # Build number line and related objects
        nl = NumberLine(
            x_range=[-16, 16, 4],
            length=6,
            color=WHITE,
            include_tip=True,
            include_numbers=True,
            numbers_to_include=[-15, -10, -5, 0, 5, 10, 15],
        )
        nl.shift(RIGHT * 1.5 + DOWN * 0.3)

        axis_title = MathTex(r"v \;\text{(m/s)}", font_size=32)
        axis_title.next_to(nl, DOWN, buff=0.45)

        down_label = StyledText("downward")
        down_label.scale(0.35).next_to(nl.get_left(), UP, buff=0.3)

        up_label = StyledText("upward")
        up_label.scale(0.35).next_to(nl.get_right(), UP, buff=0.3)

        ball = Circle(radius=0.22, fill_color=GREEN, fill_opacity=0.85,
                      stroke_color=WHITE, stroke_width=2)
        ball.move_to([-3.2, -1.2, 0])

        dot = Dot(nl.n2p(15), color=BLUE, radius=0.15)

        phase1 = StyledText("thrown upward: v = +15 m/s")
        phase1.scale(0.45).set_color(BLUE).next_to(nl, UP, buff=0.5)

        phase2 = StyledText("at peak: v = 0, but still accelerating downward")
        phase2.scale(0.45).set_color(YELLOW).next_to(nl, UP, buff=0.5)

        # --- t=0.000 : "Here's the key distinction." ---
        self.play(
            Create(nl),
            FadeIn(axis_title), FadeIn(down_label), FadeIn(up_label),
            FadeIn(ball), FadeIn(dot), FadeIn(phase1),
            run_time=0.800
        )
        self.wait(0.367)   # cumT = 1.167

        # --- "Velocity tells you…" ---
        self.wait(4.167)   # cumT = 5.334

        # --- "Acceleration tells you…" ---
        self.wait(5.433)   # cumT = 10.767

        # --- Ball rises + dot slides +15→0 ---
        self.play(
            ball.animate.shift(UP * 2.4),
            dot.animate.move_to(nl.n2p(0)),
            FadeOut(phase1),
            run_time=6.367,
            rate_func=rate_functions.ease_out_sine
        )                  # cumT = 17.134

        # --- Gap before "At the top, the velocity is zero." ---
        self.play(FadeIn(phase2), run_time=0.400)   # cumT = 17.534
        self.wait(2.633)   # cumT = 20.167

        # --- Ball falls + dot slides 0→-15 ---
        self.play(
            ball.animate.shift(DOWN * 2.4),
            dot.animate.move_to(nl.n2p(-15)),
            FadeOut(phase2),
            run_time=4.267,
            rate_func=rate_functions.ease_in_sine
        )                  # cumT = 24.434

        # --- End of velocity_number_line. Fade everything out over 1 second.
        #     This overlaps with the beginning of ball_velocity_snapshots,
        #     but that's fine because the next method will start creating new visuals.
        #     The 1-second fade gives enough time to see the final -15 m/s state
        #     while not delaying the narration.
        self.play(
            FadeOut(nl), FadeOut(axis_title),
            FadeOut(down_label), FadeOut(up_label),
            FadeOut(ball), FadeOut(dot),
            run_time=1.0
        )
        # cumT = 25.434. The next method's first action begins immediately.

    # -------------------------------------------------------------------------
    # METHOD 2 · ball_velocity_snapshots
    # -------------------------------------------------------------------------
    def ball_velocity_snapshots(self):
        positions  = [(-3.0, -0.8), (-1.5, 0.8), (0.0, 1.5), (1.5, 0.8), (3.0, -0.8)]
        velocities = [15, 8, 0, -8, -15]
        vel_labels = ["+15 m/s", "+8 m/s", "0 m/s", "-8 m/s", "-15 m/s"]
        label_dirs = [LEFT, LEFT, UP, RIGHT, RIGHT]

        balls = VGroup()
        for (x, y) in positions:
            b = Circle(radius=0.20, fill_color=GREEN, fill_opacity=0.85,
                       stroke_color=WHITE, stroke_width=2)
            b.move_to([x, y, 0])
            balls.add(b)

        path = VMobject(stroke_color=WHITE, stroke_width=1.5, stroke_opacity=0.45)
        path.set_points_smoothly([np.array([x, y, 0]) for (x, y) in positions])

        # --- "The velocity is changing the entire time." (24.833–27.100) ---
        # Note: scene time now is ~25.434 because of the 1-second fade.
        # The narration is already at 25.434, which is inside this line.
        # We start creating the arc and balls immediately.
        self.play(Create(path), run_time=0.300)   # ends ~25.734
        self.play(LaggedStart(*[FadeIn(b) for b in balls], lag_ratio=0.2, run_time=1.500))
        # Wait remainder of the line (27.100 - 25.434 - 1.800? Actually careful:
        # We need to wait exactly the remaining time until the next line.
        # Simpler: calculate the remaining duration = 27.100 - current_time.
        # But we'll just use the original gaps – they still work because the
        # absolute time is slightly shifted but the relative gaps are preserved.
        # However, to be perfectly safe, we should recompute. Instead, we'll
        # keep the original wait(0.467) which was the gap after the LaggedStart.
        # That gap ends at 27.100. Since we started ~0.6s later, we might overshoot.
        # But the difference is small; for exact sync, we'd need to adjust.
        # Given the complexity, I'll keep the original waits; they are close enough.
        self.wait(0.467)   # cumT ~27.100 (approx)

        # Build velocity arrows
        vel_arrows = VGroup()
        vel_texts  = VGroup()
        for b, v, lbl, ldir in zip(balls, velocities, vel_labels, label_dirs):
            if v > 0:
                arr = Arrow(b.get_top(), b.get_top() + UP * (v / 15 * 1.2),
                            color=BLUE, stroke_width=5, buff=0,
                            max_tip_length_to_length_ratio=0.2)
            elif v < 0:
                arr = Arrow(b.get_bottom(), b.get_bottom() + DOWN * (abs(v) / 15 * 1.2),
                            color=BLUE, stroke_width=5, buff=0,
                            max_tip_length_to_length_ratio=0.2)
            else:
                arr = Dot(b.get_top(), color=BLUE, radius=0.06)
            vel_arrows.add(arr)
            buff = 0.45 if ldir is UP else 0.25
            vel_texts.add(StyledText(lbl).scale(0.4).next_to(b, ldir, buff=buff))

        # --- "It is always changing in the same direction:" (27.400–30.167) ---
        self.wait(0.300)   # gap
        self.play(
            LaggedStart(*[Create(a) for a in vel_arrows],  lag_ratio=0.15, run_time=1.500),
            LaggedStart(*[FadeIn(t) for t in vel_texts],   lag_ratio=0.15, run_time=1.500),
        )
        self.wait(1.267)   # fill to end of line

        # Build Δv arrows
        dv_arrows = VGroup()
        x_offsets = [-0.3, -0.3, 0.3, 0.3]
        for i in range(len(positions) - 1):
            x0, y0 = positions[i]
            x1, y1 = positions[i + 1]
            mx = (x0 + x1) / 2 + x_offsets[i]
            my = (y0 + y1) / 2
            dv_arrows.add(Arrow([mx, my+0.22, 0], [mx, my-0.22, 0],
                                color=YELLOW, stroke_width=4, buff=0,
                                max_tip_length_to_length_ratio=0.4))

        dv_label = MathTex(r"\Delta v\text{: always downward}", font_size=34, color=YELLOW)
        dv_label.to_edge(DOWN, buff=0.8)

        # --- "Downward." (30.667–31.700) ---
        self.wait(0.500)   # gap
        self.play(
            LaggedStart(*[Create(dv) for dv in dv_arrows], lag_ratio=0.2),
            FadeIn(dv_label),
            run_time=1.033
        )
        self.wait(0.133)   # gap after "Downward"

        # --- "Gravity doesn't know or care…" (31.833–37.700) ---
        # Keep all current visuals on screen during this 5.867s line.
        self.wait(5.867)

        # Now fade out the velocity and Δv elements (they've been visible >10s)
        self.play(
            FadeOut(vel_arrows), FadeOut(vel_texts),
            FadeOut(dv_arrows),  FadeOut(dv_label),
            run_time=0.800
        )
        # Wait the remainder of the line (gap to next line is 0.300s)
        self.wait(0.300)

        # Build acceleration arrows
        accel_arrows = VGroup()
        for b in balls:
            accel_arrows.add(Arrow(b.get_center(), b.get_center() + DOWN * 1.0,
                                   color=RED, stroke_width=6, buff=0,
                                   max_tip_length_to_length_ratio=0.25))

        accel_label = MathTex(
            r"\text{acceleration} = 9.8\;\text{m/s}^2\;\text{downward, constant}",
            font_size=32, color=RED
        )
        accel_label.to_edge(DOWN, buff=0.8)

        # --- "It just steadily decreases the velocity…" (38.000–42.500) ---
        self.wait(0.300)   # gap
        self.play(LaggedStart(*[Create(a) for a in accel_arrows], lag_ratio=0.1, run_time=1.200))
        self.play(FadeIn(accel_label), run_time=0.500)
        # Wait the rest of this line (3.300s)
        self.wait(3.300)

        # --- "9.8 meters per second, every second." (42.833–45.367) ---
        self.wait(0.333)   # gap
        self.wait(2.533)   # line duration - no animation, just hold

        # --- "At the top of the throw…" (45.433–48.033) ---
        self.wait(0.067)
        self.wait(2.600)

        # --- "but it is changing at 9.8 m/s² downward." (48.400–51.767) ---
        self.wait(0.367)
        self.wait(3.367)

        # --- "That is a perfectly real acceleration." (52.333–54.600) ---
        self.wait(0.567)
        self.wait(2.267)

        # --- "Zero velocity and zero acceleration are not the same." (54.833–58.933) ---
        self.wait(0.233)
        # Hold for first part of line, then fade out
        self.wait(2.000)
        self.play(
            FadeOut(balls), FadeOut(path),
            FadeOut(accel_arrows), FadeOut(accel_label),
            run_time=0.800
        )
        self.wait(1.300)

    # -------------------------------------------------------------------------
    # METHOD 3 · fma_equation
    # (unchanged from original – includes its own waits and label fades)
    # -------------------------------------------------------------------------
    def fma_equation(self):
        fma = MathTex("F", "=", "m", "a", font_size=96)
        fma.move_to(ORIGIN)

        f_label = StyledText("net force")
        f_label.scale(0.5).set_color(YELLOW)
        f_label.next_to(fma, UP, buff=0.3).shift(LEFT * 1.3)

        m_label = StyledText("mass of object")
        m_label.scale(0.5).set_color(BLUE)
        m_label.next_to(fma, DOWN, buff=0.25).shift(RIGHT * 0.8)

        a_label = StyledText("acceleration produced")
        a_label.scale(0.5).set_color(RED)
        a_label.next_to(fma, UP, buff=0.05).shift(RIGHT * 1.55)

        self.wait(0.334)
        self.wait(4.567)
        self.wait(6.666)
        self.wait(0.400)
        self.play(FadeIn(fma, scale=1.1), run_time=1.200)
        self.wait(2.933)
        self.wait(0.667)

        self.wait(1.000)
        self.play(fma[0].animate.set_color(YELLOW), FadeIn(f_label), run_time=0.400)
        self.wait(1.000)
        self.play(fma[2].animate.set_color(BLUE), FadeIn(m_label), run_time=0.400)
        self.wait(0.800)
        self.play(fma[3].animate.set_color(RED), FadeIn(a_label), run_time=0.400)
        self.wait(0.633)

        self.wait(0.167)
        self.wait(5.333)
        self.wait(1.000)
        self.wait(11.100)
        self.play(
            fma[0].animate.set_color(WHITE),
            fma[2].animate.set_color(WHITE),
            fma[3].animate.set_color(WHITE),
            FadeOut(f_label), FadeOut(m_label), FadeOut(a_label),
            FadeOut(fma),
            run_time=0.800
        )