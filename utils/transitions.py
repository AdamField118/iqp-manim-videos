"""
Reusable transition and animation utilities for Manim videos.
These provide a consistent design language across all scenes.
"""

from manim import *


def fade_in_from_bottom(mobject, run_time=1, shift_amount=0.5):
    """
    Fade in a mobject while sliding it up from below.
    
    Args:
        mobject: The Manim object to animate
        run_time: Duration of the animation
        shift_amount: How far down to start (in Manim units)
    
    Returns:
        AnimationGroup of the combined animations
    """
    return AnimationGroup(
        mobject.animate.shift(UP * shift_amount),
        FadeIn(mobject),
        run_time=run_time
    )


def fade_in_with_scale(mobject, run_time=1, start_scale=0.5):
    """
    Fade in a mobject while scaling it from smaller to normal size.
    
    Args:
        mobject: The Manim object to animate
        run_time: Duration of the animation
        start_scale: Starting scale factor (0.5 = half size)
    
    Returns:
        Succession of animations
    """
    mobject.scale(start_scale)
    return Succession(
        AnimationGroup(
            FadeIn(mobject),
            mobject.animate.scale(1/start_scale),
            run_time=run_time
        )
    )


def staggered_fade_in(mobjects, lag_ratio=0.3, run_time=1.5):
    """
    Fade in multiple mobjects with a staggered/cascading effect.
    
    Args:
        mobjects: List of Manim objects to animate
        lag_ratio: Delay between each object (0-1)
        run_time: Total duration of the animation
    
    Returns:
        LaggedStart animation
    """
    return LaggedStart(
        *[FadeIn(mob) for mob in mobjects],
        lag_ratio=lag_ratio,
        run_time=run_time
    )


def slide_in_from_left(mobject, run_time=1, shift_amount=8):
    """
    Slide in a mobject from the left side of the screen.
    
    Args:
        mobject: The Manim object to animate
        run_time: Duration of the animation
        shift_amount: Distance to slide from (in Manim units)
    
    Returns:
        Animation
    """
    mobject.shift(LEFT * shift_amount)
    return mobject.animate.shift(RIGHT * shift_amount).set_run_time(run_time)


def slide_in_from_right(mobject, run_time=1, shift_amount=8):
    """
    Slide in a mobject from the right side of the screen.
    
    Args:
        mobject: The Manim object to animate
        run_time: Duration of the animation
        shift_amount: Distance to slide from (in Manim units)
    
    Returns:
        Animation
    """
    mobject.shift(RIGHT * shift_amount)
    return mobject.animate.shift(LEFT * shift_amount).set_run_time(run_time)


def write_with_glow(mobject, run_time=2, glow_color=YELLOW):
    """
    Write text with a glowing effect.
    
    Args:
        mobject: The text object to animate
        run_time: Duration of the animation
        glow_color: Color of the glow effect
    
    Returns:
        AnimationGroup
    """
    return AnimationGroup(
        Write(mobject, run_time=run_time),
        mobject.animate.set_color(glow_color).set_run_time(run_time * 0.5),
    )


def fade_out_with_shrink(mobject, run_time=0.8, end_scale=0.5):
    """
    Fade out a mobject while shrinking it.
    
    Args:
        mobject: The Manim object to animate
        run_time: Duration of the animation
        end_scale: Final scale factor before disappearing
    
    Returns:
        AnimationGroup
    """
    return AnimationGroup(
        FadeOut(mobject),
        mobject.animate.scale(end_scale),
        run_time=run_time
    )


def typewriter_text(text_object, run_time=2):
    """
    Create a typewriter effect for text.
    
    Args:
        text_object: The text object to animate
        run_time: Duration of the animation
    
    Returns:
        AddTextLetterByLetter animation
    """
    return AddTextLetterByLetter(text_object, run_time=run_time)