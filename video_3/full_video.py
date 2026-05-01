"""
Full Video 3: Beyond Newton -- Einstein's Gravity (All Manim Scenes Combined)

Scene layout (all cut points are approximate; trim to narration in CapCut):
  Scene 1: title card + Newton crack              (0:00 -- ~0:27)
  Scene 2: C.1 sun-instant + fact card + C.2      (0:27 -- ~1:17)
  Scene 3: tidal forces + C.3 + C.4              (1:17 -- ~2:45)
  Scene 4: "Gravity = Curved Spacetime" + C.5 + Wheeler quote  (2:51 -- ~4:05)
  Scene 5: C.6 confirmations + Q2 + examples     (4:05 -- ~4:55)
  Scene 6: Wheeler callback + end card            (4:55 -- end)

To render the full video:
    python -m manim -pqh "video_3/full_video.py" FullVideo --media_dir "./video_3/media"
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import BACKGROUND_COLOR

from video_3.scene_1 import Scene1
from video_3.scene_2 import Scene2
from video_3.scene_3 import Scene3
from video_3.scene_4 import Scene4
from video_3.scene_5 import Scene5
from video_3.scene_6 import Scene6


class FullVideo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        Scene1.animate_scene(self)
        self.wait(1)

        Scene2.animate_scene(self)
        self.wait(1)

        Scene3.animate_scene(self)
        self.wait(1)

        Scene4.animate_scene(self)
        self.wait(1)

        Scene5.animate_scene(self)
        self.wait(1)

        Scene6.animate_scene(self)
