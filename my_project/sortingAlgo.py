from manim import *
import random


class SelectionSort(Scene):
    def construct(self):
        text1 = Text("Selection Sort", font="IBM Plex Sans",
                     color="#fafafa", size=4)
        self.play(Write(text1))
        self.wait(2)
        self.play(text1.scale, 0.5, text1.to_edge, UP)
        code = Code(file_name="my_project/code/selectionSort.cpp", background="", style="vscode",
                    font="hack", corner_radius=0.1, tab_width=1, line_no_buff=0.2).to_edge(
            RIGHT, buff=0.8).shift(DOWN / 2)
        coderunner = CodeRunner([1, 1, 3, 1, 1], code)
        a = [[i, None] for i in range(7)]
        random.shuffle(a)
        element = Group()
        for i in range(len(a)):
            rect = Rectangle(
                width=1, height=1 + a[i][0] * 0.5, color=WHITE, fill_opacity=0.3
            )
            a[i][1] = rect
            element.add(rect)
        element.arrange(RIGHT, aligned_edge=DOWN).scale(0.7).to_edge(
            LEFT, buff=0.8
        ).align_to(code, DOWN)
        self.play(
            FadeInFrom(code[0], RIGHT),
            AnimationGroup(*[FadeInFrom(x, DOWN)
                             for x in element], lag_ratio=0.2),
            run_time=1,
        )
        self.play(Write(code.code), Write(code[1]))
        self.wait()
        speed = 0.5
        for i in range(len(a) - 1):
            iMin = i
            self.play(coderunner.runTo(1), run_time=speed)
            self.play(FadeToColor(a[iMin][1], BLUE), run_time=speed)
            self.play(coderunner.runTo(2), run_time=speed)
            for j in range(i + 1, len(a)):
                self.play(
                    FadeToColor(a[j][1], YELLOW,
                                rate_func=there_and_back_with_pause),
                    run_time=speed,
                )
                if a[j][0] <= a[iMin][0]:
                    a[j][1].save_state()
                    self.play(
                        FadeToColor(a[iMin][1], WHITE),
                        FadeToColor(a[j][1], BLUE),
                        run_time=speed / 2,
                    )
                    iMin = j
                else:
                    self.wait(speed / 2)
            a[i], a[iMin] = a[iMin], a[i]
            self.play(coderunner.runTo(3), run_time=speed)
            if i == iMin:
                self.play(FadeToColor(a[i][1], GREEN), run_time=speed * 1.2)
            else:
                self.play(
                    a[i][1].set_x,
                    a[iMin][1].get_x(),
                    a[iMin][1].set_x,
                    a[i][1].get_x(),
                    run_time=speed * 0.8,
                )
                self.play(a[i][1].set_color, GREEN, run_time=speed * 0.4)
        self.play(coderunner.runTo(-1), run_time=speed)
        self.play(FadeToColor(a[-1][1], GREEN), run_time=speed)
        self.wait(2)
        self.play(*[FadeOutAndShift(x, direction=DOWN) for x in self.mobjects])


class BubbleSort(Scene):
    def construct(self):
        text1 = Text("Bubble Sort", font="IBM Plex Sans",
                     color="#fafafa", size=4)
        self.play(Write(text1))
        self.wait(2)
        self.play(text1.scale, 0.5, text1.to_edge, UP)
        code = Code(file_name="my_project/code/bubbleSort.cpp", background="", style="vscode",
                    font="hack", corner_radius=0.1, tab_width=1, line_no_buff=0.2).to_edge(
            RIGHT, buff=0.8).shift(DOWN / 2)
        coderunner = CodeRunner([1, 1, 1, 1, 1], code)

        a = [[i, None] for i in [7, 6, 3, 2, 5, 4, 1]]
        element = Group()
        for i in range(len(a)):
            rect = Rectangle(
                width=1, height=1 + a[i][0] * 0.5, color=WHITE, fill_opacity=0.3
            )
            a[i][1] = rect
            element.add(rect)
        element.arrange(RIGHT, aligned_edge=DOWN).scale(0.7).to_edge(
            LEFT, buff=0.8
        ).align_to(code, DOWN)

        self.play(
            FadeInFrom(code[0], direction=RIGHT),
            AnimationGroup(*[FadeInFrom(x, DOWN)
                             for x in element], lag_ratio=0.2),
            run_time=1,
        )
        self.play(Write(code[1]), Write(code.code))
        self.wait()
        speed = 0.5
        rect = (
            Rectangle(color=YELLOW, fill_opacity=0, width=1.575 + 0.2,
                      height=max(x.get_height() for x in element) + 0.2)
            .align_to(element, DOWN)
            .align_to(element[0], LEFT)
            .shift(LEFT * 0.1 + DOWN * 0.1)
        )
        for i in range(len(a) - 1):
            self.play(coderunner.runTo(0), run_time=speed)
            self.play(FadeToColor(a[-(i + 1)][1], BLUE), run_time=speed / 2)
            for j in range(len(a) - i - 1):
                if (j == 0):
                    self.play(FadeIn(
                        rect.set_x(
                            (a[j][1].get_x() + a[j + 1][1].get_x()) / 2.0)),
                        coderunner.runTo(2), run_time=speed
                    )
                else:
                    self.play(
                        rect.set_x,
                        (a[j][1].get_x() + a[j + 1][1].get_x()) / 2.0,
                        coderunner.runTo(2), run_time=speed
                    )
                if a[j][0] > a[j + 1][0]:
                    self.play(coderunner.runTo(3), run_time=speed)
                    a[j], a[j + 1] = a[j + 1], a[j]
                    if (j == len(a)-i-2):
                        self.play(
                            a[j][1].set_color,
                            WHITE,
                            a[j][1].set_x,
                            a[j + 1][1].get_x(),
                            a[j+1][1].set_color,
                            BLUE,
                            a[j + 1][1].set_x,
                            a[j][1].get_x(),
                            run_time=speed/2,
                        )
                    else:
                        self.play(
                            a[j][1].set_x,
                            a[j + 1][1].get_x(),
                            a[j + 1][1].set_x,
                            a[j][1].get_x(),
                            run_time=speed/2,
                        )
                else:
                    self.wait(speed)
            self.play(a[j+1][1].set_color,
                      GREEN,
                      FadeOut(rect),
                      run_time=speed/2)
        self.play(coderunner.runTo(-1), run_time=speed)
        self.play(FadeToColor(a[0][1], GREEN), run_time=speed / 2)
        self.wait(2)
        self.play(*[FadeOutAndShift(x, direction=DOWN) for x in self.mobjects])
