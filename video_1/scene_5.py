"""
Scene 5: Wrapping Up (3:45-4:30)

This scene reviews the key concepts learned and previews the next video
on projectile motion.

From PDF transcript lines 188-218.
"""

import sys
sys.path.append('..')

from manim import *
from utils.transitions import (
    fade_in_from_bottom,
    fade_in_with_scale,
    staggered_fade_in
)
from utils.objects import (
    StyledText,
    StyledTitle,
    create_logo,
    BACKGROUND_COLOR,
    ACCENT_COLOR,
    TEXT_COLOR,
    PRIMARY_COLOR
)
from utils.physics_objects import (
    create_mass,
    create_earth,
    create_ball,
    create_fbd_force_arrows
)


class Scene5(Scene):
    """
    Scene 5: Wrapping Up
    
    Reviews key concepts:
    - Gravity is universal
    - Depends on mass and distance
    - All objects fall at same rate
    
    Previews next video on projectile motion.
    
    Duration: 3:45-4:30 (45 seconds)
    From PDF lines 188-218
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Add persistent logo
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)
        
        # PART 1: Review title (lines 192)
        self.review_title()
        self.wait(2)
        
        # PART 2: Key points (lines 193-206)
        self.key_points()
        self.wait(2)
        
        # PART 3: Final demonstration (lines 207-209)
        self.final_demo()
        self.wait(2)
        
        # PART 4: Preview next video (lines 210-213)
        self.preview_next()
        self.wait(2)
        
        # PART 5: End card (lines 214-218)
        self.end_card()
        
        # Hold final frame
        self.wait(3)
    
    def review_title(self):
        """
        Part 1: Review title
        Lines 192: "Let's review what we've learned today"
        """
        title = StyledTitle("What We Learned")
        title.scale(0.7)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title, run_time=1.2))
        self.wait(0.5)
        
        # Keep title for next part
        self.title = title
    
    def key_points(self):
        """
        Part 2: Show key points with icons
        Lines 193-206: Show three main concepts
        """
        # Point 1: Gravity is universal (lines 195-197)
        icon1_circle1 = Circle(radius=0.2, color=BLUE, fill_opacity=0.5)
        icon1_circle2 = Circle(radius=0.15, color=RED, fill_opacity=0.5).shift(RIGHT * 0.5 + UP * 0.3)
        icon1 = VGroup(
            Circle(radius=0.2, color=BLUE, fill_opacity=0.5),
            Circle(radius=0.15, color=RED, fill_opacity=0.5).shift(RIGHT * 0.5 + UP * 0.3),
            create_fbd_force_arrows(
                icon1_circle1,
                icon1_circle2,
                arrow_length=0.25,
                color=YELLOW,
                stroke_width=4
            )
        )
        icon1.shift(LEFT * 4 + UP * 0.8)
        
        text1 = StyledText("Gravity is a universal\nforce of attraction")
        text1.scale(0.5)
        text1.next_to(icon1, RIGHT, buff=0.5)
        
        point1 = VGroup(icon1, text1)
        
        # Point 2: Depends on mass and distance (lines 198-199)
        icon2 = MathTex("F \\propto \\frac{m_1 m_2}{r^2}", font_size=36, color=ACCENT_COLOR)
        icon2.shift(LEFT * 4 + DOWN * 0.3)
        
        text2 = StyledText("Depends on masses\nand distance")
        text2.scale(0.5)
        text2.next_to(icon2, RIGHT, buff=0.5)
        
        point2 = VGroup(icon2, text2)
        
        # Point 3: All objects fall at same rate (lines 202-206)
        icon3_ball1 = create_ball(radius=0.15, color=ORANGE, pattern=False)
        icon3_ball2 = create_ball(radius=0.1, color=GREEN, pattern=False)
        icon3_ball1.shift(LEFT * 0.2)
        icon3_ball2.shift(RIGHT * 0.2)
        icon3_arrow = Arrow(UP * 0.3, DOWN * 0.3, color=YELLOW, stroke_width=3, buff=0)
        icon3 = VGroup(icon3_ball1, icon3_ball2, icon3_arrow)
        icon3.shift(LEFT * 4 + DOWN * 1.4)
        
        text3 = StyledText("All objects fall at\nthe SAME rate!")
        text3.scale(0.5)
        text3.next_to(icon3, RIGHT, buff=0.5)
        text3.set_color(ACCENT_COLOR)
        
        point3 = VGroup(icon3, text3)
        
        # Animate all points appearing
        self.play(
            LaggedStart(
                FadeIn(point1, shift=RIGHT * 0.3),
                FadeIn(point2, shift=RIGHT * 0.3),
                FadeIn(point3, shift=RIGHT * 0.3),
                lag_ratio=0.5,
                run_time=3
            )
        )
        self.wait(2)
        
        # Clean up for next part
        self.play(
            FadeOut(self.title),
            FadeOut(point1),
            FadeOut(point2),
            FadeOut(point3),
            run_time=0.8
        )
    
    def final_demo(self):
        """
        Part 3: Quick replay of mass cancellation
        Lines 200-201: "Show the cancellation animation again briefly"
        """
        # Title
        title = StyledText("The Key Insight:")
        title.scale(0.7)
        title.to_edge(UP, buff=0.5)
        title.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(title))
        
        # Manually compose equation: G * M_Earth * m / r^2 = m * a
        g_part = MathTex("G", font_size=64)
        
        # Left fraction
        numerator_left = MathTex("M_{Earth} \\cdot m", font_size=48)
        frac_line_left = Line(LEFT * 1.0, RIGHT * 1.0, color=WHITE, stroke_width=2)
        denominator_left = MathTex("r^2", font_size=48)
        
        # Position left fraction
        frac_line_left.move_to(UP * 0.5)
        numerator_left.next_to(frac_line_left, UP, buff=0.15)
        denominator_left.next_to(frac_line_left, DOWN, buff=0.15)
        
        fraction_left = VGroup(numerator_left, frac_line_left, denominator_left)
        
        # Position left side
        g_part.move_to(LEFT * 2.5 + UP * 0.5)
        fraction_left.next_to(g_part, RIGHT, buff=0.3)
        
        # Right side: = m * a
        equals = MathTex("=", font_size=64)
        m_right = MathTex("m", font_size=64)
        a_right = MathTex("a", font_size=64)
        
        equals.next_to(fraction_left, RIGHT, buff=0.4)
        m_right.next_to(equals, RIGHT, buff=0.3)
        a_right.next_to(m_right, RIGHT, buff=0.3)
        
        equation = VGroup(g_part, fraction_left, equals, m_right, a_right)
        equation.move_to(UP * 0.5)
        
        self.play(Write(equation, run_time=1))
        
        # Create boxes around BOTH m's using SurroundingRectangle
        # The m in the numerator is the last character of "M_{Earth} \cdot m"
        m_in_numerator_box = SurroundingRectangle(
            numerator_left[0][-1:],  # Last character is the small m
            color=RED,
            stroke_width=3,
            buff=0.08
        )
        
        m_on_right_box = SurroundingRectangle(
            m_right,
            color=RED,
            stroke_width=3,
            buff=0.08
        )
        
        self.play(Create(m_in_numerator_box), Create(m_on_right_box), run_time=0.5)
        
        # Create X marks using the boxes
        cross1 = VGroup(
            Line(m_in_numerator_box.get_corner(DL), m_in_numerator_box.get_corner(UR), 
                color=RED, stroke_width=4),
            Line(m_in_numerator_box.get_corner(UL), m_in_numerator_box.get_corner(DR), 
                color=RED, stroke_width=4)
        )
        cross2 = VGroup(
            Line(m_on_right_box.get_corner(DL), m_on_right_box.get_corner(UR), 
                color=RED, stroke_width=4),
            Line(m_on_right_box.get_corner(UL), m_on_right_box.get_corner(DR), 
                color=RED, stroke_width=4)
        )
        
        self.play(Create(cross1), Create(cross2), run_time=0.6)
        self.wait(0.5)
        
        # Final result - manually compose
        a_final = MathTex("a", font_size=72, color=ACCENT_COLOR)
        eq_final = MathTex("=", font_size=72, color=ACCENT_COLOR)
        g_final = MathTex("G", font_size=72, color=ACCENT_COLOR)
        
        # Final fraction (without m)
        num_final = MathTex("M_{Earth}", font_size=54, color=ACCENT_COLOR)
        frac_line_final = Line(LEFT * 0.7, RIGHT * 0.7, color=ACCENT_COLOR, stroke_width=2)
        denom_final = MathTex("r^2", font_size=54, color=ACCENT_COLOR)
        
        # Position final fraction
        frac_line_final.move_to(DOWN * 1)
        num_final.next_to(frac_line_final, UP, buff=0.15)
        denom_final.next_to(frac_line_final, DOWN, buff=0.15)
        
        fraction_final = VGroup(num_final, frac_line_final, denom_final)
        
        # Position left side
        a_final.move_to(LEFT * 1.5 + DOWN * 1)
        eq_final.next_to(a_final, RIGHT, buff=0.3)
        g_final.next_to(eq_final, RIGHT, buff=0.3)
        fraction_final.next_to(g_final, RIGHT, buff=0.3)
        
        result = VGroup(a_final, eq_final, g_final, fraction_final)
        result.move_to(DOWN * 1)
        
        self.play(Write(result, run_time=1))
        
        # Text
        insight = StyledText("Mass cancels out!")
        insight.scale(0.6)
        insight.next_to(result, DOWN, buff=0.5)
        
        self.play(FadeIn(insight))
        self.wait(1.5)
        
        # Clean up
        self.play(
            *[FadeOut(mob) for mob in [title, equation, m_in_numerator_box, m_on_right_box, 
                                        cross1, cross2, result, insight]],
            run_time=0.8
        )
    
    def preview_next(self):
        """
        Part 4: Preview next video
        Lines 210-213: "In our next video, we'll explore what happens when we throw or 
        launch objects—and discover that projectile motion is just falling... with style."
        """
        # Title
        title = StyledText("Next Time...")
        title.scale(0.8)
        title.to_edge(UP, buff=0.5)
        title.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(title))
        
        # Show projectile arc (line 210)
        # Create a simple projectile trajectory
        start_point = LEFT * 3 + DOWN * 1
        
        # Parametric curve for parabola
        def projectile_path(t):
            x = -3 + 6 * t
            y = -1 + 4 * t - 5 * t * t
            return np.array([x, y, 0])
        
        trajectory = ParametricFunction(
            projectile_path,
            t_range=[0, 1],
            color=YELLOW,
            stroke_width=4
        )
        
        # Ball that follows trajectory
        ball = create_ball(radius=0.25, color=RED, pattern=False)
        ball.move_to(start_point)
        
        # Ground
        ground = Line(
            LEFT * 6, RIGHT * 6,
            color=GREY,
            stroke_width=3
        )
        ground.shift(DOWN * 2)
        
        self.play(
            Create(ground),
            FadeIn(ball)
        )
        
        # Animate trajectory
        self.play(
            Create(trajectory, run_time=2),
            MoveAlongPath(ball, trajectory, run_time=2, rate_func=linear)
        )
        
        # Text
        preview_text = StyledText("Projectile Motion:\nFalling... with style!")
        preview_text.scale(0.65)
        preview_text.next_to(trajectory, UP, buff=0.5)
        preview_text.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(preview_text))
        self.wait(1.5)
        
        # Clean up
        self.play(
            *[FadeOut(mob) for mob in [title, trajectory, ball, ground, preview_text]],
            run_time=0.8
        )
    
    def end_card(self):
        """
        Part 5: End card
        Lines 217-218: Fade to end card with channel/project info
        """
        # Large centered logo
        large_logo = create_logo(scale=0.4)
        large_logo.shift(UP * 1.2)
        
        # Project title
        project_title = StyledTitle("Short Video Projects")
        project_title.scale(0.6)
        project_title.next_to(large_logo, DOWN, buff=0.8)
        
        subtitle = StyledText("Physics Education Series")
        subtitle.scale(0.6)
        subtitle.next_to(project_title, DOWN, buff=0.3)
        
        # Thanks message
        thanks = StyledText("Thanks for watching!")
        thanks.scale(0.7)
        thanks.shift(DOWN * 1.8)
        thanks.set_color(ACCENT_COLOR)
        
        # Acknowledgments (lines 219-225)
        acknowledgment = StyledText("With guidance from Prof. Noviello & Prof. Kafle")
        acknowledgment.scale(0.4)
        acknowledgment.to_edge(DOWN, buff=0.5)
        acknowledgment.set_opacity(0.7)
        
        # Animate end card
        self.play(
            FadeIn(large_logo, scale=0.8, run_time=1.5)
        )
        self.play(
            Write(project_title, run_time=1),
            FadeIn(subtitle, shift=UP * 0.2)
        )
        self.wait(0.5)
        self.play(FadeIn(thanks))
        self.wait(0.8)
        self.play(FadeIn(acknowledgment))
        
        # Hold end card (will hold in main construct)