"""
Scene 2: Setting the Stage (0:45-1:30)

This scene introduces the concept that gravity is a universal force of attraction
between all masses, not just "what makes things fall down."

From PDF transcript lines 41-73.
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
    create_logo,
    BACKGROUND_COLOR,
    ACCENT_COLOR,
    TEXT_COLOR
)
from utils.physics_objects import (
    create_mass,
    create_earth,
    create_force_arrow,
    create_attraction_arrows,
    create_simple_person,
    create_phone,
    create_desk,
    create_ball
)


class Scene2(Scene):
    """
    Scene 2: Setting the Stage
    
    Introduces the universal nature of gravity:
    - Ball falling to Earth
    - Mutual attraction between two masses
    - Earth and person pulling on each other
    - All objects in a room attracting each other
    
    Duration: 0:45-1:30 (45 seconds)
    From PDF lines 41-73
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Add persistent logo in corner
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)
        
        # PART 1: Ball falling toward Earth (lines 46-47)
        # "Animate a simple ball falling toward Earth"
        self.ball_falling_demo()
        
        # PART 2: Two masses with mutual attraction (lines 55-57)
        # "Animate two masses (circles) with arrows pointing toward each other. Label them m1 and m2"
        self.two_masses_demo()
        
        # PART 3: Earth and person (lines 58-62)
        # "Show Earth and a person, with arrows pointing both ways"
        # "That means Earth is pulling on you... but you're also pulling on Earth!"
        self.earth_and_person_demo()
        
        # PART 4: Multiple objects in room (lines 64-70)
        # "Zoom out to show multiple objects in a room - phone, desk, person - all with tiny arrows"
        self.room_objects_demo()
        
        # Hold final frame before transition
        self.wait(2)
        
        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def ball_falling_demo(self):
        """
        Part 1: Simple ball falling toward Earth
        Lines 46-47: "Animate a simple ball falling toward Earth"
        """
        # Create Earth at bottom
        earth = create_earth(radius=1.2)
        earth.to_edge(DOWN, buff=0.5)
        
        # Create ball above Earth
        ball = create_ball(radius=0.25, color=RED)
        ball.shift(UP * 2)
        
        # Create downward arrow
        arrow = Arrow(
            start=ball.get_bottom() + DOWN * 0.3,
            end=ball.get_bottom() + DOWN * 1.5,
            color=YELLOW,
            stroke_width=6
        )
        
        # Animate
        self.play(
            FadeIn(earth),
            fade_in_from_bottom(ball, run_time=0.8)
        )
        self.wait(0.5)
        
        # Show arrow and ball falling
        self.play(Create(arrow))
        self.play(
            ball.animate.shift(DOWN * 1.5),
            arrow.animate.shift(DOWN * 1.5),
            run_time=1.5,
            rate_func=rate_functions.ease_in_quad
        )
        self.wait(0.5)
        
        # Fade out for next part
        self.play(
            FadeOut(earth),
            FadeOut(ball),
            FadeOut(arrow),
            run_time=0.8
        )
    
    def two_masses_demo(self):
        """
        Part 2: Two masses with mutual attraction
        Lines 55-57: "Animate two masses (circles) with arrows pointing toward each other. 
        Label them m1 and m2"
        
        Lines 52-54: "Gravity isn't just Earth pulling things down. 
        It's a force of attraction between ALL objects that have mass."
        """
        # Create text for key concept
        concept_text = StyledText("Gravity = Force of Attraction")
        concept_text.scale(0.8)
        concept_text.to_edge(UP, buff=0.8)
        
        self.play(Write(concept_text))
        self.wait(0.5)
        
        # Create two masses
        mass1 = create_mass(label="m_1", radius=0.5, color=BLUE)
        mass2 = create_mass(label="m_2", radius=0.6, color=RED)
        
        # Position them
        mass1.shift(LEFT * 2.5 + DOWN * 0.5)
        mass2.shift(RIGHT * 2.5 + DOWN * 0.5)
        
        # Animate masses appearing
        self.play(
            fade_in_with_scale(mass1, start_scale=0.3),
            fade_in_with_scale(mass2, start_scale=0.3),
            run_time=1.2
        )
        self.wait(0.3)
        
        # Create attraction arrows
        arrows = create_attraction_arrows(mass1, mass2, color=YELLOW)
        
        # Animate arrows
        self.play(
            LaggedStart(
                Create(arrows[0]),
                Create(arrows[1]),
                lag_ratio=0.3,
                run_time=1.2
            )
        )
        self.wait(1)
        
        # Add "between ALL objects" emphasis
        all_text = StyledText("Between ALL Masses")
        all_text.scale(0.7)
        all_text.next_to(concept_text, DOWN, buff=0.3)
        all_text.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(all_text))
        self.wait(1.5)
        
        # Fade out for next part
        self.play(
            FadeOut(concept_text),
            FadeOut(all_text),
            FadeOut(mass1),
            FadeOut(mass2),
            FadeOut(arrows),
            run_time=0.8
        )
    
    def earth_and_person_demo(self):
        """
        Part 3: Earth and person pulling on each other
        Lines 58-62: "Show Earth and a person, with arrows pointing both ways"
        "That means Earth is pulling on you... but you're also pulling on Earth!"
        """
        # Create Earth
        earth = create_earth(radius=1.8)
        earth.shift(DOWN * 1.5 + LEFT * 2)
        
        # Create person
        person = create_simple_person(height=1.2)
        person.shift(UP * 0.5 + RIGHT * 2)
        
        # Animate them appearing
        self.play(
            FadeIn(earth, scale=0.8),
            FadeIn(person, shift=DOWN * 0.5),
            run_time=1
        )
        self.wait(0.5)
        
        # Create bidirectional arrows
        arrows = create_attraction_arrows(earth, person, color=YELLOW)
        
        # Animate arrows one at a time for emphasis
        self.play(Create(arrows[0]), run_time=0.8)  # Earth pulls on you
        
        # Add text: "Earth pulls on you"
        text1 = StyledText("Earth pulls on you")
        text1.scale(0.6)
        text1.to_edge(UP, buff=0.5)
        self.play(FadeIn(text1))
        self.wait(0.8)
        
        self.play(Create(arrows[1]), run_time=0.8)  # You pull on Earth!
        
        # Add text: "You pull on Earth!"
        text2 = StyledText("You pull on Earth!")
        text2.scale(0.6)
        text2.next_to(text1, DOWN, buff=0.3)
        text2.set_color(ACCENT_COLOR)
        self.play(FadeIn(text2))
        self.wait(1.5)
        
        # Fade out for next part
        self.play(
            *[FadeOut(mob) for mob in [earth, person, arrows, text1, text2]],
            run_time=0.8
        )
    
    def room_objects_demo(self):
        """
        Part 4: Multiple objects in a room
        Lines 64-70: "Zoom out to show multiple objects in a room - phone, desk, person - 
        all with tiny arrows pointing between them"
        "Your phone is pulling on you. You're pulling on your desk. 
        Every object in this room is pulling on every other object."
        """
        # Create objects
        person = create_simple_person(height=0.8)
        person.shift(LEFT * 2 + DOWN * 0.5)
        
        phone = create_phone(scale=0.8)
        phone.shift(RIGHT * 2 + UP * 1)
        
        desk = create_desk(scale=0.8)
        desk.shift(RIGHT * 1.5 + DOWN * 1.5)
        
        ball = create_ball(radius=0.2, color=ORANGE)
        ball.shift(LEFT * 2.5 + UP * 1.5)
        
        # Group all objects
        all_objects = VGroup(person, phone, desk, ball)
        
        # Animate objects appearing
        self.play(
            LaggedStart(
                *[FadeIn(obj, scale=0.8) for obj in all_objects],
                lag_ratio=0.2,
                run_time=2
            )
        )
        self.wait(0.5)
        
        # Create small arrows between ALL objects
        arrows = VGroup()
        objects_list = [person, phone, desk, ball]
        
        for i, obj1 in enumerate(objects_list):
            for j, obj2 in enumerate(objects_list):
                if i < j:  # Only create each pair once
                    # Create small arrows
                    center1 = obj1.get_center()
                    center2 = obj2.get_center()
                    
                    # Create thin, semi-transparent arrows
                    arrow = Line(
                        start=center1,
                        end=center2,
                        color=YELLOW,
                        stroke_width=1.5,
                        stroke_opacity=0.6
                    )
                    arrow.add_tip(tip_length=0.1)
                    arrows.add(arrow)
        
        # Animate all arrows appearing
        self.play(
            LaggedStart(
                *[Create(arrow) for arrow in arrows],
                lag_ratio=0.1,
                run_time=2
            )
        )
        
        # Add text
        text = StyledText("Everything attracts everything!")
        text.scale(0.7)
        text.to_edge(UP, buff=0.5)
        text.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(text))
        self.wait(2)
        
        # Fade out text (objects and arrows will be faded by main construct)
        self.play(FadeOut(text))