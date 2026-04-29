"""
Scene 3: Newton's Big Discovery (1:30-2:45)

This scene introduces Newton's Law of Universal Gravitation and explains
each component of the equation. Includes one interactive question.

From PDF transcript lines 74-131.
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
    create_force_arrow,
    create_fbd_force_arrows,
    create_ball
)


class Scene3(Scene):
    """
    Scene 3: Newton's Big Discovery

    Introduces Newton's Law of Universal Gravitation:
    F = G * m₁ * m₂ / r²

    Includes:
    - Explanation of each variable
    - Question 1: Inverse square law (doubling distance)

    Duration: 1:30-2:45 (75 seconds)
    From PDF lines 74-131
    """

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        """All scene animation logic. Called by construct() and importable by full_video.py."""

        # Add persistent logo
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        # PART 1: Introduce Newton and the law (lines 78-82)
        Scene3.introduce_newton(self)

        # PART 1b: Show complete vector formula briefly (lines 82-96)
        Scene3.show_vector_formula(self)

        # PART 2: Show and explain the magnitude equation (lines 96-99)
        Scene3.show_equation(self)

        # PART 3: Demonstrate the relationships (lines 100-105)
        Scene3.demonstrate_relationships(self)

        # PART 4: Question 1 - Inverse Square Law (lines 106-114)
        Scene3.question_1_inverse_square(self)

        # Hold final frame
        self.wait(2)

        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def introduce_newton(self):
        """
        Part 1: Introduce Newton and the law
        Lines 78-80: "In 1687, Isaac Newton figured out the exact rule for how gravity works."
        """
        title = StyledTitle("Newton's Law of Universal Gravitation")
        title.scale(0.6)
        title.to_edge(UP, buff=0.5)

        subtitle = StyledText("1687")
        subtitle.scale(0.7)
        subtitle.next_to(title, DOWN, buff=0.3)
        subtitle.set_color(ACCENT_COLOR)

        self.play(
            Write(title, run_time=1.5),
            FadeIn(subtitle, shift=UP * 0.2)
        )
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            run_time=0.8
        )

    def show_vector_formula(self):
        """
        Part 1b: Show the complete vector formula briefly before simplifying
        Lines 82-96:
          [MANIM: Vector equation fades in gracefully]
          F⃗ = -G (m₁m₂/r²) r̂
          Highlight negative sign and r̂, then show magnitude version below,
          then fade the vector form out leaving only the magnitude equation.
        """
        # Complete vector formula
        vec_formula = MathTex(
            r"\vec{F} = -G \frac{m_1 m_2}{r^2} \hat{r}",
            font_size=72
        )
        vec_formula.shift(UP * 0.8)

        self.play(FadeIn(vec_formula, scale=1.1), run_time=1.5)
        self.wait(5)

        # Lines 88-91: Highlight the negative sign and r̂
        neg_label = StyledText("Always attractive (pulls together)")
        neg_label.scale(0.55)
        neg_label.next_to(vec_formula, DOWN, buff=0.5)
        neg_label.set_color(YELLOW)

        self.play(
            vec_formula[0][3].animate.set_color(YELLOW),   # negative sign
            vec_formula[0][-2:].animate.set_color(YELLOW), # r̂
            FadeIn(neg_label),
            run_time=0.8
        )
        self.wait(14.0)

        # Lines 92-96: "For this video we focus on the magnitude"
        scope_text = StyledText("For this video: magnitude only")
        scope_text.scale(0.55)
        scope_text.set_color(ACCENT_COLOR)
        scope_text.next_to(vec_formula, DOWN, buff=0.5)

        mag_formula = MathTex(
            r"F = G \frac{m_1 m_2}{r^2}",
            font_size=72
        )
        mag_formula.next_to(scope_text, DOWN, buff=0.4)

        self.play(
            FadeOut(neg_label),
            FadeIn(scope_text),
            run_time=0.5
        )
        
        self.play(FadeIn(mag_formula, shift=UP * 0.2), run_time=1)
        self.wait(8.0)

        # Fade out vector form and scope text, leaving clean screen for show_equation
        self.play(
            FadeOut(vec_formula),
            FadeOut(scope_text),
            FadeOut(mag_formula),
            run_time=1
        )

    def show_equation(self):
        """
        Part 2: Show and explain the equation
        Lines 82-99: Show F = G m₁m₂/r² and explain each variable
        """
        f_part = MathTex("F", font_size=72)
        equals = MathTex("=", font_size=72)
        g_part = MathTex("G", font_size=72)

        numerator = MathTex("m_1 m_2", font_size=48)
        fraction_line = Line(LEFT * 0.6, RIGHT * 0.6, color=WHITE, stroke_width=2)
        denominator = MathTex("r^2", font_size=48)

        fraction_line.shift(UP * 1.5)
        numerator.next_to(fraction_line, UP, buff=0.15)
        denominator.next_to(fraction_line, DOWN, buff=0.15)

        fraction = VGroup(numerator, fraction_line, denominator)

        f_part.shift(UP * 1.5 + LEFT * 3)
        equals.next_to(f_part, RIGHT, buff=0.3)
        g_part.next_to(equals, RIGHT, buff=0.3)
        fraction.next_to(g_part, RIGHT, buff=0.3)

        equation = VGroup(f_part, equals, g_part, fraction)
        equation.move_to(UP * 1.5)

        self.play(FadeIn(equation, scale=1.2), run_time=1.5)
        self.wait(1)

        reassurance = StyledText("Let's break this down...")
        reassurance.scale(0.6)
        reassurance.to_edge(DOWN, buff=1)
        reassurance.set_color(ACCENT_COLOR)

        self.play(FadeIn(reassurance))
        self.wait(0.8)
        self.play(FadeOut(reassurance))

        # Highlight F
        self.play(f_part.animate.set_color(YELLOW), run_time=0.5)
        f_label = StyledText("Force of gravity")
        f_label.scale(0.5)
        f_label.next_to(f_part, DOWN, buff=0.8)
        f_label.set_color(YELLOW)
        self.play(FadeIn(f_label, shift=UP * 0.2))
        self.wait(1)
        self.play(f_part.animate.set_color(WHITE), FadeOut(f_label))

        # Highlight numerator m₁m₂
        self.play(numerator.animate.set_color(BLUE), run_time=0.5)
        mass_label = StyledText("Mass of object 1 × Mass of object 2")
        mass_label.scale(0.5)
        mass_label.next_to(fraction, DOWN, buff=0.8)
        mass_label.set_color(BLUE)
        self.play(FadeIn(mass_label, shift=UP * 0.2))
        self.wait(0.5)

        mass1 = create_mass(label="m_1", radius=0.4, color=BLUE)
        mass2 = create_mass(label="m_2", radius=0.5, color=RED)
        mass1.shift(DOWN * 2.5 + LEFT * 1.5)
        mass2.shift(DOWN * 2.5 + RIGHT * 1.5)
        self.play(FadeIn(mass1, scale=0.5), FadeIn(mass2, scale=0.5))
        self.wait(1)
        self.play(numerator.animate.set_color(WHITE), FadeOut(mass_label))

        # Highlight denominator r²
        self.play(denominator.animate.set_color(GREEN), run_time=0.5)
        r_label = StyledText("Distance between objects (squared)")
        r_label.scale(0.5)
        r_label.next_to(fraction, DOWN, buff=0.8)
        r_label.set_color(GREEN)
        self.play(FadeIn(r_label, shift=UP * 0.2))

        distance_line = Line(
            mass1.get_center(),
            mass2.get_center(),
            color=GREEN,
            stroke_width=4
        )
        distance_label = MathTex("r", font_size=48, color=GREEN)
        distance_label.next_to(distance_line, UP, buff=0.2)
        self.play(Create(distance_line), FadeIn(distance_label))
        self.wait(1.5)
        self.play(
            denominator.animate.set_color(WHITE),
            FadeOut(r_label),
            FadeOut(distance_line),
            FadeOut(distance_label)
        )

        # Highlight G
        self.play(g_part.animate.set_color(ACCENT_COLOR), run_time=0.5)
        g_label = StyledText("Gravitational constant")
        g_label.scale(0.5)
        g_label.next_to(g_part, UP, buff=0.5)
        g_label.set_color(ACCENT_COLOR)

        g_value = MathTex(
            "G = 6.67 \\times 10^{-11}",
            font_size=36,
            color=ACCENT_COLOR
        )
        g_value.next_to(g_part, DOWN, buff=0.5)

        tiny_text = StyledText("(Very tiny number!)")
        tiny_text.scale(0.4)
        tiny_text.next_to(g_value, DOWN, buff=0.1)
        tiny_text.set_color(ACCENT_COLOR)

        self.play(
            FadeIn(g_label),
            FadeIn(g_value, shift=UP * 0.1),
            FadeIn(tiny_text, shift=UP * 0.1)
        )
        self.wait(1.5)

        self.play(
            FadeOut(g_label),
            FadeOut(g_value),
            FadeOut(tiny_text),
            FadeOut(mass1),
            FadeOut(mass2),
            equation.animate.set_color(WHITE),
            run_time=0.8
        )

        self.equation = equation

    def demonstrate_relationships(self):
        """
        Part 3: Demonstrate the relationships
        Lines 100-105: Force grows with mass, shrinks with distance
        """
        self.play(
            self.equation.animate.scale(0.7).to_edge(UP, buff=0.5),
            run_time=0.8
        )

        mass1 = create_mass(label="m_1", radius=0.5, color=BLUE)
        mass2 = create_mass(label="m_2", radius=0.5, color=RED)
        mass1.shift(LEFT * 2)
        mass2.shift(RIGHT * 2)

        arrows = create_fbd_force_arrows(
            mass1,
            mass2,
            arrow_length=1.0,
            color=YELLOW,
            stroke_width=6
        )

        self.play(FadeIn(mass1), FadeIn(mass2), Create(arrows))
        self.wait(0.5)

        text1 = StyledText("Bigger masses →")
        text1.scale(0.6)
        text1.to_edge(DOWN, buff=1.5)
        self.play(FadeIn(text1))

        longer_arrows = create_fbd_force_arrows(
            mass1,
            mass2,
            arrow_length=1.6,
            color=YELLOW,
            stroke_width=8
        )

        self.play(
            mass1.animate.scale(1.5),
            mass2.animate.scale(1.5),
            Transform(arrows, longer_arrows),
            run_time=1.5
        )

        text2 = StyledText("Stronger force!")
        text2.scale(0.6)
        text2.next_to(text1, DOWN, buff=0.2)
        text2.set_color(ACCENT_COLOR)
        self.play(FadeIn(text2))
        self.wait(1)

        self.play(FadeOut(text1), FadeOut(text2), FadeOut(mass1), FadeOut(mass2), FadeOut(arrows))

        # Recreate at normal size for distance demonstration
        mass1 = create_mass(label="m_1", radius=0.5, color=BLUE)
        mass2 = create_mass(label="m_2", radius=0.5, color=RED)
        mass1.shift(LEFT * 2)
        mass2.shift(RIGHT * 2)

        arrows = create_fbd_force_arrows(
            mass1,
            mass2,
            arrow_length=1.0,
            color=YELLOW,
            stroke_width=6
        )

        self.play(FadeIn(mass1), FadeIn(mass2), Create(arrows))
        self.wait(0.3)

        text3 = StyledText("Farther apart →")
        text3.scale(0.6)
        text3.to_edge(DOWN, buff=1.5)
        self.play(FadeIn(text3))

        new_mass1_pos = mass1.get_center() + LEFT * 1.5
        new_mass2_pos = mass2.get_center() + RIGHT * 1.5

        temp_mass1 = mass1.copy().move_to(new_mass1_pos)
        temp_mass2 = mass2.copy().move_to(new_mass2_pos)

        shorter_arrows = create_fbd_force_arrows(
            temp_mass1,
            temp_mass2,
            arrow_length=0.5,
            color=YELLOW,
            stroke_width=3
        )

        self.play(
            mass1.animate.move_to(new_mass1_pos),
            mass2.animate.move_to(new_mass2_pos),
            Transform(arrows, shorter_arrows),
            run_time=1.5
        )

        text4 = StyledText("Weaker force!")
        text4.scale(0.6)
        text4.next_to(text3, DOWN, buff=0.2)
        text4.set_color(ACCENT_COLOR)
        self.play(FadeIn(text4))
        self.wait(1.5)

        self.play(
            *[FadeOut(mob) for mob in [mass1, mass2, arrows, text3, text4]],
            run_time=0.8
        )

    def question_1_inverse_square(self):
        """
        Part 4: Question 1 - Inverse Square Law
        Lines 106-114: "If you doubled the distance between two objects,
        what would happen to the gravitational force between them?"
        """
        self.play(FadeOut(self.equation), run_time=0.5)

        question_title = StyledText("Test Your Understanding:")
        question_title.scale(0.8)
        question_title.to_edge(UP, buff=0.5)
        question_title.set_color(ACCENT_COLOR)

        self.play(FadeIn(question_title))

        question_text = StyledText(
            "If you doubled the distance between two objects,\nwhat happens to the gravitational force?"
        )
        question_text.scale(0.65)
        question_text.next_to(question_title, DOWN, buff=0.5)

        self.play(Write(question_text, run_time=2))

        thinking = StyledText("Think about it...")
        thinking.scale(0.5)
        thinking.to_edge(DOWN, buff=1)
        thinking.set_color(YELLOW)

        self.play(FadeIn(thinking))
        self.wait(3.5)
        self.play(FadeOut(thinking))

        answer_title = StyledText("Answer:")
        answer_title.scale(0.7)
        answer_title.shift(UP * 0.3)
        answer_title.set_color(ACCENT_COLOR)

        self.play(FadeIn(answer_title))

        # Show equation with r replaced by 2r
        f_ans = MathTex("F", font_size=56)
        eq_ans = MathTex("=", font_size=56)
        g_ans = MathTex("G", font_size=56)

        num_ans = MathTex("m_1 m_2", font_size=42)
        frac_line_ans = Line(LEFT * 0.7, RIGHT * 0.7, color=WHITE, stroke_width=2)
        denom_ans = MathTex("(2r)^2", font_size=42)

        frac_line_ans.move_to(DOWN * 0.5)
        num_ans.next_to(frac_line_ans, UP, buff=0.15)
        denom_ans.next_to(frac_line_ans, DOWN, buff=0.15)

        fraction_ans = VGroup(num_ans, frac_line_ans, denom_ans)

        f_ans.move_to(LEFT * 1.8 + DOWN * 0.5)
        eq_ans.next_to(f_ans, RIGHT, buff=0.3)
        g_ans.next_to(eq_ans, RIGHT, buff=0.3)
        fraction_ans.next_to(g_ans, RIGHT, buff=0.3)

        equation_ans = VGroup(f_ans, eq_ans, g_ans, fraction_ans)
        equation_ans.move_to(DOWN * 0.5)

        self.play(Write(equation_ans))

        self.play(denom_ans.animate.set_color(GREEN), run_time=0.5)
        self.wait(0.5)

        arrow_right = Arrow(
            denom_ans.get_right(),
            denom_ans.get_right() + RIGHT * 1.5,
            color=GREEN,
            stroke_width=3
        )
        four_r_squared = MathTex("4r^2", font_size=42, color=GREEN)
        four_r_squared.next_to(arrow_right, RIGHT, buff=0.2)

        self.play(Create(arrow_right), FadeIn(four_r_squared))
        self.wait(1)

        final_answer = StyledText("Force becomes ONE-FOURTH as strong!")
        final_answer.scale(0.7)
        final_answer.to_edge(DOWN, buff=0.8)
        final_answer.set_color(ACCENT_COLOR)

        self.play(FadeIn(final_answer))
        self.wait(2)

        self.play(
            *[FadeOut(mob) for mob in [
                question_title, question_text, answer_title,
                equation_ans, arrow_right, four_r_squared, final_answer
            ]],
            run_time=0.8
        )


class VectorFormula(Scene):
    """
    Standalone scene: just the vector formula moment from Scene 3.
    """

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        Scene3.show_vector_formula(self)