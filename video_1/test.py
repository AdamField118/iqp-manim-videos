from manim import *
import math

class Test(Scene):
    def construct(self):
        line1 = Line(ORIGIN-[3,0,0], ORIGIN+[3,0,0])
        line2 = Line(ORIGIN-[3,0,0], ORIGIN+[3,0,0])
        line3 = Line(ORIGIN-[3,0,0], ORIGIN+[3,0,0])
        circle = Circle(radius=1, color=GREEN)
        self.wait()
        self.play(Create(line1))
        self.play(Create(line2))
        self.play(Create(line3))

        # Fade in and out the indication of a segment before the transformation.
        # 4/5 = x/6
        # x = 6*4/5 = 24/5 = 4.8

        segm1 = Line(ORIGIN-[3,0,0], ORIGIN+[1.8,0,0], color=PURPLE).next_to(line1, DOWN, buff=0.5).shift(LEFT)
        segm2 = Line(ORIGIN+[1.8,0,0], ORIGIN+[3,0,0], color=ORANGE).next_to(segm1, RIGHT, buff=0.5)
        self.play(Transform(line2,segm1))
        self.play(Transform(line3,segm2))


        # I split the line into two segments (with different colours) UP UP UP
        

        # I indicate them with two curly brackets and two letters below
        brace1 = Brace(segm1, color=PURPLE)
        brace2 = Brace(segm2, color=ORANGE)

        text1 = Text("4 real beats", font="Cambria", font_size=24, color=PURPLE).next_to(brace1, DOWN)
        text2 = Text("1 imaginary beat", font="Cambria", font_size=24, color=ORANGE).next_to(brace2, DOWN)

        self.play(FadeIn(brace1, brace2))
        self.play(FadeIn(text1, text2))

        # I fade out all this stuff
        self.play(FadeOut(segm1, segm2, brace1, brace2, text1, text2, line2, line3))

        cp = ComplexPlane(x_length = 3, y_length = 3, x_range = [-1, 1, 1], y_range = [-1, 1, 1],
                          axis_config={
                            "include_tip": True,
                            "tip_length": 0.15,
                            "tip_width": 0.15,
                            },
                        )
        self.play(Create(cp))
        self.play(ReplacementTransform(line1, circle))
        self.play(circle.animate.scale(2), cp.animate.scale(2))
        self.play(circle.animate.shift(RIGHT*2.5), cp.animate.shift(RIGHT*2.5))

        complexFormula = MathTex("\\frac{4+3i}{4}", tex_to_color_map={"\\frac{4+3i}{4}": BLUE}).scale(3).to_edge(DL, buff=1.5)

        radiusU = VMobject()
        cosU = VMobject()
        sinU = VMobject()

        
        sin = DecimalNumber(0, num_decimal_places=3, include_sign=True, unit=None).move_to([-3.5, 2, 0]).set_color(YELLOW)
        sin.add_updater(lambda d: d.set_value(dot.get_center()[1]/2.0))
        cos = DecimalNumber(0, num_decimal_places=3, include_sign=True, unit=None).move_to([-3.5, 1, 0]).set_color(RED)
        cos.add_updater(lambda d: d.set_value(dot.get_center()[0]/2.0-1.250))
        sinText = MathTex("\\sin = ").set_color(YELLOW).next_to(sin, LEFT)
        cosText = MathTex("\\cos = ").set_color(RED).next_to(cos, LEFT)


        dot = Dot(RIGHT*4.5, color=GREEN)

        def dot_position(mobject):
            mobject.set_value(dot.get_center()[1])
            mobject.next_to(dot)

        label = DecimalNumber()
        label.add_updater(dot_position)

        rect1 = SurroundingRectangle(label, color=DARK_BROWN, buff=MED_SMALL_BUFF).set_fill(opacity=1.0)
        rect1.set_z_index(-1)
        rect1.add_updater(dot_position)
        
        self.play(FadeIn(dot, label, cosU, sinU, radiusU, dot, sin, cos, sinText, cosText, rect1))
        self.play(Write(complexFormula))
        self.play(complexFormula.animate.shift(DOWN))

        radiusU.add_updater(lambda x: x.become(Line(circle.get_center(), dot.get_center()).set_color(GRAY)))
        cosU.add_updater(lambda x: x.become(DashedLine([circle.get_center()[0], dot.get_center()[1], 0], [dot.get_center()[0], dot.get_center()[1], 0]).set_color(RED)))
        sinU.add_updater(lambda x: x.become(DashedLine([dot.get_center()[0], 0, 0], [dot.get_center()[0], dot.get_center()[1], 0]).set_color(YELLOW)))
        

        self.play(Rotating(dot, about_point=circle.get_center(), angle=TAU, run_time=TAU, rate_func=linear))
        self.wait()
        self.play(FadeOut(cp, circle, dot, label, cosU, sinU, radiusU, dot, sin, cos, sinText, cosText, complexFormula, rect1))

        text3 = Text("But what am I creating?", color=GREEN, font="Cambria", font_size=72).to_edge(UP)
        icon = SVGMobject(f"D:\\Downloads\\manim_pi_creatures-main\\manim_pi_creatures-main\\PiCreatures_pondering.svg").scale(2).next_to(text3, DOWN*5)

        text4 = Text("Pause and ponder.", color=WHITE, font="Cambria", font_size=36).next_to(icon, DR)

        self.play(Write(text3))
        self.play(DrawBorderThenFill(icon))
        self.play(FadeIn(text4))
        self.wait(2)
        self.play(FadeOut(text3, text4, icon))