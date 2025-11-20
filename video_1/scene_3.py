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
    create_force_arrow
)


class Scene3(Scene):
    """
    Scene 3: Newton's Big Discovery
    
    Introduces Newton's Law of Universal Gravitation:
    F = G * m₁ * m₂ / r²
    
    Explains each variable and demonstrates the relationships.
    
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
        
        # PART 4: Why don't we feel everyday gravity? (lines 109-125)
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
        equation = MathTex(
            "F", "=", "G", "\\frac{m_1 m_2}{r^2}",
            font_size=72
        )
        equation.set_color(WHITE)
        equation.shift(UP * 1.5)
        
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
        self.play(equation[0].animate.set_color(YELLOW), run_time=0.5)
        
        f_label = StyledText("Force of gravity")
        f_label.scale(0.5)
        f_label.next_to(equation[0], DOWN, buff=0.8)
        f_label.set_color(YELLOW)
        
        self.play(FadeIn(f_label, shift=UP * 0.2))
        self.wait(1)
        self.play(
            equation[0].animate.set_color(WHITE),
            FadeOut(f_label)
        )
        
        # Lines 91-92: Show two masses with labels m₁ and m₂
        # Create separate equation to highlight masses
        equation_split = MathTex(
            "F", "=", "G", "\\frac{", "m_1", "m_2", "}{r^2}",
            font_size=72
        )
        equation_split.move_to(equation)
        
        self.play(Transform(equation, equation_split))
        
        # Highlight m₁ and m₂
        self.play(
            equation[4].animate.set_color(BLUE),  # m₁
            equation[5].animate.set_color(RED),   # m₂
            run_time=0.5
        )
        
        # Show two masses below
        mass1 = create_mass(label="m_1", radius=0.4, color=BLUE)
        mass2 = create_mass(label="m_2", radius=0.5, color=RED)
        
        mass1.shift(DOWN * 1.8 + LEFT * 1.5)
        mass2.shift(DOWN * 1.8 + RIGHT * 1.5)
        
        self.play(
            FadeIn(mass1, scale=0.5),
            FadeIn(mass2, scale=0.5)
        )
        self.wait(1)
        
        # Lines 93-95: Show distance r
        equation_r = MathTex(
            "F", "=", "G", "\\frac{m_1 m_2}{", "r", "^2}",
            font_size=72
        )
        equation_r.move_to(equation)
        
        self.play(Transform(equation, equation_r))
        
        # Highlight r
        self.play(equation[4].animate.set_color(GREEN), run_time=0.5)
        
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
        
        # Lines 96-99: Highlight G - "very tiny number"
        equation_g = MathTex(
            "F", "=", "G", "\\frac{m_1 m_2}{r^2}",
            font_size=72
        )
        equation_g.move_to(equation)
        
        self.play(
            Transform(equation, equation_g),
            FadeOut(distance_line),
            FadeOut(distance_label)
        )
        
        self.play(equation[2].animate.set_color(ACCENT_COLOR), run_time=0.5)
        
        g_label = StyledText("Very tiny number!")
        g_label.scale(0.5)
        g_label.next_to(equation[2], UP, buff=0.5)
        g_label.set_color(ACCENT_COLOR)
        
        g_value = MathTex(
            "G = 6.67 \\times 10^{-11}",
            font_size=36,
            color=ACCENT_COLOR
        )
        g_value.next_to(g_label, DOWN, buff=0.2)
        
        self.play(
            FadeIn(g_label),
            FadeIn(g_value, shift=UP * 0.1)
        )
        self.wait(1.5)
        
        # Clean up for next part
        self.play(
            FadeOut(g_label),
            FadeOut(g_value),
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
        
        # Create two masses with force arrow
        mass1 = create_mass(label="m_1", radius=0.5, color=BLUE)
        mass2 = create_mass(label="m_2", radius=0.5, color=RED)
        
        mass1.shift(LEFT * 2)
        mass2.shift(RIGHT * 2)
        
        # Force arrow
        arrow = Arrow(
            mass1.get_right() + RIGHT * 0.1,
            mass2.get_left() + LEFT * 0.1,
            color=YELLOW,
            stroke_width=6,
            buff=0
        )
        
        self.play(
            FadeIn(mass1),
            FadeIn(mass2),
            Create(arrow)
        )
        self.wait(0.5)
        
        # Text: "Bigger masses..."
        text1 = StyledText("Bigger masses →")
        text1.scale(0.6)
        text1.to_edge(DOWN, buff=1.5)
        
        self.play(FadeIn(text1))
        
        # Animate masses getting LARGER, arrow grows
        self.play(
            mass1.animate.scale(1.5),
            mass2.animate.scale(1.5),
            arrow.animate.scale_to_fit_width(arrow.width * 1.3).set_stroke(width=10),
            run_time=1.5
        )
        
        text2 = StyledText("Stronger force!")
        text2.scale(0.6)
        text2.next_to(text1, DOWN, buff=0.2)
        text2.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(text2))
        self.wait(1)
        
        # Reset
        self.play(
            FadeOut(text1),
            FadeOut(text2)
        )
        
        # Recreate at normal size
        self.play(
            FadeOut(mass1),
            FadeOut(mass2),
            FadeOut(arrow)
        )
        
        mass1 = create_mass(label="m_1", radius=0.5, color=BLUE)
        mass2 = create_mass(label="m_2", radius=0.5, color=RED)
        mass1.shift(LEFT * 2)
        mass2.shift(RIGHT * 2)
        arrow = Arrow(
            mass1.get_right() + RIGHT * 0.1,
            mass2.get_left() + LEFT * 0.1,
            color=YELLOW,
            stroke_width=6,
            buff=0
        )
        
        self.play(
            FadeIn(mass1),
            FadeIn(mass2),
            Create(arrow)
        )
        
        # Text: "Farther apart..."
        text3 = StyledText("Farther apart →")
        text3.scale(0.6)
        text3.to_edge(DOWN, buff=1.5)
        
        self.play(FadeIn(text3))
        
        # Animate masses moving APART, arrow shrinks
        self.play(
            mass1.animate.shift(LEFT * 1.5),
            mass2.animate.shift(RIGHT * 1.5),
            arrow.animate.scale_to_fit_width(arrow.width * 1.8).set_stroke(width=3),
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
            *[FadeOut(mob) for mob in [mass1, mass2, arrow, text3, text4]],
            run_time=0.8
        )
    
    def everyday_gravity_explanation(self):
        """
        Part 4: Why don't we feel everyday gravity?
        Lines 109-125: Explain why we don't feel gravity between everyday objects
        """
        # Bring back two small objects (balls)
        ball1 = create_mass(label="", radius=0.2, color=RED, show_label=False)
        ball2 = create_mass(label="", radius=0.2, color=ORANGE, show_label=False)
        
        ball1.shift(LEFT * 1.5)
        ball2.shift(RIGHT * 1.5)
        
        # Tiny, almost invisible arrow
        tiny_arrow = Line(
            ball1.get_right(),
            ball2.get_left(),
            color=YELLOW,
            stroke_width=1,
            stroke_opacity=0.3
        )
        tiny_arrow.add_tip(tip_length=0.05)
        
        self.play(
            FadeIn(ball1),
            FadeIn(ball2),
            Create(tiny_arrow)
        )
        
        # Text: "Tiny force"
        tiny_text = StyledText("Tiny force (barely exists!)")
        tiny_text.scale(0.5)
        tiny_text.next_to(tiny_arrow, UP, buff=0.3)
        tiny_text.set_color(YELLOW)
        
        self.play(FadeIn(tiny_text))
        self.wait(1)
        
        # Zoom out to show Earth
        self.play(
            ball1.animate.scale(0.3).shift(UP * 1.5),
            ball2.animate.scale(0.3).shift(UP * 1.5),
            tiny_arrow.animate.scale(0.3).shift(UP * 1.5),
            tiny_text.animate.scale(0.5).shift(UP * 2.2),
            run_time=1
        )
        
        # Show Earth
        earth = create_earth(radius=1.5)
        earth.shift(DOWN * 1.5)
        
        # Huge arrow from Earth to balls
        huge_arrow = Arrow(
            earth.get_top(),
            ball1.get_bottom() + ball2.get_bottom() / 2,
            color=YELLOW,
            stroke_width=12,
            buff=0.2
        )
        
        self.play(
            FadeIn(earth, scale=0.8),
            Create(huge_arrow)
        )
        
        # Text: "HUGE force"
        huge_text = StyledText("HUGE force!")
        huge_text.scale(0.7)
        huge_text.next_to(huge_arrow, RIGHT, buff=0.5)
        huge_text.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(huge_text))
        self.wait(1)
        
        # Show Earth's mass (lines 120-124)
        earth_mass = MathTex(
            "M_{Earth} = 6 \\times 10^{24} \\text{ kg}",
            font_size=48,
            color=ACCENT_COLOR
        )
        earth_mass.next_to(earth, DOWN, buff=0.5)
        
        self.play(Write(earth_mass, run_time=1.5))
        self.wait(2)
        
        # Clean up (will be faded by main construct)