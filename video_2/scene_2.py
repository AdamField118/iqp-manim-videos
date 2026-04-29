"""
Scene 2: What Acceleration Actually Is (0:50--2:20)

Transcript Manim tags:
- Number line for velocity (left=downward, right=upward), dot at zero
- Ball velocity at several heights: +15, +8, 0, -8, -15 m/s with arrows
- Small equal downward delta-v arrows between each snapshot, labeled "Delta v, always downward"
- Single steady downward arrow: "acceleration = 9.8 m/s^2 downward" across all positions
- F = ma fades in, labeled: F=net force, m=mass, a=acceleration produced
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

        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def velocity_number_line(self):
        """
        A dot moves along the number line as the ball rises and falls,
        making concrete that velocity is a continuous quantity passing
        through zero rather than stopping there.
        """
        # Number line on the right half of the screen
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

        # Ball on the left half of the screen
        ball = Circle(radius=0.22, fill_color=GREEN, fill_opacity=0.85,
                      stroke_color=WHITE, stroke_width=2)
        ball.move_to([-3.2, -1.2, 0])

        # Dot starts at +15 on the number line
        dot = Dot(nl.n2p(15), color=BLUE, radius=0.15)

        phase1 = StyledText("thrown upward: v = +15 m/s")
        phase1.scale(0.45).set_color(BLUE).next_to(nl, UP, buff=0.5)

        self.play(Create(nl), FadeIn(axis_title), FadeIn(down_label), FadeIn(up_label))
        self.play(FadeIn(ball), FadeIn(dot), FadeIn(phase1))
        self.wait(0.5)

        # Ball rises, dot slides toward zero (both slow down together)
        self.play(
            ball.animate.shift(UP * 2.4),
            dot.animate.move_to(nl.n2p(0)),
            FadeOut(phase1),
            run_time=2.5, rate_func=rate_functions.ease_out_sine
        )

        phase2 = StyledText("at peak: v = 0, but still accelerating downward")
        phase2.scale(0.45).set_color(YELLOW).next_to(nl, UP, buff=0.5)
        self.play(FadeIn(phase2))
        self.wait(1.2)

        # Ball falls, dot slides to -15 (both speed up together)
        self.play(
            ball.animate.shift(DOWN * 2.4),
            dot.animate.move_to(nl.n2p(-15)),
            FadeOut(phase2),
            run_time=2.5, rate_func=rate_functions.ease_in_sine
        )

        phase3 = StyledText("now falling: v = -15 m/s (downward)")
        phase3.scale(0.45).set_color(RED).next_to(nl, UP, buff=0.5)
        self.play(FadeIn(phase3))
        self.wait(2)

        self.play(
            FadeOut(nl), FadeOut(axis_title), FadeOut(down_label), FadeOut(up_label),
            FadeOut(ball), FadeOut(dot), FadeOut(phase3),
            run_time=0.8
        )

    def ball_velocity_snapshots(self):
        """
        Five snapshots of the ball arranged in a parabolic arc across the
        screen, making clear these are moments along a single trajectory.
        Velocity arrows leave from the ball's surface.
        Acceleration arrows (equal length, downward) come from each center.
        """
        # Parabolic arc: sides are lowest, peak is highest.
        positions   = [(-3.0, -0.8), (-1.5, 0.8), (0.0, 1.5), (1.5, 0.8), (3.0, -0.8)]
        velocities  = [15, 8, 0, -8, -15]
        vel_labels  = ["+15 m/s", "+8 m/s", "0 m/s", "-8 m/s", "-15 m/s"]
        label_dirs  = [LEFT, LEFT, UP, RIGHT, RIGHT]
        ball_radius = 0.2

        balls = VGroup()
        for (x, y) in positions:
            b = Circle(radius=ball_radius,
                       fill_color=GREEN, fill_opacity=0.85,
                       stroke_color=WHITE, stroke_width=2)
            b.move_to([x, y, 0])
            balls.add(b)

        # Dashed path to emphasise the arc trajectory
        path = VMobject(stroke_color=WHITE, stroke_width=1.5, stroke_opacity=0.45)
        path.set_points_smoothly([np.array([x, y, 0]) for (x, y) in positions])

        self.play(Create(path), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(b) for b in balls], lag_ratio=0.2, run_time=1.5))

        # Velocity arrows: from surface, scaled to speed
        vel_arrows = VGroup()
        vel_texts  = VGroup()

        for ball, v, lbl, ldir in zip(balls, velocities, vel_labels, label_dirs):
            if v > 0:
                arrow_len = v / 15 * 1.2
                arrow = Arrow(
                    ball.get_top(),
                    ball.get_top() + UP * arrow_len,
                    color=BLUE, stroke_width=5, buff=0,
                    max_tip_length_to_length_ratio=0.2
                )
            elif v < 0:
                arrow_len = abs(v) / 15 * 1.2
                arrow = Arrow(
                    ball.get_bottom(),
                    ball.get_bottom() + DOWN * arrow_len,
                    color=BLUE, stroke_width=5, buff=0,
                    max_tip_length_to_length_ratio=0.2
                )
            else:
                # Zero velocity: dot at surface
                arrow = Dot(ball.get_top(), color=BLUE, radius=0.06)
            vel_arrows.add(arrow)

            buff = 0.45 if ldir is UP else 0.25
            text = StyledText(lbl).scale(0.4).next_to(ball, ldir, buff=buff)
            vel_texts.add(text)

        self.play(
            LaggedStart(*[Create(a) for a in vel_arrows], lag_ratio=0.15, run_time=1.5),
            LaggedStart(*[FadeIn(t) for t in vel_texts], lag_ratio=0.15, run_time=1.5),
        )
        self.wait(2)

        # Delta-v arrows: one between each consecutive pair of balls,
        # offset slightly toward the outside of the arc to avoid overlap.
        dv_arrows  = VGroup()
        x_offsets  = [-0.3, -0.3, 0.3, 0.3]

        for i in range(len(positions) - 1):
            x0, y0 = positions[i]
            x1, y1 = positions[i + 1]
            mx = (x0 + x1) / 2 + x_offsets[i]
            my = (y0 + y1) / 2
            dv = Arrow(
                [mx, my + 0.22, 0],
                [mx, my - 0.22, 0],
                color=YELLOW, stroke_width=4, buff=0,
                max_tip_length_to_length_ratio=0.4
            )
            dv_arrows.add(dv)

        dv_label = MathTex(
            r"\Delta v\text{: always downward}",
            font_size=34, color=YELLOW
        )
        dv_label.to_edge(DOWN, buff=0.8)

        self.play(
            LaggedStart(*[Create(dv) for dv in dv_arrows], lag_ratio=0.2, run_time=1.5),
            FadeIn(dv_label)
        )
        self.wait(2)

        # Consolidate: replace with equal-length acceleration arrows from each center
        self.play(
            FadeOut(vel_arrows), FadeOut(vel_texts),
            FadeOut(dv_arrows), FadeOut(dv_label)
        )

        accel_arrows = VGroup()
        for ball in balls:
            a = Arrow(
                ball.get_center(),
                ball.get_center() + DOWN * 1.0,
                color=RED, stroke_width=6, buff=0,
                max_tip_length_to_length_ratio=0.25
            )
            accel_arrows.add(a)

        accel_label = MathTex(
            r"\text{acceleration} = 9.8\;\text{m/s}^2\;\text{downward}",
            font_size=34, color=RED
        )
        accel_label.to_edge(DOWN, buff=0.8)

        self.play(
            LaggedStart(*[Create(a) for a in accel_arrows], lag_ratio=0.1, run_time=1.2),
            FadeIn(accel_label)
        )
        self.wait(3)

        self.play(
            FadeOut(balls), FadeOut(path),
            FadeOut(accel_arrows), FadeOut(accel_label),
            run_time=0.8
        )

    def fma_equation(self):
        """
        F = ma: each letter highlighted by color, matching the Video 1 style.
        Split into separate substrings so each letter has a stable index.
        [0]=F  [1]==  [2]=m  [3]=a
        """
        fma = MathTex("F", "=", "m", "a", font_size=96)
        fma.move_to(ORIGIN)

        self.play(FadeIn(fma, scale=1.1), run_time=1.2)
        self.wait(0.5)

        f_label = StyledText("net force")
        f_label.scale(0.5).set_color(YELLOW)
        f_label.next_to(fma, UP, buff=0.3).shift(LEFT * 1.3)

        m_label = StyledText("mass of object")
        m_label.scale(0.5).set_color(BLUE)
        m_label.next_to(fma, DOWN, buff=0.25).shift(RIGHT * 0.8)

        a_label = StyledText("acceleration produced")
        a_label.scale(0.5).set_color(RED)
        a_label.next_to(fma, UP, buff=0.05).shift(RIGHT * 1.55)

        # Reveal one at a time with color highlights
        self.play(fma[0].animate.set_color(YELLOW), FadeIn(f_label))
        self.wait(0.8)
        self.play(fma[2].animate.set_color(BLUE), FadeIn(m_label))
        self.wait(0.8)
        self.play(fma[3].animate.set_color(RED), FadeIn(a_label))
        self.wait(2)

        self.play(
            fma[0].animate.set_color(WHITE),
            fma[2].animate.set_color(WHITE),
            fma[3].animate.set_color(WHITE),
            FadeOut(f_label), FadeOut(m_label), FadeOut(a_label),
            FadeOut(fma),
            run_time=0.8
        )