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
    create_fbd_force_arrows,
    create_simple_person,
    create_phone,
    create_desk,
    create_ball
)


class Scene2(Scene):
    """
    Scene 2: Setting the Stage

    Introduces the universal nature of gravity:
    - Tennis ball falling to Earth
    - Mutual attraction between two masses
    - Earth and person pulling on each other
    - All objects in a room attracting each other

    Duration: 0:45-1:30 (45 seconds)
    From PDF lines 41-73
    """

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self.animate_scene()

    def animate_scene(self):
        """All scene animation logic. Called by construct() and importable by full_video.py."""

        # Add persistent logo in corner
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        # PART 1: Tennis ball falling toward Earth (lines 46-47)
        Scene2.ball_falling_demo(self)

        # PART 2: Two masses with mutual attraction (lines 55-57)
        Scene2.two_masses_demo(self)

        # PART 3: Earth and person (lines 58-62)
        Scene2.earth_and_person_demo(self)

        # PART 4: Multiple objects in room (lines 64-70)
        Scene2.room_objects_demo(self)

        # Hold final frame before transition
        self.wait(2)

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def ball_falling_demo(self):
        """
        Part 1: Tennis ball falling toward Earth
        Lines 46-47: "Animate a simple ball falling toward Earth"
        """
        earth = create_earth(radius=1.2)
        earth.to_edge(DOWN, buff=0.5)

        tennis_ball = create_ball(radius=0.2, color=GREEN, pattern=True)
        tennis_ball.shift(UP * 2)

        arrows = create_fbd_force_arrows(
            earth,
            tennis_ball,
            arrow_length=1.0,
            color=YELLOW,
            stroke_width=6
        )
        ball_arrow = arrows[1]
        earth_arrow = arrows[0]

        self.play(
            FadeIn(earth),
            fade_in_from_bottom(tennis_ball, run_time=0.8)
        )
        self.wait(0.5)

        self.play(Create(ball_arrow))
        self.play(Create(earth_arrow))
        self.play(
            tennis_ball.animate.shift(DOWN * 3.0),
            ball_arrow.animate.shift(DOWN * 3.0),
            run_time=2.5,
            rate_func=rate_functions.ease_in_quad
        )
        self.wait(0.5)

        self.play(
            FadeOut(earth),
            FadeOut(tennis_ball),
            FadeOut(ball_arrow),
            FadeOut(earth_arrow),
            run_time=0.8
        )

    def two_masses_demo(self):
        """
        Part 2: Two masses with mutual attraction - FBD ARROWS
        Lines 55-57: "Animate two masses (circles) with arrows pointing toward each other.
        Label them m1 and m2"
        """
        concept_text = StyledText("Gravity = Force of Attraction")
        concept_text.scale(0.8)
        concept_text.to_edge(UP, buff=0.8)

        self.play(Write(concept_text))
        self.wait(0.5)

        # Mass 1: Larger, blue
        mass1_circle = Circle(
            radius=0.6,
            fill_color=BLUE,
            fill_opacity=0.7,
            stroke_color=BLUE_E,
            stroke_width=3
        )
        mass1_label = MathTex("m_1", font_size=42, color=WHITE)
        mass1_label.move_to(mass1_circle.get_center())
        mass1 = VGroup(mass1_circle, mass1_label)

        # Mass 2: Smaller, red-orange with stripes
        mass2_circle = Circle(
            radius=0.4,
            fill_color=RED_C,
            fill_opacity=0.8,
            stroke_color=RED_E,
            stroke_width=3
        )
        stripe1 = Line(
            mass2_circle.get_top() + LEFT * 0.3,
            mass2_circle.get_bottom() + LEFT * 0.1,
            color=ORANGE,
            stroke_width=2
        )
        stripe2 = Line(
            mass2_circle.get_top() + RIGHT * 0.1,
            mass2_circle.get_bottom() + RIGHT * 0.3,
            color=ORANGE,
            stroke_width=2
        )
        mass2_label = MathTex("m_2", font_size=36, color=WHITE)
        mass2_label.move_to(mass2_circle.get_center())
        mass2 = VGroup(mass2_circle, stripe1, stripe2, mass2_label)

        mass1.shift(LEFT * 3 + DOWN * 0.5)
        mass2.shift(RIGHT * 2.5 + DOWN * 0.5)

        self.play(
            fade_in_with_scale(mass1, start_scale=0.3),
            fade_in_with_scale(mass2, start_scale=0.3),
            run_time=1.2
        )
        self.wait(0.3)

        # FBD-style attraction arrows
        arrows = create_fbd_force_arrows(
            mass1,
            mass2,
            arrow_length=1.2,
            color=YELLOW,
            stroke_width=5
        )

        self.play(
            LaggedStart(
                Create(arrows[0]),
                Create(arrows[1]),
                lag_ratio=0.3,
                run_time=1.2
            )
        )
        self.wait(1)

        all_text = StyledText("Between ALL Masses")
        all_text.scale(0.7)
        all_text.next_to(concept_text, DOWN, buff=0.3)
        all_text.set_color(ACCENT_COLOR)

        self.play(FadeIn(all_text))
        self.wait(1.5)

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
        Part 3: Earth and person pulling on each other - FBD ARROWS
        Lines 58-62: "Show Earth and a person, with arrows pointing both ways"
        """
        earth = create_earth(radius=1.8)
        earth.shift(DOWN * 1.5 + LEFT * 2)

        person = create_simple_person(height=1.2)
        person.shift(UP * 0.5 + RIGHT * 2)

        self.play(
            FadeIn(earth, scale=0.8),
            FadeIn(person, shift=DOWN * 0.5),
            run_time=1
        )
        self.wait(0.5)

        arrows = create_fbd_force_arrows(
            earth,
            person,
            arrow_length=1.5,
            color=YELLOW,
            stroke_width=5
        )

        self.play(Create(arrows[1]), run_time=0.8)

        text1 = StyledText("Earth pulls on you")
        text1.scale(0.6)
        text1.to_edge(UP, buff=0.5)
        self.play(FadeIn(text1))
        self.wait(0.8)

        self.play(Create(arrows[0]), run_time=0.8)

        text2 = StyledText("You pull on Earth!")
        text2.scale(0.6)
        text2.next_to(text1, DOWN, buff=0.3)
        text2.set_color(ACCENT_COLOR)
        self.play(FadeIn(text2))
        self.wait(1.5)

        self.play(
            *[FadeOut(mob) for mob in [earth, person, arrows, text1, text2]],
            run_time=0.8
        )

    def room_objects_demo(self):
        """
        Part 4: Multiple objects in a room - SMALL FBD ARROWS
        Lines 64-70: "Zoom out to show multiple objects in a room"
        """
        person = create_simple_person(height=0.8)
        person.shift(LEFT * 2 + DOWN * 0.5)

        phone = create_phone(scale=0.8)
        phone.shift(RIGHT * 2 + UP * 1)

        desk = create_desk(scale=0.8)
        desk.shift(RIGHT * 1.5 + DOWN * 1.5)

        ball = create_ball(radius=0.2, color=ORANGE)
        ball.shift(LEFT * 2.5 + UP * 1.5)

        all_objects = VGroup(person, phone, desk, ball)

        self.play(
            LaggedStart(
                *[FadeIn(obj, scale=0.8) for obj in all_objects],
                lag_ratio=0.2,
                run_time=2
            )
        )
        self.wait(0.5)

        # Small FBD arrows between ALL object pairs
        arrows = VGroup()
        objects_list = [person, phone, desk, ball]

        for i, obj1 in enumerate(objects_list):
            for j, obj2 in enumerate(objects_list):
                if i < j:
                    small_arrows = create_fbd_force_arrows(
                        obj1,
                        obj2,
                        arrow_length=0.4,
                        color=YELLOW,
                        stroke_width=2
                    )
                    small_arrows.set_opacity(0.6)
                    arrows.add(small_arrows)

        self.play(
            LaggedStart(
                *[Create(arrow) for arrow in arrows],
                lag_ratio=0.1,
                run_time=2
            )
        )

        text = StyledText("Everything attracts everything!")
        text.scale(0.7)
        text.to_edge(UP, buff=0.5)
        text.set_color(ACCENT_COLOR)

        self.play(FadeIn(text))
        self.wait(2)

        self.play(FadeOut(text))