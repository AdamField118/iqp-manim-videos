"""
Full Video: Acceleration Due to Gravity (All Scenes Combined)

Scene layout:
- Scene 1: Title Card               (0:00-0:50)   [Manim]
- Scene 2: What Acceleration Is     (0:50-2:20)   [Manim]
- Scene 3: Back to the Cliffhanger  (2:20-3:30)   [Manim]
- Scene 4: Vacuum Tube Demo         (3:30-4:10)   [Live action — no Manim]
- Scene 5: Putting It Together      (4:10-4:50)   [Manim]
- Scene 6: Wrapping Up              (4:50-5:30)   [Manim — end card only]

To render:
    python -m manim -pqh "video_2/full_video.py" FullVideo --media_dir "./video_2/media"
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import BACKGROUND_COLOR

from video_2.scene_1 import Scene1
from video_2.scene_2 import Scene2
from video_2.scene_3 import Scene3
from video_2.scene_5 import Scene5
from video_2.scene_6 import Scene6


class FullVideo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        Scene1.animate_scene(self)
        self.wait(1)

        Scene2.animate_scene(self)
        self.wait(1)

        Scene3.animate_scene(self)
        self.wait(1)

        # Scene 4 is live-action only (vacuum tube demonstration) — no Manim content.

        Scene5.animate_scene(self)
        self.wait(1)

        Scene6.animate_scene(self)