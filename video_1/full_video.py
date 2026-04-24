"""
Full Video: Universal Gravitation (All Scenes Combined)

This file renders all 5 scenes in sequence to create the complete video.
Each scene's animation logic lives in its own scene file — this file
imports and calls animate_scene() from each one.

Total Duration: ~5 minutes
- Scene 1: Title Card          (0:00-0:45)
- Scene 2: Setting the Stage   (0:45-1:30)
- Scene 3: Newton's Discovery  (1:30-2:45)  ← includes Q1 and Q2
- Scene 4: Connection to Falling (2:45-3:30) ← bridging/preview scene
- Scene 5: Wrapping Up         (3:30-4:15)

Note: Live-action portions are not included here — Manim handles only
the animated segments from the transcript.

To render the full video:
    python -m manim -pqh "video_1/full_video.py" FullVideo --media_dir "./video_1/media"
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import BACKGROUND_COLOR

# Import each scene class so animate_scene() can be called on this scene
from video_1.scene_1 import Scene1
from video_1.scene_2 import Scene2
from video_1.scene_3 import Scene3
from video_1.scene_4 import Scene4
from video_1.scene_5 import Scene5


class FullVideo(Scene):
    """
    Complete Universal Gravitation video with all scenes.

    Calls animate_scene() from each individual scene file so that
    all animation logic stays in one place — the scene files.
    Edits to any scene should be made in the corresponding scene_N.py file.
    """

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        # --- Scene 1: Title Card ---
        Scene1.animate_scene(self)
        self.wait(1)

        # --- Scene 2: Setting the Stage ---
        Scene2.animate_scene(self)
        self.wait(1)

        # --- Scene 3: Newton's Discovery (includes Q1 + Q2) ---
        Scene3.animate_scene(self)
        self.wait(1)

        # --- Scene 4: Connection to Falling (bridging/preview) ---
        Scene4.animate_scene(self)
        self.wait(1)

        # --- Scene 5: Wrapping Up ---
        Scene5.animate_scene(self)