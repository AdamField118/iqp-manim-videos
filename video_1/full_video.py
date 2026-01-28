"""
Full Video: Universal Gravitation (All Scenes Combined)

This file renders all 5 scenes in sequence to create the complete video.

Total Duration: ~5 minutes (300 seconds)
- Scene 1: Title Card (0:00-0:45) - 6 seconds
- Scene 2: Setting the Stage (0:45-1:30) - 45 seconds  
- Scene 3: Newton's Discovery (1:30-2:30) - 60 seconds (now includes Question 1)
- Scene 4: Solving the Mystery (2:30-3:45) - 75 seconds
- Scene 5: Wrapping Up (3:45-4:30) - 45 seconds

Note: The live-action portions are not included in these Manim scenes.
This is only the animated portions from the transcript.

To render the full video:
python -m manim -pqh "video_1/full_video.py" FullVideo --media_dir "./video_1/media"
"""

import sys
sys.path.append('..')

from manim import *
from utils.transitions import *
from utils.objects import *
from utils.physics_objects import *


class FullVideo(Scene):
    """
    Complete Universal Gravitation video with all scenes.
    
    This combines Scene 1 through Scene 5 into one continuous animation.
    Each scene is separated by brief transitions.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Render all scenes in sequence
        self.scene_1_title_card()
        self.wait(1)  # Brief pause between scenes
        
        self.scene_2_setting_the_stage()
        self.wait(1)
        
        self.scene_3_newtons_discovery()
        self.wait(1)
        
        self.scene_4_solving_mystery()
        self.wait(1)
        
        self.scene_5_wrapping_up()
    
    def scene_1_title_card(self):
        """Scene 1: Title Card"""
        # Add persistent logo
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        
        # Title card
        title_card = TitleCard(
            "Universal Gravitation",
            "Short Video Projects on Physics Education"
        )
        title_card.move_to(ORIGIN)
        
        # Animations
        self.play(fade_in_from_bottom(logo, run_time=1))
        self.wait(0.3)
        
        if len(title_card) == 3:
            title_elements = [title_card[0], title_card[1], title_card[2]]
            self.play(staggered_fade_in(title_elements, lag_ratio=0.4, run_time=2))
        
        self.wait(2.5)
        
        self.play(FadeOut(title_card), run_time=1)
        
        # Keep logo for rest of video
        self.logo = logo
    
    def scene_2_setting_the_stage(self):
        """Scene 2: Setting the Stage - Gravity is universal (UPDATED WITH TENNIS BALL + FBD ARROWS)"""
        
        # Two masses with attraction - FBD ARROWS
        # Create DISTINCTLY DIFFERENT masses
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
        
        mass2_circle = Circle(
            radius=0.4,
            fill_color=RED_C,
            fill_opacity=0.8,
            stroke_color=RED_E,
            stroke_width=3
        )
        # Add stripes to mass2 for distinction
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
        
        mass1.shift(LEFT * 2.5)
        mass2.shift(RIGHT * 2.5)
        
        self.play(
            fade_in_with_scale(mass1, start_scale=0.3),
            fade_in_with_scale(mass2, start_scale=0.3)
        )
        
        # Use FBD-style arrows (fixed length, from centers)
        arrows = create_fbd_force_arrows(
            mass1, 
            mass2, 
            arrow_length=1.2,
            color=YELLOW,
            stroke_width=5
        )
        self.play(Create(arrows))
        
        text = StyledText("Gravity = Universal Force")
        text.scale(0.7)
        text.to_edge(UP, buff=0.5)
        self.play(Write(text))
        
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in [mass1, mass2, arrows, text]])
    
    def scene_3_newtons_discovery(self):
        """Scene 3: Newton's Big Discovery - The equation"""
        
        title = StyledTitle("Newton's Law")
        title.scale(0.6)
        title.to_edge(UP, buff=0.5)
        
        equation = MathTex(
            "F = G \\frac{m_1 m_2}{r^2}",
            font_size=72
        )
        
        self.play(Write(title))
        self.play(FadeIn(equation, scale=1.2))
        
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in [title, equation]])
    
    def scene_4_solving_mystery(self):
        """Scene 4: Solving the Mystery - Mass cancellation (UPDATED WITH ALIGNED CROSSES)"""
        
        title = StyledText("The Beautiful Truth")
        title.scale(0.8)
        title.to_edge(UP, buff=0.3)
        title.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(title))
        
        # Show cancellation - UPDATED VERSION WITH PROPER ALIGNMENT
        # Create equation as complete valid LaTeX, using substrings for the m's
        combined = MathTex(
            "G", "{M_{Earth}", "m", "\\over", "r^2}", "=", "m", "a",
            font_size=64
        )
        
        self.play(Write(combined))
        self.wait(1)
        
        # Get exact submobjects for the m's
        m1_submobject = combined[2]  # First m (in numerator)
        m2_submobject = combined[6]  # Second m (right side of =)
        
        # Create boxes that EXACTLY surround the m's
        m1_box = SurroundingRectangle(
            m1_submobject,
            color=RED,
            stroke_width=3,
            buff=0.1
        )
        
        m2_box = SurroundingRectangle(
            m2_submobject,
            color=RED,
            stroke_width=3,
            buff=0.1
        )
        
        self.play(
            Create(m1_box),
            Create(m2_box),
            run_time=0.8
        )
        
        # Cross out both m's with X marks - PERFECTLY ALIGNED
        cross1 = VGroup(
            Line(m1_box.get_corner(DL), m1_box.get_corner(UR), color=RED, stroke_width=4),
            Line(m1_box.get_corner(UL), m1_box.get_corner(DR), color=RED, stroke_width=4)
        )
        cross2 = VGroup(
            Line(m2_box.get_corner(DL), m2_box.get_corner(UR), color=RED, stroke_width=4),
            Line(m2_box.get_corner(UL), m2_box.get_corner(DR), color=RED, stroke_width=4)
        )
        
        self.play(Create(cross1), Create(cross2))
        self.wait(1)
        
        # Result
        result = MathTex("a = G\\frac{M_{Earth}}{r^2}", font_size=72)
        result.shift(DOWN * 1.5)
        
        self.play(
            FadeOut(combined),
            FadeOut(m1_box),
            FadeOut(m2_box),
            FadeOut(cross1),
            FadeOut(cross2),
            run_time=0.5
        )
        
        self.play(Write(result))
        
        insight = StyledText("Mass cancels out!")
        insight.scale(0.6)
        insight.next_to(result, DOWN, buff=0.5)
        self.play(FadeIn(insight))
        
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in [title, result, insight]])
    
    def scene_5_wrapping_up(self):
        """Scene 5: Wrapping Up - Review and preview"""
        
        # End card
        large_logo = create_logo(scale=0.4)
        large_logo.shift(UP * 1.2)
        
        project_title = StyledTitle("Short Video Projects")
        project_title.scale(0.6)
        project_title.next_to(large_logo, DOWN, buff=0.8)
        
        subtitle = StyledText("Physics Education Series")
        subtitle.scale(0.6)
        subtitle.next_to(project_title, DOWN, buff=0.3)
        
        thanks = StyledText("Thanks for watching!")
        thanks.scale(0.7)
        thanks.shift(DOWN * 1.8)
        thanks.set_color(ACCENT_COLOR)
        
        self.play(FadeIn(large_logo, scale=0.8))
        self.play(Write(project_title), FadeIn(subtitle))
        self.play(FadeIn(thanks))
        
        self.wait(3)


class QuickPreview(Scene):
    """
    A 30-second preview showing key moments from each scene.
    Useful for testing or creating a trailer.
    
    To render:
    python -m manim -pqh "video_1/full_video.py" QuickPreview
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Logo
        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)
        
        # Quick hits from each scene
        scenes_text = [
            "Universal Gravitation",
            "Gravity is Universal",
            "Newton's Law: F = Gm₁m₂/r²",
            "Mass Cancels Out!",
            "All Objects Fall at Same Rate"
        ]
        
        for text_content in scenes_text:
            text = StyledText(text_content)
            text.scale(0.8)
            
            if "Cancel" in text_content or "Same Rate" in text_content:
                text.set_color(ACCENT_COLOR)
            
            self.play(FadeIn(text, scale=1.2), run_time=0.8)
            self.wait(1)
            self.play(FadeOut(text), run_time=0.5)
        
        # End
        end_text = StyledTitle("Coming Soon")
        end_text.scale(0.7)
        end_text.set_color(ACCENT_COLOR)
        
        self.play(Write(end_text))
        self.wait(2)


class TestFBDArrows(Scene):
    """
    Quick test scene to verify FBD arrows are working.
    
    To render:
    python -m manim -pql "video_1/full_video.py" TestFBDArrows
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Create two distinct masses
        mass1_circle = Circle(radius=0.6, fill_color=BLUE, fill_opacity=0.7, stroke_color=BLUE_E, stroke_width=3)
        mass1_label = MathTex("m_1", font_size=42, color=WHITE)
        mass1_label.move_to(mass1_circle.get_center())
        mass1 = VGroup(mass1_circle, mass1_label)
        
        mass2_circle = Circle(radius=0.4, fill_color=RED_C, fill_opacity=0.8, stroke_color=RED_E, stroke_width=3)
        stripe1 = Line(mass2_circle.get_top() + LEFT * 0.3, mass2_circle.get_bottom() + LEFT * 0.1, color=ORANGE, stroke_width=2)
        stripe2 = Line(mass2_circle.get_top() + RIGHT * 0.1, mass2_circle.get_bottom() + RIGHT * 0.3, color=ORANGE, stroke_width=2)
        mass2_label = MathTex("m_2", font_size=36, color=WHITE)
        mass2_label.move_to(mass2_circle.get_center())
        mass2 = VGroup(mass2_circle, stripe1, stripe2, mass2_label)
        
        mass1.shift(LEFT * 3)
        mass2.shift(RIGHT * 2.5)
        
        # Create FBD arrows
        arrows = create_fbd_force_arrows(mass1, mass2, arrow_length=1.2, color=YELLOW, stroke_width=5)
        
        # Add label
        label = Text("FBD-Style Arrows", font_size=36, color=WHITE)
        label.to_edge(UP, buff=0.5)
        
        self.add(mass1, mass2, arrows, label)
        self.wait(2)


class TestAlignedCancellation(Scene):
    """
    Quick test scene to verify aligned mass cancellation.
    
    To render:
    python -m manim -pql "video_1/full_video.py" TestAlignedCancellation
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Create equation using \over for proper indexing
        eq = MathTex(
            "G", "{M_{Earth}", "m", "\\over", "r^2}", "=", "m", "a",
            font_size=64
        )
        
        # Get exact submobjects
        m1 = eq[2]  # First m (in numerator)
        m2 = eq[6]  # Second m (right side)
        
        # Create perfectly fitted boxes
        m1_box = SurroundingRectangle(m1, color=RED, buff=0.1, stroke_width=3)
        m2_box = SurroundingRectangle(m2, color=RED, buff=0.1, stroke_width=3)
        
        # Create aligned crosses
        cross1 = VGroup(
            Line(m1_box.get_corner(DL), m1_box.get_corner(UR), color=RED, stroke_width=4),
            Line(m1_box.get_corner(UL), m1_box.get_corner(DR), color=RED, stroke_width=4)
        )
        cross2 = VGroup(
            Line(m2_box.get_corner(DL), m2_box.get_corner(UR), color=RED, stroke_width=4),
            Line(m2_box.get_corner(UL), m2_box.get_corner(DR), color=RED, stroke_width=4)
        )
        
        # Add label
        label = Text("Perfectly Aligned Cancellation", font_size=36, color=WHITE)
        label.to_edge(UP, buff=0.5)
        
        self.add(eq, m1_box, m2_box, cross1, cross2, label)
        self.wait(2)