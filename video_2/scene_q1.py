"""
video_2/scene_q1.py
Question 1 card — standalone clip for CapCut insertion.

Drop this into the timeline immediately after the live-action moment
where the presenter asks "what was its acceleration?" and let it run
through the thinking pause.
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import StyledText, create_logo, BACKGROUND_COLOR, ACCENT_COLOR
from utils.question_utils import show_stop_sign


class QuestionCard1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        logo = create_logo(scale=0.15)
        logo.to_corner(DR, buff=0.3)
        self.add(logo)

        # Same text style as Video 1
        question_title = StyledText("Question:")
        question_title.scale(0.8).to_edge(UP, buff=0.5).set_color(ACCENT_COLOR)
        self.play(FadeIn(question_title))

        question_text = StyledText(
            "At the very top of that throw —\n"
            "the instant the ball was hanging in the air —\n"
            "what was its acceleration?"
        )
        question_text.scale(0.65).next_to(question_title, DOWN, buff=0.5)
        self.play(Write(question_text, run_time=2))

        show_stop_sign(self, thinking_seconds=3.5)

        self.play(FadeOut(question_title), FadeOut(question_text), run_time=0.5)
        self.wait(0.3)