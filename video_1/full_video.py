"""
Full Video: Universal Gravitation (All Scenes Combined)

To render the full video:
    python -m manim -pqh "video_1/full_video.py" FullVideo --media_dir "./video_1/media"
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import BACKGROUND_COLOR

from video_1.scene_1 import Scene1
from video_1.scene_2 import Scene2
from video_1.scene_3 import Scene3
from video_1.scene_5 import Scene5


class FullVideo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        Scene1.animate_scene(self)
        self.wait(1)

        Scene2.animate_scene(self)
        self.wait(1)

        Scene3.animate_scene(self)
        self.wait(1)

        # Scene 4 is live-action only — no Manim content.

        Scene5.animate_scene(self)