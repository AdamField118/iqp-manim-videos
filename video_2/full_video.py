"""
Full Video: Acceleration Due to Gravity (All Scenes Combined)

Scene layout (based on SRT timestamps):
- 0:00 – 0:31   : Live‑action hook (no Manim)
- 0:31 – 0:50   : Question card (from scene_q1.py)
- 0:50 – 0:55   : Title card (Scene1)
- 0:55 – 2:20   : Scene2
- 2:20 – 3:30   : Scene3
- 3:30 – 4:10   : Live‑action vacuum tube demo (no Manim)
- 4:10 – 4:50   : Scene5
- 4:50 – 5:30   : Scene6

To render:
    python -m manim -pqh "video_2/full_video.py" FullVideo --media_dir "./video_2/media"
"""

import sys
sys.path.append('..')

from manim import *
from utils.objects import BACKGROUND_COLOR

from video_2.scene_1 import Scene1
from video_2.scene_q1 import QuestionCard1
from video_2.scene_2 import Scene2
from video_2.scene_3 import Scene3
from video_2.scene_5 import Scene5
from video_2.scene_6 import Scene6


class FullVideo(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        QuestionCard1.construct(self)

        Scene1.animate_scene(self)

        Scene2.animate_scene(self)

        Scene3.animate_scene(self)

        Scene5.animate_scene(self)

        Scene6.animate_scene(self)