"""
Scene 1: Title Card - Universal Gravitation

This is the opening title card for Video 1 of the IQP Physics Education project.
The title card introduces the topic "Universal Gravitation" with an elegant animation.

From the transcript (lines 38-40), this scene appears after the live-action hook
where balls are dropped, transitioning into the manim animation portion.
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
    TitleCard,
    create_logo,
    BACKGROUND_COLOR
)


class Scene1(Scene):
    """
    Scene 1: Title Card - "Universal Gravitation"
    
    From PDF transcript lines 38-40:
    [VISUAL: Fade to manim animation]
    [MANIM: Title card with "Universal Gravitation" animates in]
    
    Duration: ~5 seconds total
    
    To render this scene, run:
    python -m manim -pqh "video_1/scene_1.py" Scene1
    """
    
    def construct(self):
        # Set background color
        self.camera.background_color = BACKGROUND_COLOR
        
        # Create the title card - "Universal Gravitation" from PDF
        title_card = TitleCard(
            "Universal Gravitation",
            "Short Video Projects on Physics Education"
        )
        
        # Add logo in bottom right corner
        logo = create_logo(scale=0.2)
        logo.to_corner(DR, buff=0.5)
        
        # Position title card in center
        title_card.move_to(ORIGIN)
        
        # Animation sequence
        # 1. Fade in logo from bottom
        self.play(fade_in_from_bottom(logo, run_time=1))
        self.wait(0.3)
        
        # 2. Animate in the title card elements with stagger
        # Get individual elements from the title card
        if len(title_card) == 3:  # Has title, line, and subtitle
            title_elements = [title_card[0], title_card[1], title_card[2]]
            self.play(staggered_fade_in(title_elements, lag_ratio=0.4, run_time=2))
        else:  # Just title
            self.play(fade_in_with_scale(title_card, run_time=1.5))
        
        # 3. Hold on the title card
        self.wait(2.5)
        
        # 4. Fade out everything before next scene
        self.play(
            FadeOut(title_card),
            FadeOut(logo),
            run_time=1
        )


class Scene1Alternate(Scene):
    """
    Alternative title card with different animation style.
    
    To render this scene, run:
    python -m manim -pqh "video_1/scene_1.py" Scene1Alternate
    """
    
    def construct(self):
        # Set background color
        self.camera.background_color = BACKGROUND_COLOR
        
        # Create the title card
        title_card = TitleCard(
            "Your Video Title",
            "Subtitle Here"
        )
        title_card.move_to(ORIGIN)
        
        # Scale animation entrance
        self.play(fade_in_with_scale(title_card, run_time=1.5, start_scale=0.3))
        self.wait(2.5)
        
        # Optional fade out
        # self.play(FadeOut(title_card), run_time=1)