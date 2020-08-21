from manim import *
import math

loop = [4, 6, 12, 24, 48, 96, 192, 786432, 50331648]


class Scene2(Scene):
    def construct(self):
        c = Circle(stroke_width=3).to_edge(LEFT).shift(
            RIGHT*2+DOWN/2).set_color(WHITE)
        textn = TexMobject("n =", color=WHITE, font="Arial")
        number = Integer(4, color=WHITE).next_to(textn, RIGHT)
        textn.add(number).next_to(c, UP*8)
        c.scale(2)
        tabledict = {
            TexMobject("n").scale(1.3): [],
            TexMobject("g(x)", color=BLUE).scale(1.3): [],
            TexMobject("f(x)", color=YELLOW).scale(1.3): [],
        }

        table = Table(tabledict=tabledict, line_color=GRAY,
                      raw_string_color=BLUE, hbuff_length=2)
        self.play(ShowCreation(c), Write(textn), Write(
            table.scale(0.5).to_corner(UR)), run_time=2)
        # step by step n
        for k in loop[:4]:
            n = min(k, 50)
            number.set_value(k)
            p = RegularPolygon(n).to_edge(LEFT).shift(RIGHT*2+DOWN/2)
            p2 = RegularPolygon(n, color=YELLOW).to_edge(
                LEFT).shift(RIGHT*2+DOWN/2)
            p2.scale(2 / math.cos(2 * PI / (n * 2)))
            p.scale(2)
            if (k == 4):
                p.rotate(PI/4)
                p2.rotate(PI/4)
            self.play(Indicate(textn), ShowCreation(
                p), ShowCreation(p2))

            c1 = Integer(k).scale(0.6)
            c2 = DecimalNumber(
                k*math.tan(2*PI / (2*k)), num_decimal_places=11, color=YELLOW).scale(0.6)
            c3 = DecimalNumber(
                k*math.sin(2*PI / (2*k)), num_decimal_places=11, color=BLUE).scale(0.6)

            table.add_record(record=c1, field_num=0)
            table.add_record(
                record=c2, field_num=2)
            table.add_record(
                record=c3, field_num=1)
            self.play(
                table.adjust_lines(),
                TransformFromCopy(number, c1),
                TransformFromCopy(p, c2),
                TransformFromCopy(p2, c3))
            self.play(FadeToColor(c2, WHITE),
                      FadeToColor(c3, WHITE), VFadeOut(p), VFadeOut(p2))

        # a lot of n
        p = RegularPolygon(100, color=GREEN).to_edge(
            LEFT).shift(RIGHT*2+DOWN/2)
        p.scale(2)

        tess = []
        for k in loop[4:]:
            c1 = Integer(k).scale(0.6)
            c2 = DecimalNumber(
                k*math.tan(2*PI / (2*k)), num_decimal_places=11, color=WHITE).scale(0.6)
            c3 = DecimalNumber(
                k*math.sin(2*PI / (2*k)), num_decimal_places=11, color=WHITE).scale(0.6)
            tess += [
                AnimationGroup(
                    Write(table.add_record(record=c1, field_num=0)),
                    Write(table.add_record(
                        record=c2, field_num=2)),
                    Write(table.add_record(
                        record=c3, field_num=1)),
                    table.adjust_lines(), lag_ratio=0),
            ]

        self.play(
            textn.shift, LEFT,
            ChangeDecimalToValue(number, loop[-1]),
            ShowCreation(p),
            LaggedStart(*tess, lag_ratio=0.2),
            run_time=5
        )
        self.play(
            Write(table.add_record(record=Text(
                "...", font="Arial").scale(0.6), field_num=0)),
            Write(table.add_record(record=Text(
                "...", font="Arial").scale(0.6), field_num=1)),
            Write(table.add_record(record=Text(
                "...", font="Arial").scale(0.6), field_num=2)),
            table.adjust_lines(),
        )
        self.wait(5)
        self.play(FadeOutAndShift(table, direction=DOWN),
                  FadeOutAndShift(c, direction=DOWN),
                  FadeOutAndShift(p, direction=DOWN),
                  FadeOutAndShift(p2, direction=DOWN),
                  FadeOutAndShift(textn, direction=DOWN),
                  )
        self.wait()


class Scene1(Scene):
    def construct(self):
        text = TextMobject(
            "Consider a regular n-sided polygon outside circle").to_edge(UP)
        self.play(Write(text))
        circle = Circle().scale(2).to_edge(LEFT).set_color(WHITE)
        p = RegularPolygon(6, color=YELLOW).next_to(circle, ORIGIN).scale(
            2 / math.cos(2*PI / (6 * 2)))
        textO = TextMobject("O", color=YELLOW).scale(
            0.6).next_to(circle.get_center(), DOWN)
        self.play(ShowCreation(circle), ShowCreation(p), Write(
            textO), ShowCreation(Dot(circle.get_center(), radius=0.04)))
        self.wait()
        pA = p.get_top()
        pC = p.get_all_points()[4]
        lineA = Line(p.get_center(), pA, color=YELLOW)
        lineC = Line(p.get_center(), pC, color=YELLOW)
        textA = TextMobject("A", color=YELLOW).scale(0.6).next_to(pA, UP)
        textC = TextMobject("C", color=YELLOW).scale(0.6).next_to(pC, UP)
        square = Square(side_length=0.25, color=YELLOW).move_to(pA, UP + LEFT)
        angle = Arc(start_angle=lineC.get_angle(), radius=0.4, color=YELLOW,
                    angle=lineA.get_angle() - lineC.get_angle(), arc_center=p.get_center())

        text1 = TextMobject(
            "Let $f(n)=$ perimeter of the regular n-gon").scale(0.8).to_corner(UR).shift(DOWN)
        self.play(Write(text1))
        self.play(ShowCreation(lineA), ShowCreation(
            lineC), ShowCreation(
            square), ShowCreation(
            angle), FadeInFrom(textA, dirction=DOWN),
            FadeInFrom(textC, dirction=DOWN))
        text2 = TexMobject(
            "f(n)", "=", "2", "n", "AC").scale(0.8).next_to(text1, DOWN).align_to(text1, LEFT)
        self.play(Write(text2), ShowCreationThenFadeOut(
            p.copy().set_color(BLUE)))
        text3 = TexMobject(
            "AO=\\frac{d}{2}=\\frac{1}{2}", ", ", "\widehat{AOC}=\\frac{360}{2n}").scale(0.8).next_to(text2, DOWN).align_to(text1, LEFT)
        self.play(Write(text3[0]), Write(text3[1]), ShowCreationThenFadeOut(
            lineA.copy().set_color(BLUE)))
        self.play(Write(text3[2]),
                  ShowCreationThenFadeOut(
            lineA.copy().set_color(BLUE)),
            ShowCreationThenFadeOut(
            lineC.copy().set_color(BLUE)),
            ShowCreationThenFadeOut(
            angle.copy().set_color(BLUE)))
        text4 = TexMobject("AC", "=", "AO", "\\tan{\widehat{AOC}}", "=", "\\frac{1}{2}\\tan{\\frac{360}{2n}}").scale(0.8).next_to(
            text3, DOWN).align_to(text3, LEFT)
        self.play(*[Write(t) for t in text4[:4]], ShowCreationThenFadeOut(
            Line(pA, pC).set_color(BLUE)))
        self.play(*[Write(t) for t in text4[4:]])
        self.wait()
        #"f(n)", "=", "2n", "AC"
        text5 = text2.copy().scale(1.4).next_to(text4, DOWN*2.5).align_to(text1, LEFT)
        self.play(TransformFromCopy(text2, text5))
        self.wait()
        self.play(
            Transform(text5[-1], TexMobject("\\frac{1}{2}", "\\tan{\\frac{360}{2n}}").scale(1.2).next_to(text5[-2], RIGHT).shift(UP*0.08)))
        self.play(
            FadeOut(text5[2]),
            FadeOut(text5[-1][0]),
        )
        self.play(
            text5[3].next_to, text5[1],
            text5[-1][1].next_to, text5[1].get_center()+UP*0.07 +
            RIGHT*3/5
        )
        self.wait(3)
        self.play(*[FadeOutAndShift(m, direction=DOWN) for m in self.mobjects])
        self.remove(*[m for m in self.mobjects])


class Scene1_2(Scene):
    def construct(self):
        text = TextMobject(
            "Consider a regular n-sided polygon inside circle").to_edge(UP)
        self.play(Write(text))
        circle = Circle().scale(2).to_edge(LEFT).set_color(WHITE)
        p = RegularPolygon(6, color=BLUE).next_to(circle, ORIGIN).scale(2)
        textO = TextMobject("O", color=BLUE).scale(
            0.6).next_to(circle.get_center(), DOWN)
        self.play(ShowCreation(circle), ShowCreation(p), Write(
            textO), ShowCreation(Dot(circle.get_center(), radius=0.04)))
        self.wait()
        pA = p.get_top()
        pC = p.get_all_points()[4]
        lineA = Line(p.get_center(), pA, color=BLUE)
        lineC = Line(p.get_center(), pC, color=BLUE)
        textA = TextMobject("A", color=BLUE).scale(0.6).next_to(pA, UP)
        textC = TextMobject("C", color=BLUE).scale(0.6).next_to(pC, UP)
        square = Square(side_length=0.25, color=BLUE).move_to(pA, UP + LEFT)
        angle = Arc(start_angle=lineC.get_angle(), radius=0.4, color=BLUE,
                    angle=lineA.get_angle() - lineC.get_angle(), arc_center=p.get_center())

        text1 = TextMobject(
            "Let $g(n)=$ perimeter of the regular n-gon").scale(0.8).to_corner(UR).shift(DOWN)
        self.play(Write(text1))
        self.play(ShowCreation(lineA), ShowCreation(
            lineC), ShowCreation(
            square), ShowCreation(
            angle), FadeInFrom(textA, dirction=DOWN),
            FadeInFrom(textC, dirction=DOWN))
        text2 = TexMobject(
            "g(n)", "=", "2", "n", "AC").scale(0.8).next_to(text1, DOWN).align_to(text1, LEFT)
        self.play(Write(text2), ShowCreationThenFadeOut(
            p.copy().set_color(YELLOW)))
        text3 = TexMobject(
            "OC=\\frac{d}{2}=\\frac{1}{2}", ", ", "\widehat{AOC}=\\frac{360}{2n}").scale(0.8).next_to(text2, DOWN).align_to(text1, LEFT)
        self.play(Write(text3[0]), Write(text3[1]), ShowCreationThenFadeOut(
            lineC.copy().set_color(YELLOW)))
        self.play(Write(text3[2]),
                  ShowCreationThenFadeOut(
            lineA.copy().set_color(YELLOW)),
            ShowCreationThenFadeOut(
            lineC.copy().set_color(YELLOW)),
            ShowCreationThenFadeOut(
            angle.copy().set_color(YELLOW)))
        text4 = TexMobject("AC", "=", "OC", "\\sin{\widehat{AOC}}", "=", "\\frac{1}{2}\\sin{\\frac{360}{2n}}").scale(0.8).next_to(
            text3, DOWN).align_to(text3, LEFT)
        self.play(*[Write(t) for t in text4[:4]],
                  ShowCreationThenFadeOut(
            Line(pA, pC).set_color(YELLOW)))
        self.play(*[Write(t) for t in text4[4:]])
        self.wait()
        #"f(n)", "=", "2n", "AC"
        text5 = text2.copy().scale(1.4).next_to(text4, DOWN*2.5).align_to(text1, LEFT)
        self.play(TransformFromCopy(text2, text5))
        self.wait()
        self.play(
            Transform(text5[-1], TexMobject("\\frac{1}{2}", "\\sin{\\frac{360}{2n}}").scale(1.2).next_to(text5[-2], RIGHT).shift(UP*0.08)))
        self.play(
            FadeOut(text5[2]),
            FadeOut(text5[-1][0]),
        )
        self.play(
            text5[3].next_to, text5[1],
            text5[-1][1].next_to, text5[1].get_center()+UP*0.07 +
            RIGHT*3/5
        )
        self.wait(3)
        self.play(*[FadeOutAndShift(m, direction=DOWN) for m in self.mobjects])
        self.remove(*[m for m in self.mobjects])


class Scene1_3(Scene):
    def construct(self):
        tex = TexMobject("g(n)", "\leq", "\pi", "\leq", "f(n)")
        tex[-1].set_color(YELLOW)
        tex[0].set_color(BLUE)
        self.play(Write(tex.scale(1.3)))
        self.wait(2)
        self.play(tex[0].become, TexMobject(
            "\lim_{n\\to\infty} g(n)").set_color(BLUE).next_to(tex[1], LEFT).scale(1.3).shift(LEFT),
            tex[-1].become, TexMobject(
            "\lim_{n\\to\infty} f(n)").set_color(YELLOW).next_to(tex[-2], RIGHT).scale(1.3).shift(RIGHT),
        )
        self.wait(2)
        self.play(tex[0].become, TexMobject(
            "\lim_{n\\to\infty} n\\sin\\bigg(\\frac{360}{2n}\\bigg)").set_color(BLUE).next_to(tex[1], LEFT).scale(1.3).shift(LEFT),
            tex[-1].become, TexMobject(
            "\lim_{n\\to\infty} n\\tan\\bigg(\\frac{360}{2n}\\bigg)").set_color(YELLOW).next_to(tex[-2], RIGHT).scale(1.3).shift(RIGHT),
        )
        self.wait(4)
        self.play(*[FadeOutAndShift(m, direction=DOWN) for m in self.mobjects])


class Scene0(Scene):
    def construct(self):
        # part 1
        tex = TexMobject(
            "\pi=", "{circumference", "\\over", "diameter}").scale(2)
        self.play(Write(tex), run_time=2)
        self.wait(3)

        circle = Circle().scale(3).to_edge(LEFT).set_color(WHITE)
        line = Line(circle.get_left(), circle.get_right())
        self.play(ShowCreation(circle),
                  ShowCreation(line),
                  tex.scale, 0.5,
                  tex.to_corner, UR,
                  tex.shift, LEFT)
        self.wait()
        self.play(Indicate(tex[1], color=GREEN), FadeToColor(
            circle, GREEN, rate_func=there_and_back),
            run_time=2
        )
        self.play(
            Indicate(tex[3], color=ORANGE), FadeToColor(
                line, ORANGE, rate_func=there_and_back),
            run_time=2
        )
        self.play(Transform(tex, TexMobject(
            "\pi=", "{C", "\\over", "d}").move_to(tex)))
        text1 = TextMobject("Assume $d=1$").next_to(tex, DOWN)
        self.play(FadeInFrom(text1, direction=DOWN))
        self.play(Swap(text1, tex))
        tex2 = TexMobject(
            "\pi=", "{C", "\\over", "d}", "=", "\\frac{C}{1}", "=", "C").move_to(tex)
        self.play(*[ReplacementTransform(tx, ty)
                    for (tx, ty) in zip(tex, tex2)])
        self.play(*[Write(x) for x in tex2[4:]])
        self.wait()
        self.play(Transform(tex2, TexMobject(
            "\pi=", "C").move_to(tex2)))
        self.play(Indicate(tex2, color=GREEN), FadeToColor(
            circle, GREEN, rate_func=there_and_back), run_time=2)
        squareOT = TextMobject(
            "Consider a regular 4-sided polygon outside circle").next_to(tex2, DOWN).scale(0.6).to_edge(RIGHT)
        squareO = Square().move_to(circle).scale(3).set_color(YELLOW)
        self.play(Write(squareOT))
        perimeterOT = TextMobject(
            "$perimeter=1*4=4$", color=YELLOW).next_to(squareOT, DOWN)
        self.play(Write(perimeterOT),
                  ShowCreation(squareO))

        squareIT = TextMobject(
            "Consider a regular 4-sided polygon inside circle").next_to(perimeterOT, DOWN).scale(0.6).to_edge(RIGHT)
        self.play(Write(squareIT))
        squareI = Square().move_to(circle).scale(3*math.sqrt(1/2)).set_color(BLUE)
        perimeterIT = TexMobject(
            "perimeter=\\frac{\sqrt{2}}{2}*4", "=", "2\sqrt{2}", color=BLUE).next_to(squareIT, DOWN)
        self.play(Write(perimeterIT), ShowCreation(squareI))
        self.play(
            Transform(perimeterIT[-2], TexMobject(
                "\\approx", color=BLUE).move_to(perimeterIT[-2])),
            Transform(perimeterIT[-1], TexMobject(
                "2.82", color=BLUE).move_to(perimeterIT[-1])))
        self.wait()
        ketluan = TexMobject("\Rightarrow", "2.82", "\leq", "\pi", "\leq",
                             "4").scale(1.5).next_to(perimeterIT, DOWN)
        ketluan[1].set_color(BLUE)
        ketluan[-1].set_color(YELLOW)
        self.play(Write(ketluan))
        self.wait(2)
        self.play(*[FadeOutAndShift(m, direction=DOWN) for m in self.mobjects])


class FinalScene(Scene):
    def construct(self):
        Scene0.construct(self)
        Scene1.construct(self)
        Scene1_2.construct(self)
        Scene1_3.construct(self)
        Scene2.construct(self)
