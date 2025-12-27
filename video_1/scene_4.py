"""
Scene 4: Solving the Mystery (2:30-3:45)

This is the KEY scene where we show why all objects fall at the same rate
through the mass cancellation in F = ma and F = GMm/r².

From PDF transcript lines 126-181.
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


class Scene4(Scene):
    """
    Scene 4: Solving the Mystery
    
    Shows why heavy and light objects fall at the same rate:
    - F = GMm/r² (gravity pulls harder on heavier objects)
    - F = ma (heavier objects are harder to accelerate)
    - Mass cancels out! a = GM/r²
    
    Duration: 2:30-3:45 (75 seconds)
    From PDF lines 126-181
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Add persistent logo
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)
        
        # PART 1: Restate the question (lines 129-134)
        self.restate_question()
        
        # PART 2: Show F = ma (lines 141-153)
        self.wait(2.0)
        self.introduce_fma()
        
        # PART 3: The mass cancellation (lines 154-169) - THE KEY MOMENT
        self.wait(2.0)
        self.mass_cancellation()
        
        # PART 4: Feather and hammer on Moon (lines 170-175)
        self.wait(2.0)
        self.moon_demo()
        
        # PART 5: Interactive question (lines 177-187)
        self.wait(2.0)
        self.interactive_question()
        
        # Hold final frame
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def restate_question(self):
        """
        Part 1: Restate the original question
        Lines 129-134: "Why do these two balls fall at the same rate? 
        Earth pulls harder on the basketball because it has more mass. So shouldn't it fall faster?"
        """
        # Show question
        question = StyledText("Why do they fall at the same rate?")
        question.scale(0.8)
        question.to_edge(UP, buff=0.5)
        
        self.play(Write(question, run_time=1.5))
        self.wait(0.5)
        
        # Show basketball and tennis ball
        basketball = create_ball(radius=0.35, color=ORANGE)
        basketball.shift(LEFT * 2 + DOWN * 0.5)
        
        tennis_ball = create_ball(radius=0.2, color=GREEN)
        tennis_ball.shift(RIGHT * 2 + DOWN * 0.5)
        
        # Labels
        bb_label = StyledText("Basketball (heavy)")
        bb_label.scale(0.5)
        bb_label.next_to(basketball, DOWN, buff=0.3)
        
        tb_label = StyledText("Tennis ball (light)")
        tb_label.scale(0.5)
        tb_label.next_to(tennis_ball, DOWN, buff=0.3)
        
        self.play(
            FadeIn(basketball, scale=0.5),
            FadeIn(tennis_ball, scale=0.5),
            FadeIn(bb_label),
            FadeIn(tb_label)
        )
        self.wait(1.5)
        
        # Clean up
        self.play(
            *[FadeOut(mob) for mob in [question, basketball, tennis_ball, bb_label, tb_label]],
            run_time=0.8
        )
    
    def introduce_fma(self):
        """
        Part 2: Introduce F = ma and explain the basketball
        Lines 141-153: Show that basketball is pulled harder BUT is also harder to accelerate
        """
        # Show F = ma equation
        title = StyledText("Newton's Second Law")
        title.scale(0.7)
        title.to_edge(UP, buff=0.3)
        
        fma_eq = MathTex("F = ma", font_size=72)
        fma_eq.next_to(title, DOWN, buff=0.5)
        
        self.play(
            FadeIn(title),
            Write(fma_eq, run_time=1.2)
        )
        self.wait(3)
        
        # Show basketball
        basketball = create_ball(radius=0.5, color=ORANGE)
        basketball.shift(DOWN * 0.5)
        
        ball_label = MathTex("m_{ball}", font_size=42)
        ball_label.next_to(basketball, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(basketball, scale=0.5),
            FadeIn(ball_label)
        )
        self.wait(0.5)
        
        # Simple arrow pointing down (gravity)
        force_arrow = Arrow(
            basketball.get_center(),
            basketball.get_bottom() + DOWN * 0.5,
            color=YELLOW,
            stroke_width=8,
            buff=0
        )
        force_label = MathTex("F_{gravity}", font_size=36, color=YELLOW)
        force_label.next_to(force_arrow, LEFT, buff=0.3)
        
        self.play(
            Create(force_arrow),
            FadeIn(force_label)
        )

        self.wait(1.0)
        
        # Text: "Earth pulls harder on heavier objects"
        text1 = StyledText("Bigger mass → Bigger force")
        text1.scale(0.6)
        text1.next_to(basketball, DOWN, buff=1.2)
        text1.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(text1))
        self.wait(2.5)
        
        # BUT... harder to accelerate
        text2 = StyledText("BUT... also harder to accelerate!")
        text2.scale(0.6)
        text2.next_to(text1, DOWN, buff=0.3)
        text2.set_color(RED)
        
        self.play(FadeIn(text2))
        self.wait(1.5)
        
        # Clean up for next part
        self.play(
            *[FadeOut(mob) for mob in [
                title, fma_eq, basketball, ball_label, 
                force_arrow, force_label, text1, text2
            ]],
            run_time=0.8
        )
    
    def mass_cancellation(self):
        """
        Part 3: THE KEY MOMENT - Mass cancellation with manual equation composition
        Lines 154-169: Show both equations and cancel the mass
        """
        # Title
        title = StyledText("The Beautiful Truth")
        title.scale(0.8)
        title.to_edge(UP, buff=0.3)
        title.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(title))
        self.wait(0.5)
        
        # Manually create first equation: F = G * M_Earth * m / r^2
        f1 = MathTex("F", font_size=56)
        eq1 = MathTex("=", font_size=56)
        g1 = MathTex("G", font_size=56)
        
        # Fraction for first equation
        numerator1 = MathTex("M_{Earth} \\cdot m", font_size=42)
        frac_line1 = Line(LEFT * 0.8, RIGHT * 0.8, color=WHITE, stroke_width=2)
        denominator1 = MathTex("r^2", font_size=42)
        
        # Position fraction
        numerator1.shift(UP * 1.2 + LEFT * 1)
        frac_line1.next_to(numerator1, DOWN, buff=0.15)
        denominator1.next_to(frac_line1, DOWN, buff=0.15)
        
        fraction1 = VGroup(numerator1, frac_line1, denominator1)
        
        # Position left side
        f1.shift(UP * 1.2 + LEFT * 3.5)
        eq1.next_to(f1, RIGHT, buff=0.3)
        g1.next_to(eq1, RIGHT, buff=0.3)
        fraction1.next_to(g1, RIGHT, buff=0.3)
        
        gravity_eq = VGroup(f1, eq1, g1, fraction1)
        gravity_eq.move_to(UP * 1.2 + LEFT * 2.5)
        
        # Manually create second equation: F = m * a
        f2 = MathTex("F", font_size=56)
        eq2 = MathTex("=", font_size=56)
        m2 = MathTex("m", font_size=56)
        a2 = MathTex("a", font_size=56)
        
        f2.shift(UP * 1.2 + RIGHT * 1.5)
        eq2.next_to(f2, RIGHT, buff=0.3)
        m2.next_to(eq2, RIGHT, buff=0.3)
        a2.next_to(m2, RIGHT, buff=0.3)
        
        newton_eq = VGroup(f2, eq2, m2, a2)
        newton_eq.move_to(UP * 1.2 + RIGHT * 2.5)
        
        # Labels
        eq1_label = StyledText("Gravity")
        eq1_label.scale(0.5)
        eq1_label.next_to(gravity_eq, DOWN, buff=0.3)
        
        eq2_label = StyledText("Newton's 2nd Law")
        eq2_label.scale(0.5)
        eq2_label.next_to(newton_eq, DOWN, buff=0.3)
        
        self.play(
            FadeIn(gravity_eq),
            FadeIn(newton_eq),
            run_time=1.5
        )
        self.play(
            FadeIn(eq1_label),
            FadeIn(eq2_label)
        )
        self.wait(1)
        
        # Lines 157-158: Set them equal - manually compose combined equation
        g_comb = MathTex("G", font_size=64)
        
        # Combined fraction numerator with both M_Earth and m
        num_comb = MathTex("M_{Earth} \\cdot m", font_size=48)
        frac_line_comb = Line(LEFT * 0.9, RIGHT * 0.9, color=WHITE, stroke_width=2)
        denom_comb = MathTex("r^2", font_size=48)
        
        # Position combined fraction
        frac_line_comb.move_to(ORIGIN + UP * 0.3)
        num_comb.next_to(frac_line_comb, UP, buff=0.15)
        denom_comb.next_to(frac_line_comb, DOWN, buff=0.15)
        
        fraction_comb = VGroup(num_comb, frac_line_comb, denom_comb)
        
        # Position left side
        g_comb.move_to(LEFT * 1.5 + UP * 0.3)
        fraction_comb.next_to(g_comb, RIGHT, buff=0.3)
        
        # Right side: = m * a
        eq_comb = MathTex("=", font_size=64)
        m_comb = MathTex("m", font_size=64)
        a_comb = MathTex("a", font_size=64)
        
        eq_comb.next_to(fraction_comb, RIGHT, buff=0.4)
        m_comb.next_to(eq_comb, RIGHT, buff=0.3)
        a_comb.next_to(m_comb, RIGHT, buff=0.3)
        
        combined = VGroup(g_comb, fraction_comb, eq_comb, m_comb, a_comb)
        combined.move_to(ORIGIN + UP * 0.3)
        
        self.play(
            FadeOut(eq1_label),
            FadeOut(eq2_label),
            TransformFromCopy(gravity_eq, VGroup(g_comb, fraction_comb)),
            TransformFromCopy(newton_eq, VGroup(eq_comb, m_comb, a_comb)),
            FadeOut(gravity_eq),
            FadeOut(newton_eq),
            run_time=1.5
        )
        self.wait(1)
        
        # Lines 159-160: Highlight the m on both sides
        highlight_text = StyledText("Notice: m appears on BOTH sides!")
        highlight_text.scale(0.6)
        highlight_text.next_to(combined, DOWN, buff=0.8)
        highlight_text.set_color(YELLOW)
        
        self.play(FadeIn(highlight_text))
        
        # Create boxes around BOTH m's
        # The m in the numerator is part of num_comb
        # We need to extract just the "m" part - it's the last character
        m_in_numerator_box = SurroundingRectangle(
            num_comb[0][-1:],  # Last character of M_Earth · m
            color=RED,
            stroke_width=3,
            buff=0.08
        )
        
        m_on_right_box = SurroundingRectangle(
            m_comb,
            color=RED,
            stroke_width=3,
            buff=0.08
        )
        
        self.play(
            Create(m_in_numerator_box),
            Create(m_on_right_box),
            run_time=0.8
        )
        self.wait(1)
        
        # Lines 159-160: Show them canceling
        cancel_text = StyledText("They CANCEL OUT!")
        cancel_text.scale(0.7)
        cancel_text.next_to(combined, DOWN, buff=0.8)
        cancel_text.set_color(ACCENT_COLOR)
        
        self.play(
            FadeOut(highlight_text),
            FadeIn(cancel_text)
        )
        
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
        
        self.play(
            Create(cross1),
            Create(cross2),
            run_time=1
        )
        self.wait(1)
        
        # Lines 164-165: Show final result - manually compose
        a_final = MathTex("a", font_size=72)
        eq_final = MathTex("=", font_size=72)
        g_final = MathTex("G", font_size=72)
        
        # Final fraction (without m)
        num_final = MathTex("M_{Earth}", font_size=54)
        frac_line_final = Line(LEFT * 0.7, RIGHT * 0.7, color=WHITE, stroke_width=2)
        denom_final = MathTex("r^2", font_size=54)
        
        # Position final fraction
        frac_line_final.move_to(DOWN * 0.5)
        num_final.next_to(frac_line_final, UP, buff=0.15)
        denom_final.next_to(frac_line_final, DOWN, buff=0.15)
        
        fraction_final = VGroup(num_final, frac_line_final, denom_final)
        
        # Position left side
        a_final.move_to(LEFT * 2 + DOWN * 0.5)
        eq_final.next_to(a_final, RIGHT, buff=0.3)
        g_final.next_to(eq_final, RIGHT, buff=0.3)
        fraction_final.next_to(g_final, RIGHT, buff=0.3)
        
        final = VGroup(a_final, eq_final, g_final, fraction_final)
        final.move_to(DOWN * 0.5)
        
        self.play(
            FadeOut(combined),
            FadeOut(m_in_numerator_box),
            FadeOut(m_on_right_box),
            FadeOut(cross1),
            FadeOut(cross2),
            FadeOut(cancel_text),
            run_time=0.8
        )
        
        self.play(Write(final, run_time=1.5))
        self.wait(0.5)
        
        # Lines 167-169: Show that m is missing
        no_m_text = StyledText("No m! Acceleration is the SAME for all objects!")
        no_m_text.scale(0.65)
        no_m_text.next_to(final, DOWN, buff=0.5)
        no_m_text.set_color(ACCENT_COLOR)
        
        # Circle where m would be
        circle = Circle(
            radius=0.3,
            color=YELLOW,
            stroke_width=3
        )
        circle.move_to(a_final.get_left() + LEFT * 0.5)
        
        question_mark = Text("m?", font_size=36, color=YELLOW)
        question_mark.move_to(circle)
        
        cross = VGroup(
            Line(circle.get_top(), circle.get_bottom(), color=RED, stroke_width=4),
            Line(circle.get_left(), circle.get_right(), color=RED, stroke_width=4)
        )
        
        self.play(
            Create(circle),
            FadeIn(question_mark)
        )
        self.play(Create(cross))
        self.play(FadeIn(no_m_text))
        self.wait(2)
        
        # Clean up
        self.play(
            *[FadeOut(mob) for mob in [title, final, no_m_text, circle, question_mark, cross]],
            run_time=0.8
        )
    
    def moon_demo(self):
        """
        Part 4: Feather and hammer on Moon
        Lines 170-175: Show famous footage reference
        """
        # Title
        title = StyledText("Apollo 15: Hammer & Feather")
        title.scale(0.7)
        title.to_edge(UP, buff=0.5)
        
        self.play(FadeIn(title))
        
        # Create Moon surface
        moon_surface = Line(
            LEFT * 6,
            RIGHT * 6,
            color=GREY,
            stroke_width=4
        )
        moon_surface.shift(DOWN * 2.5)
        
        # Feather
        feather = Polygon(
            [0, 0.6, 0],
            [0.1, 0.5, 0],
            [0, 0, 0],
            [-0.1, 0.5, 0],
            fill_color=WHITE,
            fill_opacity=0.8,
            stroke_color=WHITE
        )
        feather.shift(LEFT * 2 + UP * 1.5)
        
        feather_label = StyledText("Feather")
        feather_label.scale(0.5)
        feather_label.next_to(feather, UP, buff=0.2)
        
        # Hammer
        hammer_head = Rectangle(
            width=0.4,
            height=0.2,
            fill_color=GREY,
            fill_opacity=0.8,
            stroke_color=WHITE
        )
        hammer_handle = Rectangle(
            width=0.1,
            height=0.6,
            fill_color=GREY_BROWN,
            fill_opacity=0.8,
            stroke_color=WHITE
        )
        hammer_handle.next_to(hammer_head, DOWN, buff=0)
        hammer = VGroup(hammer_head, hammer_handle)
        hammer.shift(RIGHT * 2 + UP * 1.5)
        
        hammer_label = StyledText("Hammer")
        hammer_label.scale(0.5)
        hammer_label.next_to(hammer, UP, buff=0.2)
        
        self.play(
            Create(moon_surface),
            FadeIn(feather),
            FadeIn(hammer),
            FadeIn(feather_label),
            FadeIn(hammer_label)
        )
        self.wait(0.5)
        
        # Both fall at same rate
        subtitle = StyledText("No air resistance → Same acceleration!")
        subtitle.scale(0.6)
        subtitle.to_edge(DOWN, buff=1)
        subtitle.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(subtitle))
        
        self.play(
            feather.animate.shift(DOWN * 3.7),
            hammer.animate.shift(DOWN * 3.7),
            feather_label.animate.shift(DOWN * 3.7),
            hammer_label.animate.shift(DOWN * 3.7),
            run_time=2,
            rate_func=rate_functions.ease_in_quad
        )
        self.wait(1.5)
        
        # Clean up
        self.play(
            *[FadeOut(mob) for mob in [
                title, moon_surface, feather, hammer,
                feather_label, hammer_label, subtitle
            ]],
            run_time=0.8
        )
    
    def interactive_question(self):
        """
        Part 5: Interactive question
        Lines 177-187: Test understanding with a question about 2× Earth's mass
        """
        # Question
        question = StyledText("Test Your Understanding:")
        question.scale(0.8)
        question.to_edge(UP, buff=0.5)
        question.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(question))
        
        question_text = StyledText(
            "On a planet with 2× Earth's mass,\nwould objects fall faster, slower, or the same?"
        )
        question_text.scale(0.65)
        question_text.next_to(question, DOWN, buff=0.5)
        
        self.play(Write(question_text, run_time=2))
        
        # Pause for thinking (lines 181: "Pause for 3-4 seconds")
        thinking = StyledText("Think about it...")
        thinking.scale(0.5)
        thinking.to_edge(DOWN, buff=1)
        thinking.set_color(YELLOW)
        
        self.play(FadeIn(thinking))
        self.wait(3)
        self.play(FadeOut(thinking))
        
        # Show answer (lines 182-187)
        answer_title = StyledText("Answer:")
        answer_title.scale(0.7)
        answer_title.shift(DOWN * 0.5)
        answer_title.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(answer_title))
        
        # Manually create equation with 2M_Earth
        a_ans = MathTex("a", font_size=56)
        eq_ans = MathTex("=", font_size=56)
        g_ans = MathTex("G", font_size=56)
        
        # Fraction with 2M_Earth
        num_ans = MathTex("2M_{Earth}", font_size=42)
        frac_line_ans = Line(LEFT * 0.7, RIGHT * 0.7, color=WHITE, stroke_width=2)
        denom_ans = MathTex("r^2", font_size=42)
        
        # Position fraction
        frac_line_ans.move_to(DOWN * 1.2)
        num_ans.next_to(frac_line_ans, UP, buff=0.15)
        denom_ans.next_to(frac_line_ans, DOWN, buff=0.15)
        
        fraction_ans = VGroup(num_ans, frac_line_ans, denom_ans)
        
        # Position left side
        a_ans.move_to(LEFT * 1.8 + DOWN * 1.2)
        eq_ans.next_to(a_ans, RIGHT, buff=0.3)
        g_ans.next_to(eq_ans, RIGHT, buff=0.3)
        fraction_ans.next_to(g_ans, RIGHT, buff=0.3)
        
        equation = VGroup(a_ans, eq_ans, g_ans, fraction_ans)
        equation.move_to(DOWN * 1.2)
        
        self.play(Write(equation))
        
        # Highlight 2M
        self.play(num_ans.animate.set_color(ACCENT_COLOR), run_time=0.5)
        
        # Arrow showing increase
        arrow_up = Arrow(
            num_ans.get_bottom(),
            num_ans.get_bottom() + DOWN * 0.5,
            color=GREEN,
            stroke_width=4
        )
        arrow_label = StyledText("Bigger!")
        arrow_label.scale(0.5)
        arrow_label.next_to(arrow_up, DOWN, buff=0.1)
        arrow_label.set_color(GREEN)
        
        self.play(
            Create(arrow_up),
            FadeIn(arrow_label)
        )
        
        # Final answer text
        final_answer = StyledText("Objects would fall FASTER!")
        final_answer.scale(0.7)
        final_answer.to_edge(DOWN, buff=0.8)
        final_answer.set_color(GREEN)
        
        self.play(FadeIn(final_answer))
        self.wait(2)
        
        # Clean up (will be faded by main construct)