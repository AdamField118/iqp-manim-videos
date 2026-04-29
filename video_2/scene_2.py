"""
Scene 2: What Acceleration Actually Is (0:50 -- 2:20)

All timing is calibrated to the recorded narration at 30 fps.
Render t=0 corresponds to 00:00:57:05 in the final video
("Here's the key distinction.").

Every self.wait() and run_time is derived from the frame-accurate timestamps
below.  Gaps between lines are preserved so animation beats land on the
correct spoken word.

Narration timestamps (relative to render t=0):
  "Here's the key distinction."                   0.000 – 1.167  (1.167s)
  "Velocity tells you…"                           1.367 – 5.333  (3.967s, gap 0.200)
  "Acceleration tells you…"                       5.767 – 10.767 (5.000s, gap 0.433)
  "Watch the ball's velocity…"                   10.833 – 13.033 (2.200s, gap 0.067)
  "On the way up…"                               13.167 – 17.133 (3.967s, gap 0.133)
  "At the top, the velocity is zero."            17.933 – 20.167 (2.233s, gap 0.800)
  "On the way down…"                             20.667 – 24.433 (3.767s, gap 0.500)
  "The velocity is changing the entire time."    24.833 – 27.100 (2.267s, gap 0.400)
  "It is always changing in the same direction:" 27.400 – 30.167 (2.767s, gap 0.300)
  "Downward."                                    30.667 – 31.700 (1.033s, gap 0.500)
  "Gravity doesn't know or care…"               31.833 – 37.700 (5.867s, gap 0.133)
  "It just steadily decreases…"                 38.000 – 42.500 (4.500s, gap 0.300)
  "9.8 meters per second, every second."         42.833 – 45.367 (2.533s, gap 0.333)
  "At the top of the throw…"                     45.433 – 48.033 (2.600s, gap 0.067)
  "but it is changing at 9.8 m/s² downward."    48.400 – 51.767 (3.367s, gap 0.367)
  "That is a perfectly real acceleration."       52.333 – 54.600 (2.267s, gap 0.567)
  "Zero velocity and zero acceleration…"         54.833 – 58.933 (4.100s, gap 0.233)
  "So what's causing that acceleration? A force."59.267 – 63.833 (4.567s, gap 0.333)
  "Gravity is pulling the ball downward…"        63.333 – 70.500 (7.167s, overlap -0.500)
  "And Newton gave us…"                          70.900 – 75.033 (4.133s, gap 0.400)
  "Newton's Second Law: force equals…"           75.700 – 80.333 (4.633s, gap 0.667)
  "If you know the force…"                       80.500 – 85.833 (5.333s, gap 0.167)
  "This is the bridge…"                          86.833 – 98.733 (11.900s, gap 1.000)
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

    # ─────────────────────────────────────────────────────────────────────────
    # METHOD 1 · velocity_number_line
    # Entry scene_t = 0.000   Exit scene_t ≈ 24.833
    # ─────────────────────────────────────────────────────────────────────────
    def velocity_number_line(self):
        # ── Build all objects ─────────────────────────────────────────────────
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

        # Ball starts LOW on the left half — it has already been thrown upward
        ball = Circle(radius=0.22, fill_color=GREEN, fill_opacity=0.85,
                      stroke_color=WHITE, stroke_width=2)
        ball.move_to([-3.2, -1.2, 0])

        # Dot starts at +15 (high velocity, just thrown)
        dot = Dot(nl.n2p(15), color=BLUE, radius=0.15)

        phase1 = StyledText("thrown upward: v = +15 m/s")
        phase1.scale(0.45).set_color(BLUE).next_to(nl, UP, buff=0.5)

        phase2 = StyledText("at peak: v = 0, but still accelerating downward")
        phase2.scale(0.45).set_color(YELLOW).next_to(nl, UP, buff=0.5)

        # ── t = 0.000 ─ ALL appear as "Here's the key distinction." begins ──
        # run_time 0.800 -> cumT = 0.800
        self.play(
            Create(nl),
            FadeIn(axis_title), FadeIn(down_label), FadeIn(up_label),
            FadeIn(ball), FadeIn(dot), FadeIn(phase1),
            run_time=0.800
        )
        # "Here's the key distinction." ends at 1.167 -> hold 0.367
        self.wait(0.367)   # cumT = 1.167

        # ── Static: "Velocity tells you how fast something is moving…" ───────
        # gap 0.200 + line 3.967 = 4.167
        self.wait(4.167)   # cumT = 5.334

        # ── Static: "Acceleration tells you how quickly that velocity is changing…"
        # gap 0.433 + line 5.000 = 5.433
        self.wait(5.433)   # cumT = 10.767

        # ── Ball rises + dot slides +15->0 ────────────────────────────────────
        # Covers: gap(0.067) + "Watch the ball's velocity…"(2.200)
        #       + gap(0.133) + "On the way up, it's moving upward…"(3.967)
        # = 6.367 s total.  Ball arrives at peak exactly as "On the way up" ends.
        # run_time 6.367 -> cumT = 17.134
        self.play(
            ball.animate.shift(UP * 2.4),
            dot.animate.move_to(nl.n2p(0)),
            FadeOut(phase1),
            run_time=6.367,
            rate_func=rate_functions.ease_out_sine
        )

        # ── Gap 0.800 before "At the top, the velocity is zero." ─────────────
        # Phase2 label fades in during this gap (0.400 s)
        self.play(FadeIn(phase2), run_time=0.400)   # cumT = 17.534
        # "At the top, the velocity is zero." ends at 20.167 -> hold 2.633
        self.wait(2.633)   # cumT = 20.167

        # ── Ball falls + dot slides 0->-15 ────────────────────────────────────
        # Covers: gap(0.500) + "On the way down, it's moving downward…"(3.767)
        # = 4.267 s total.
        # run_time 4.267 -> cumT = 24.434
        self.play(
            ball.animate.shift(DOWN * 2.4),
            dot.animate.move_to(nl.n2p(-15)),
            FadeOut(phase2),
            run_time=4.267,
            rate_func=rate_functions.ease_in_sine
        )

        # ── Fade number line out in the 0.400 s gap before "The velocity is changing…"
        # run_time 0.400 -> cumT = 24.834 ≈ 24.833 ✓
        self.play(
            FadeOut(nl), FadeOut(axis_title),
            FadeOut(down_label), FadeOut(up_label),
            FadeOut(ball), FadeOut(dot),
            run_time=0.400
        )
        # Hand off to ball_velocity_snapshots at scene_t ≈ 24.833

    # ─────────────────────────────────────────────────────────────────────────
    # METHOD 2 · ball_velocity_snapshots
    # Entry scene_t ≈ 24.833   Exit scene_t ≈ 58.933
    # ─────────────────────────────────────────────────────────────────────────
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

        # ── "The velocity is changing the entire time." (24.833–27.100) ───────
        # Arc path traces (0.300 s) -> scene = 25.133
        self.play(Create(path), run_time=0.300)
        # Five balls fade in with lag (1.500 s) -> scene = 26.633
        self.play(LaggedStart(*[FadeIn(b) for b in balls], lag_ratio=0.2, run_time=1.500))
        # Fill to end of line at 27.100 -> hold 0.467
        self.wait(0.467)   # scene = 27.100

        # ── Build velocity arrows (not yet shown) ────────────────────────────
        vel_arrows = VGroup()
        vel_texts  = VGroup()
        for b, v, lbl, ldir in zip(balls, velocities, vel_labels, label_dirs):
            if v > 0:
                arr = Arrow(
                    b.get_top(), b.get_top() + UP * (v / 15 * 1.2),
                    color=BLUE, stroke_width=5, buff=0,
                    max_tip_length_to_length_ratio=0.2
                )
            elif v < 0:
                arr = Arrow(
                    b.get_bottom(), b.get_bottom() + DOWN * (abs(v) / 15 * 1.2),
                    color=BLUE, stroke_width=5, buff=0,
                    max_tip_length_to_length_ratio=0.2
                )
            else:
                # Zero velocity: dot at surface
                arr = Dot(b.get_top(), color=BLUE, radius=0.06)
            vel_arrows.add(arr)
            buff = 0.45 if ldir is UP else 0.25
            vel_texts.add(StyledText(lbl).scale(0.4).next_to(b, ldir, buff=buff))

        # ── "It is always changing in the same direction:" (27.400–30.167) ───
        # gap 0.300 -> scene = 27.400
        self.wait(0.300)
        # Velocity arrows + labels appear over 1.500 s -> scene = 28.900
        self.play(
            LaggedStart(*[Create(a) for a in vel_arrows],  lag_ratio=0.15, run_time=1.500),
            LaggedStart(*[FadeIn(t) for t in vel_texts],   lag_ratio=0.15, run_time=1.500),
        )
        # Fill to end of line at 30.167 -> hold 1.267
        self.wait(1.267)   # scene = 30.167

        # ── Build Δv arrows (not yet shown) ─────────────────────────────────
        dv_arrows = VGroup()
        x_offsets = [-0.3, -0.3, 0.3, 0.3]
        for i in range(len(positions) - 1):
            x0, y0 = positions[i]
            x1, y1 = positions[i + 1]
            mx = (x0 + x1) / 2 + x_offsets[i]
            my = (y0 + y1) / 2
            dv_arrows.add(Arrow(
                [mx, my + 0.22, 0], [mx, my - 0.22, 0],
                color=YELLOW, stroke_width=4, buff=0,
                max_tip_length_to_length_ratio=0.4
            ))

        dv_label = MathTex(r"\Delta v\text{: always downward}", font_size=34, color=YELLOW)
        dv_label.to_edge(DOWN, buff=0.8)

        # ── "Downward." (30.667–31.700) ────────────────────────────────────
        # gap 0.500 -> scene = 30.667
        self.wait(0.500)
        # Δv arrows + label appear across the full word (1.033 s) -> scene = 31.700
        self.play(
            LaggedStart(*[Create(dv) for dv in dv_arrows], lag_ratio=0.2),
            FadeIn(dv_label),
            run_time=1.033
        )

        # ── "Gravity doesn't know or care whether the ball is moving…" (31.833–37.700)
        # gap 0.133 -> scene = 31.833
        self.wait(0.133)
        # Fade velocity arrows, texts, Δv arrows, Δv label at top of line (0.800 s)
        # -> scene = 32.633
        self.play(
            FadeOut(vel_arrows), FadeOut(vel_texts),
            FadeOut(dv_arrows),  FadeOut(dv_label),
            run_time=0.800
        )
        # Fill to end of line at 37.700 -> hold 5.067
        self.wait(5.067)   # scene = 37.700

        # ── Build acceleration arrows (equal length, red, from each ball center) ─
        accel_arrows = VGroup()
        for b in balls:
            accel_arrows.add(Arrow(
                b.get_center(), b.get_center() + DOWN * 1.0,
                color=RED, stroke_width=6, buff=0,
                max_tip_length_to_length_ratio=0.25
            ))

        accel_label = MathTex(
            r"\text{acceleration} = 9.8\;\text{m/s}^2\;\text{downward, constant}",
            font_size=32, color=RED
        )
        accel_label.to_edge(DOWN, buff=0.8)

        # ── "It just steadily decreases the velocity at the same rate…" (38.000–42.500)
        # gap 0.300 -> scene = 38.000
        self.wait(0.300)
        # Acceleration arrows appear at the top of this line (1.200 s) -> scene = 39.200
        self.play(LaggedStart(*[Create(a) for a in accel_arrows], lag_ratio=0.1, run_time=1.200))
        # Fill to end of line at 42.500 -> hold 3.300
        self.wait(3.300)   # scene = 42.500

        # ── "9.8 meters per second, every second." (42.833–45.367) ───────────
        # gap 0.333 -> scene = 42.833
        self.wait(0.333)
        # Acceleration label lands on this line (0.500 s) -> scene = 43.333
        self.play(FadeIn(accel_label), run_time=0.500)
        # Fill to end of line at 45.367 -> hold 2.034
        self.wait(2.034)   # scene = 45.367

        # ── "At the top of the throw, the ball's velocity is zero —" (45.433–48.033)
        # gap 0.067 -> scene = 45.433
        self.wait(0.067)
        # Screen holds — the peak ball is the visual anchor for this line
        self.wait(2.600)   # scene = 48.033

        # ── "but it is changing at 9.8 m/s² downward." (48.400–51.767) ──────
        # gap 0.367 -> scene = 48.400
        self.wait(0.367)
        # Screen holds — red arrow on the peak ball is the visual payoff
        self.wait(3.367)   # scene = 51.767

        # ── "That is a perfectly real acceleration." (52.333–54.600) ─────────
        # gap 0.567 -> scene = 52.333
        self.wait(0.567)
        self.wait(2.267)   # scene = 54.600

        # ── "Zero velocity and zero acceleration are not the same thing." (54.833–58.933)
        # gap 0.233 -> scene = 54.833
        self.wait(0.233)
        # Hold for 2.000 s into the line, then fade the arc out (0.800 s),
        # then hold for the remaining 1.300 s of the line.
        self.wait(2.000)   # scene = 56.833
        self.play(
            FadeOut(balls), FadeOut(path),
            FadeOut(accel_arrows), FadeOut(accel_label),
            run_time=0.800
        )                  # scene = 57.633
        self.wait(1.300)   # scene = 58.933
        # Hand off to fma_equation

    # ─────────────────────────────────────────────────────────────────────────
    # METHOD 3 · fma_equation
    # Entry scene_t ≈ 58.933   Exit scene_t ≈ 98.733
    # ─────────────────────────────────────────────────────────────────────────
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

        # ── "So what's causing that acceleration? A force." (59.267–63.833) ──
        # Blank screen during this line (cut to on-camera if desired).
        # gap 0.334 -> scene = 59.267
        self.wait(0.334)
        self.wait(4.567)   # scene = 63.834

        # ── "Gravity is pulling the ball downward the whole time…" (63.333–70.500)
        # Timestamps overlap with previous line by ~0.500 s; continue from 63.834.
        # Remaining time to end of line: 70.500 - 63.834 = 6.666 s
        # Blank screen continues (cut to on-camera if desired).
        self.wait(6.666)   # scene = 70.500

        # ── "And Newton gave us the exact relationship between force and acceleration:"
        # (70.900–75.033, gap 0.400)
        self.wait(0.400)   # scene = 70.900
        # F = ma fades in at the opening of this line (1.200 s)
        self.play(FadeIn(fma, scale=1.1), run_time=1.200)   # scene = 72.100
        # Fill to end of line at 75.033 -> hold 2.933
        self.wait(2.933)   # scene = 75.033

        # ── "Newton's Second Law: force equals mass times acceleration."
        # (75.700–80.333, dur 4.633 s, gap 0.667)
        self.wait(0.667)   # scene = 75.700
        #
        # Within the line, highlights land on the spoken word:
        #   "force"        ≈ 1.0 s into line  -> scene ≈ 76.700
        #   "mass"         ≈ 2.8 s into line  -> scene ≈ 78.500
        #   "acceleration" ≈ 4.0 s into line  -> scene ≈ 79.700
        #
        # Timing breakdown (must sum to 4.633 s):
        #   wait(1.000) + play(0.400) + wait(1.000) + play(0.400) + wait(0.800) + play(0.400) + wait(0.633)
        self.wait(1.000)
        self.play(fma[0].animate.set_color(YELLOW), FadeIn(f_label), run_time=0.400)
        # scene = 77.100
        self.wait(1.000)
        self.play(fma[2].animate.set_color(BLUE), FadeIn(m_label), run_time=0.400)
        # scene = 78.500
        self.wait(0.800)
        self.play(fma[3].animate.set_color(RED), FadeIn(a_label), run_time=0.400)
        # scene = 79.700
        self.wait(0.633)   # scene = 80.333

        # ── "If you know the force acting on an object and its mass…" (80.500–85.833)
        # gap 0.167 -> scene = 80.500
        self.wait(0.167)
        # All three labels visible — no new animation
        self.wait(5.333)   # scene = 85.833

        # ── "This is the bridge between the force of gravity…" (86.833–98.733)
        # gap 1.000 -> scene = 86.833
        self.wait(1.000)
        # Hold while Adam speaks (11.100 s), then fade F = ma out in the last 0.800 s
        self.wait(11.100)  # scene = 97.933
        self.play(
            fma[0].animate.set_color(WHITE),
            fma[2].animate.set_color(WHITE),
            fma[3].animate.set_color(WHITE),
            FadeOut(f_label), FadeOut(m_label), FadeOut(a_label),
            FadeOut(fma),
            run_time=0.800
        )                  # scene = 98.733