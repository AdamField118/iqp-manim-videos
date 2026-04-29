"""
utils/question_utils.py

Provides a red octagon PAUSE sign that pops in during question thinking
pauses and shrinks away before the answer. Drop into utils/ alongside
objects.py and transitions.py.

Usage:
    from utils.question_utils import show_stop_sign

    self.play(Write(question_text, run_time=2))
    show_stop_sign(self, thinking_seconds=3.5)
    # then show answer
"""

from manim import *

STOP_RED = "#c0392b"


def show_stop_sign(scene, thinking_seconds=3.5, position=DOWN * 1.8):
    """
    Pop a red octagon PAUSE sign in, hold for thinking_seconds, shrink away.

    Parameters
    ----------
    scene            : the Manim Scene instance (pass `self`)
    thinking_seconds : how long the sign holds before disappearing
    position         : where to place the sign (default lower-centre)
    """
    octagon = RegularPolygon(
        n=8,
        radius=0.9,
        color=STOP_RED,
        fill_color=STOP_RED,
        fill_opacity=1.0,
        stroke_color=WHITE,
        stroke_width=5,
    )
    inner = RegularPolygon(
        n=8,
        radius=0.76,
        fill_opacity=0.0,
        stroke_color=WHITE,
        stroke_width=2,
    )
    pause_text = Text("PAUSE", font_size=28, color=WHITE, weight=BOLD)
    here_text  = Text("HERE",  font_size=28, color=WHITE, weight=BOLD)
    here_text.next_to(pause_text, DOWN, buff=0.04)
    label = VGroup(pause_text, here_text).move_to(octagon.get_center())

    sign = VGroup(octagon, inner, label)
    sign.move_to(position)

    scene.play(GrowFromCenter(sign), run_time=0.4)
    scene.wait(thinking_seconds)
    scene.play(ShrinkToCenter(sign), run_time=0.4)