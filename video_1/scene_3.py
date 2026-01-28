"""
Scene 3: Newton's Big Discovery (1:30-2:30)

This scene introduces Newton's Law of Universal Gravitation and explains
each component of the equation.

From PDF transcript lines 74-125.
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
    
    Explains each variable and demonstrates the relationships.
    Includes Question 1 about inverse square law.
    
    Duration: 1:30-2:30 (60 seconds)
    From PDF lines 74-125
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Add persistent logo
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)
        
        # PART 1: Introduce Newton and the law (lines 78-82)
        self.introduce_newton()
        
        # PART 2: Show and explain the equation (lines 82-99)
        self.show_equation()
        
        # PART 3: Demonstrate the relationships (lines 100-105)
        self.demonstrate_relationships()
        
        # PART 4: **NEW** Interactive Question 1 - Inverse Square Law (lines 106-114)
        self.question_1_inverse_square()
        
        # PART 5: Why don't we feel everyday gravity? (lines 115-125)
        self.everyday_gravity_explanation()
        
        # Hold final frame
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def introduce_newton(self):
        """
        Part 1: Introduce Newton and the law
        Lines 78-80: "In 1687, Isaac Newton figured out the exact rule for how gravity works. 
        He called it the Law of Universal Gravitation"
        """
        # Title
        title = StyledTitle("Newton's Law of Universal Gravitation")
        title.scale(0.6)
        title.to_edge(UP, buff=0.5)
        
        # Subtitle
        subtitle = StyledText("1687")
        subtitle.scale(0.7)
        subtitle.next_to(title, DOWN, buff=0.3)
        subtitle.set_color(ACCENT_COLOR)
        
        self.play(
            Write(title, run_time=1.5),
            FadeIn(subtitle, shift=UP * 0.2)
        )
        self.wait(1.5)
        
        # Fade out to make room for equation
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            run_time=0.8
        )
    
    def show_equation(self):
        """
        Part 2: Show and explain the equation
        Lines 82-99: Show F = G m₁m₂/r² and explain each variable
        """
        # Line 82: "Equation fades in gracefully"
        # Create equation by manually composing parts
        f_part = MathTex("F", font_size=72)
        equals = MathTex("=", font_size=72)
        g_part = MathTex("G", font_size=72)
        
        # Fraction parts - numerator and denominator
        numerator = MathTex("m_1 m_2", font_size=48)
        fraction_line = Line(LEFT * 0.6, RIGHT * 0.6, color=WHITE, stroke_width=2)
        denominator = MathTex("r^2", font_size=48)
        
        # Position the fraction
        fraction_line.shift(UP * 1.5)
        numerator.next_to(fraction_line, UP, buff=0.15)
        denominator.next_to(fraction_line, DOWN, buff=0.15)
        
        # Group the fraction
        fraction = VGroup(numerator, fraction_line, denominator)
        
        # Position left side of equation
        f_part.shift(UP * 1.5 + LEFT * 3)
        equals.next_to(f_part, RIGHT, buff=0.3)
        g_part.next_to(equals, RIGHT, buff=0.3)
        fraction.next_to(g_part, RIGHT, buff=0.3)
        
        # Create the full equation group
        equation = VGroup(f_part, equals, g_part, fraction)
        equation.move_to(UP * 1.5)
        
        self.play(FadeIn(equation, scale=1.2), run_time=1.5)
        self.wait(1)
        
        # Lines 85-86: "Don't worry if equations make you nervous—let's break this down together"
        reassurance = StyledText("Let's break this down...")
        reassurance.scale(0.6)
        reassurance.to_edge(DOWN, buff=1)
        reassurance.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(reassurance))
        self.wait(0.8)
        self.play(FadeOut(reassurance))
        
        # Line 90: Highlight F - "F is the force of gravity"
        self.play(f_part.animate.set_color(YELLOW), run_time=0.5)
        
        f_label = StyledText("Force of gravity")
        f_label.scale(0.5)
        f_label.next_to(f_part, DOWN, buff=0.8)
        f_label.set_color(YELLOW)
        
        self.play(FadeIn(f_label, shift=UP * 0.2))
        self.wait(1)
        self.play(
            f_part.animate.set_color(WHITE),
            FadeOut(f_label)
        )
        
        # Lines 91-92: Show two masses with labels m₁ and m₂
        # Highlight the numerator (m_1 m_2)
        self.play(numerator.animate.set_color(BLUE), run_time=0.5)
        
        # Show label for masses
        mass_label = StyledText("Mass of object 1 × Mass of object 2")
        mass_label.scale(0.5)
        mass_label.next_to(fraction, DOWN, buff=0.8)
        mass_label.set_color(BLUE)
        
        self.play(FadeIn(mass_label, shift=UP * 0.2))
        self.wait(0.5)
        
        # Show two masses below
        mass1 = create_mass(label="m_1", radius=0.4, color=BLUE)
        mass2 = create_mass(label="m_2", radius=0.5, color=RED)
        
        mass1.shift(DOWN * 2.5 + LEFT * 1.5)
        mass2.shift(DOWN * 2.5 + RIGHT * 1.5)
        
        self.play(
            FadeIn(mass1, scale=0.5),
            FadeIn(mass2, scale=0.5)
        )
        self.wait(1)
        
        self.play(
            numerator.animate.set_color(WHITE),
            FadeOut(mass_label)
        )
        
        # Lines 93-95: Show distance r
        # Highlight the denominator (r^2)
        self.play(denominator.animate.set_color(GREEN), run_time=0.5)
        
        r_label = StyledText("Distance between objects (squared)")
        r_label.scale(0.5)
        r_label.next_to(fraction, DOWN, buff=0.8)
        r_label.set_color(GREEN)
        
        self.play(FadeIn(r_label, shift=UP * 0.2))
        
        # Draw line between masses showing r
        distance_line = Line(
            mass1.get_center(),
            mass2.get_center(),
            color=GREEN,
            stroke_width=4
        )
        distance_label = MathTex("r", font_size=48, color=GREEN)
        distance_label.next_to(distance_line, UP, buff=0.2)
        
        self.play(
            Create(distance_line),
            FadeIn(distance_label)
        )
        self.wait(1.5)
        
        self.play(
            denominator.animate.set_color(WHITE),
            FadeOut(r_label),
            FadeOut(distance_line),
            FadeOut(distance_label)
        )
        
        # Lines 96-99: Highlight G - "very tiny number"
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
        
        # Clean up for next part
        self.play(
            FadeOut(g_label),
            FadeOut(g_value),
            FadeOut(tiny_text),
            FadeOut(mass1),
            FadeOut(mass2),
            equation.animate.set_color(WHITE),
            run_time=0.8
        )
        
        # Store equation for next part
        self.equation = equation
    
    def demonstrate_relationships(self):
        """
        Part 3: Demonstrate the relationships
        Lines 100-105: "The force of gravity gets stronger when objects are more massive, 
        and it gets weaker when they're farther apart"
        """
        # Move equation to top
        self.play(
            self.equation.animate.scale(0.7).to_edge(UP, buff=0.5),
            run_time=0.8
        )
        
        # Create two masses with force arrows
        mass1 = create_mass(label="m_1", radius=0.5, color=BLUE)
        mass2 = create_mass(label="m_2", radius=0.5, color=RED)
        
        mass1.shift(LEFT * 2)
        mass2.shift(RIGHT * 2)
        
        # Initial force arrows (normal length)
        arrows = create_fbd_force_arrows(
            mass1, 
            mass2, 
            arrow_length=1.0,
            color=YELLOW,
            stroke_width=6
        )
        
        self.play(
            FadeIn(mass1),
            FadeIn(mass2),
            Create(arrows)
        )
        self.wait(0.5)
        
        # Text: "Bigger masses..."
        text1 = StyledText("Bigger masses →")
        text1.scale(0.6)
        text1.to_edge(DOWN, buff=1.5)
        
        self.play(FadeIn(text1))
        
        # Create LONGER arrows for stronger force
        longer_arrows = create_fbd_force_arrows(
            mass1, 
            mass2, 
            arrow_length=1.6,
            color=YELLOW,
            stroke_width=8
        )
        
        # Animate masses getting LARGER and arrows getting LONGER simultaneously
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
        
        # Reset - fade out everything
        self.play(
            FadeOut(text1),
            FadeOut(text2),
            FadeOut(mass1),
            FadeOut(mass2),
            FadeOut(arrows)
        )
        
        # Recreate at normal size for distance demonstration
        mass1 = create_mass(label="m_1", radius=0.5, color=BLUE)
        mass2 = create_mass(label="m_2", radius=0.5, color=RED)
        mass1.shift(LEFT * 2)
        mass2.shift(RIGHT * 2)
        
        # Normal arrows again
        arrows = create_fbd_force_arrows(
            mass1, 
            mass2, 
            arrow_length=1.0,
            color=YELLOW,
            stroke_width=6
        )
        
        self.play(
            FadeIn(mass1),
            FadeIn(mass2),
            Create(arrows)
        )
        self.wait(0.3)
        
        # Text: "Farther apart..."
        text3 = StyledText("Farther apart →")
        text3.scale(0.6)
        text3.to_edge(DOWN, buff=1.5)
        
        self.play(FadeIn(text3))
        
        # Store new positions for masses
        new_mass1_pos = mass1.get_center() + LEFT * 1.5
        new_mass2_pos = mass2.get_center() + RIGHT * 1.5
        
        # Create a temporary copy to calculate new arrow positions
        temp_mass1 = mass1.copy().move_to(new_mass1_pos)
        temp_mass2 = mass2.copy().move_to(new_mass2_pos)
        
        # Create shorter arrows for weaker force at new positions
        shorter_arrows = create_fbd_force_arrows(
            temp_mass1, 
            temp_mass2, 
            arrow_length=0.5,
            color=YELLOW,
            stroke_width=3
        )
        
        # Animate masses moving APART and arrows getting SHORTER simultaneously
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
        
        # Clean up
        self.play(
            *[FadeOut(mob) for mob in [mass1, mass2, arrows, text3, text4]],
            run_time=0.8
        )
    
    def question_1_inverse_square(self):
        """
        **NEW PART 4:** Interactive Question 1 - Inverse Square Law
        Lines 106-114: Test understanding about doubling distance
        
        "Let's test your understanding. If you doubled the distance between two objects, 
        what would happen to the gravitational force between them?"
        """
        # Fade out equation first
        self.play(FadeOut(self.equation), run_time=0.5)
        
        # Question title
        question_title = StyledText("Test Your Understanding:")
        question_title.scale(0.8)
        question_title.to_edge(UP, buff=0.5)
        question_title.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(question_title))
        
        # Question text
        question_text = StyledText(
            "If you doubled the distance between two objects,\nwhat happens to the gravitational force?"
        )
        question_text.scale(0.65)
        question_text.next_to(question_title, DOWN, buff=0.5)
        
        self.play(Write(question_text, run_time=2))
        
        # Pause for thinking (3-4 seconds)
        thinking = StyledText("Think about it...")
        thinking.scale(0.5)
        thinking.to_edge(DOWN, buff=1)
        thinking.set_color(YELLOW)
        
        self.play(FadeIn(thinking))
        self.wait(3.5)
        self.play(FadeOut(thinking))
        
        # Show answer (lines 109-114)
        answer_title = StyledText("Answer:")
        answer_title.scale(0.7)
        answer_title.shift(UP * 0.3)
        answer_title.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(answer_title))
        
        # Show equation with r being replaced by 2r
        # Create equation: F = G m₁m₂/(2r)²
        f_ans = MathTex("F", font_size=56)
        eq_ans = MathTex("=", font_size=56)
        g_ans = MathTex("G", font_size=56)
        
        # Fraction with (2r)²
        num_ans = MathTex("m_1 m_2", font_size=42)
        frac_line_ans = Line(LEFT * 0.7, RIGHT * 0.7, color=WHITE, stroke_width=2)
        denom_ans = MathTex("(2r)^2", font_size=42)
        
        # Position fraction
        frac_line_ans.move_to(DOWN * 0.5)
        num_ans.next_to(frac_line_ans, UP, buff=0.15)
        denom_ans.next_to(frac_line_ans, DOWN, buff=0.15)
        
        fraction_ans = VGroup(num_ans, frac_line_ans, denom_ans)
        
        # Position left side
        f_ans.move_to(LEFT * 1.8 + DOWN * 0.5)
        eq_ans.next_to(f_ans, RIGHT, buff=0.3)
        g_ans.next_to(eq_ans, RIGHT, buff=0.3)
        fraction_ans.next_to(g_ans, RIGHT, buff=0.3)
        
        equation_ans = VGroup(f_ans, eq_ans, g_ans, fraction_ans)
        equation_ans.move_to(DOWN * 0.5)
        
        self.play(Write(equation_ans))
        
        # Highlight (2r)²
        self.play(denom_ans.animate.set_color(GREEN), run_time=0.5)
        self.wait(0.5)
        
        # Show that this equals 4r²
        arrow_right = Arrow(
            denom_ans.get_right(),
            denom_ans.get_right() + RIGHT * 1.5,
            color=GREEN,
            stroke_width=3
        )
        four_r_squared = MathTex("4r^2", font_size=42, color=GREEN)
        four_r_squared.next_to(arrow_right, RIGHT, buff=0.2)
        
        self.play(
            Create(arrow_right),
            FadeIn(four_r_squared)
        )
        self.wait(1)
        
        # Final answer text
        final_answer = StyledText("Force becomes ONE-FOURTH as strong!")
        final_answer.scale(0.7)
        final_answer.to_edge(DOWN, buff=0.8)
        final_answer.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(final_answer))
        self.wait(2)
        
        # Clean up
        self.play(
            *[FadeOut(mob) for mob in [
                question_title, question_text, answer_title, 
                equation_ans, arrow_right, four_r_squared, final_answer
            ]],
            run_time=0.8
        )
    
    def everyday_gravity_explanation(self):
        """
        Part 5: Why don't we feel everyday gravity? (UPDATED with basketball/tennis ball)
        Lines 115-125: Explain why we don't feel gravity between everyday objects
        """
        # Bring back basketball and tennis ball (instead of generic balls)
        basketball = create_ball(radius=0.35, color=ORANGE, pattern=True)
        basketball.shift(LEFT * 1.8)
        
        tennis_ball = create_ball(radius=0.2, color=GREEN, pattern=True)
        tennis_ball.shift(RIGHT * 1.8)
        
        # Create FBD arrows between balls (very short to show weak force)
        tiny_arrows = create_fbd_force_arrows(
            basketball,
            tennis_ball,
            arrow_length=0.3,
            color=YELLOW,
            stroke_width=2
        )
        tiny_arrows.set_opacity(0.3)
        
        self.play(
            FadeIn(basketball),
            FadeIn(tennis_ball),
            Create(tiny_arrows)
        )
        
        # Text: "Tiny force"
        tiny_text = StyledText("Tiny force (barely exists!)")
        tiny_text.scale(0.5)
        tiny_text.next_to(VGroup(basketball, tennis_ball), UP, buff=0.3)
        tiny_text.set_color(YELLOW)
        
        self.play(FadeIn(tiny_text))
        self.wait(1)
        
        # Group balls and arrows together so they move as one unit
        ball_group = VGroup(basketball, tennis_ball, tiny_text, tiny_arrows)
        
        # Zoom out to show Earth - move the group together
        self.play(
            ball_group.animate.scale(0.3).shift(UP * 1.5),
            run_time=1
        )
        
        # Show Earth
        earth = create_earth(radius=1.5)
        earth.shift(DOWN * 1.5)
        
        self.play(FadeIn(earth, scale=0.8))
        self.wait(0.3)
        
        # Create FBD arrows from Earth to each ball (huge to show strong force)
        earth_to_ball1_arrows = create_fbd_force_arrows(
            earth,
            basketball,
            arrow_length=1.0,
            color=YELLOW,
            stroke_width=12
        )
        
        earth_to_ball2_arrows = create_fbd_force_arrows(
            earth,
            tennis_ball,
            arrow_length=1.0,
            color=YELLOW,
            stroke_width=12
        )
        
        # Show all arrows from Earth
        self.play(
            Create(earth_to_ball1_arrows[0]),
            Create(earth_to_ball2_arrows[0]),
            Create(earth_to_ball1_arrows[1]),
            Create(earth_to_ball2_arrows[1])
        )
        
        # Text: "HUGE force"
        huge_text = StyledText("HUGE force!")
        huge_text.scale(0.7)
        huge_text.next_to(earth, RIGHT, buff=1.5)
        huge_text.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(huge_text))
        self.wait(1)
        
        # Show Earth's mass (lines 120-124)
        earth_mass = MathTex(
            "M_{\\text{Earth}} = 6 \\times 10^{24} \\text{ kg}",
            font_size=48,
            color=ACCENT_COLOR
        )
        earth_mass.next_to(earth, DOWN, buff=0.3)
        
        self.play(Write(earth_mass, run_time=1.5))
        self.wait(2)
        
        # Clean up (will be faded by main construct)