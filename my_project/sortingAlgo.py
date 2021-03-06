from manim import *
import random


class SelectionSort(Scene):
    def construct(self):
        text1 = Text("Selection Sort", font="IBM Plex Sans",
                     color="#fafafa", size=4)
        self.play(Write(text1))
        self.wait(2)
        self.play(text1.scale, 0.5, text1.to_edge, UP)
        code = Code(file_name="my_project/code/selectionSort_1.cpp",
                    style="vscode").to_edge(RIGHT, buff=0.8).shift(DOWN/2)
        coderunner = CodeRunner([1]*8, code)
        self.play(FadeInFrom(code[0], RIGHT))
        self.play(Write(code[1]), Write(code.code))
        a = [[i, None] for i in [5, 4, 1, 6, 2, 0, 3]]
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
        self.play(coderunner.runTo(3), run_time=0.5)
        self.play(coderunner.runTo(4), run_time=0.5)
        self.play(
            AnimationGroup(*[FadeInFrom(x, DOWN)
                             for x in element], lag_ratio=0.2),
            run_time=1,
        )
        self.play(coderunner.runTo(5))
        code2 = Code(file_name="my_project/code/selectionSort_2.cpp",
                     style="vscode").align_to(code, DOWN+LEFT)
        code2.add(CodeRunner([1, 1, 1, 3, 1, 1], code2))
        self.play(FadeInFrom(code2, direction=UP),
                  FadeOutAndShift(code, direction=DOWN))
        code = code2
        coderunner = code2[-1]
        speed = 0.5
        for i in range(len(a) - 1):
            iMin = i
            self.play(coderunner.runTo(2), run_time=speed)
            self.play(FadeToColor(a[iMin][1], BLUE), run_time=speed)
            self.play(coderunner.runTo(3), run_time=speed)
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
            self.play(coderunner.runTo(4), run_time=speed)
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

        code = Code(file_name="my_project/code/bubbleSort_1.cpp",
                    style="vscode").to_edge(RIGHT, buff=0.8).shift(DOWN/2)
        coderunner = CodeRunner([1]*8, code)
        code.add(coderunner)
        self.play(FadeInFrom(code[0], RIGHT))
        self.play(Write(code[1]), Write(code.code))
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
        self.play(coderunner.runTo(3), run_time=0.5)
        self.play(coderunner.runTo(4), run_time=0.5)
        self.play(
            AnimationGroup(*[FadeInFrom(x, DOWN)
                             for x in element], lag_ratio=0.2),
            run_time=1,
        )
        self.play(coderunner.runTo(5))
        code2 = Code(file_name="my_project/code/bubbleSort_2.cpp",
                     style="vscode").align_to(code, DOWN+LEFT)
        code2.add(CodeRunner([1]*7, code2))
        self.play(FadeInFrom(code2, direction=UP),
                  FadeOutAndShift(code, direction=DOWN))
        code = code2
        coderunner = code2[-1]
        speed = 0.5
        rect = (
            Rectangle(color=YELLOW, fill_opacity=0, width=1.575 + 0.2,
                      height=max(x.get_height() for x in element) + 0.2)
            .align_to(element, DOWN)
            .align_to(element[0], LEFT)
            .shift(LEFT * 0.1 + DOWN * 0.1)
        )
        for i in range(len(a) - 1):
            self.play(coderunner.runTo(1), run_time=speed)
            self.play(FadeToColor(a[-(i + 1)][1], BLUE), run_time=speed / 2)
            for j in range(len(a) - i - 1):
                if (j == 0):
                    self.play(FadeIn(
                        rect.set_x(
                            (a[j][1].get_x() + a[j + 1][1].get_x()) / 2.0)),
                        coderunner.runTo(3), run_time=speed
                    )
                else:
                    self.play(
                        rect.set_x,
                        (a[j][1].get_x() + a[j + 1][1].get_x()) / 2.0,
                        coderunner.runTo(3), run_time=speed
                    )
                if a[j][0] > a[j + 1][0]:
                    self.play(coderunner.runTo(4), run_time=speed)
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


class CallStack(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.add(Text("CallStack", font='Hack', size=0.8))
        self.add(BackgroundRectangle(self, color=WHITE, buff=0.3,
                                     fill_opacity=0, stroke_width=3, stroke_opacity=1))
        self.add(
            Line(ORIGIN, DOWN*7, stroke_width=3).align_to(self, LEFT+DOWN))
        self.add(
            Line(ORIGIN, DOWN*7, stroke_width=3).align_to(self, RIGHT+DOWN))
        self.length = 0

    def push(self, text):
        t = Text(text, size=0.4,
                 font='Hack')
        t.add_to_back(Rectangle(color=WHITE, fill_opacity=0,
                                stroke_width=3, stroke_opacity=1, width=self[1].get_width(), height=t.get_height()+0.4).move_to(t))
        if (self.length == 0):
            t.next_to(self[1], UP, buff=0)
        else:
            t.next_to(self[-1], UP, buff=0)
        self.length += 1
        self.add(t)
        return t

    def pop(self):
        t = self[-1]
        self.remove(t)
        self.length -= 1
        return t


class QuickSort(Scene):
    def construct(self):
        text1 = Text("Quick Sort", font="IBM Plex Sans",
                     color="#fafafa", size=4)
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOutAndShift(text1, direction=DOWN))
        a = list(range(14))
        random.seed(40)
        random.shuffle(a)
        a = [[i, None] for i in a]
        element = Group()
        for i in range(len(a)):
            rect = Rectangle(
                width=0.5, height=0.5 + a[i][0] * 0.26, color=WHITE, fill_opacity=0.3
            )
            a[i][1] = rect
            element.add(rect)
        element.arrange(RIGHT, aligned_edge=DOWN,
                        buff=0.2).to_corner(DL)
        callStack = CallStack()
        callStack.to_corner(DR)
        codeStart = Code(file_name="my_project/code/quickSort_0.cpp",
                         style="vscode").scale(0.7).to_corner(UL)
        codeStartR = CodeRunner([1, 1, 1, 2, 1], codeStart)
        codeStart.add(codeStartR)
        self.play(FadeInFrom(codeStart[0], LEFT),
                  FadeInFrom(callStack, RIGHT)
                  )
        self.play(Write(codeStart[1]), Write(codeStart.code))
        self.play(codeStartR.runTo(3))
        self.play(
            AnimationGroup(*[FadeInFrom(x, DOWN)
                             for x in element], lag_ratio=0.2),
            run_time=1,
        )

        self.play(codeStartR.runTo(4))
        code1 = Code(file_name="my_project/code/quickSort_1.cpp",
                     style="vscode").scale(0.6).to_corner(UL)
        code1.add(CodeRunner([1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], code1))
        code2 = Code(file_name="my_project/code/quickSort_2.cpp",
                     style="vscode").scale(0.6).next_to(code1, RIGHT).align_to(code1, UP)
        code2.add(CodeRunner([1]*7, code2))

        self.play(LaggedStart(FadeInFrom(code2[0], UP), AnimationGroup(
            Write(code2[1]), Write(code2.code)), lag_ratio=1))
        self.play(FadeOutAndShift(codeStart, LEFT),
                  FadeInFrom(code1[0], LEFT),
                  FadeInFrom(code1[1], LEFT), FadeInFrom(code1.code, LEFT),
                  )
        speed = 0.5

        def partition(low,  high):
            e = callStack.push("partition(a, {}, {})".format(low, high))
            self.play(FadeInFrom(e, UP*6),
                      code1[0][0].set_stroke, {
                      "opacity": 1, "width": 5, "color": GREEN},
                      code2[0][0].set_stroke, {"opacity": 0}, run_time=speed)
            pivot = a[high]
            i = low
            self.play(code1[-1].runTo(1), run_time=speed)
            self.play(FadeToColor(
                a[high][1], YELLOW, run_time=speed)
            )
            ti = Text("i", font="Hack", size=0.4).next_to(
                a[i][1], DOWN, buff=0.4)
            tj = Text("j", font="Hack", size=0.4).next_to(
                a[i][1], DOWN, buff=0.1)
            self.play(code1[-1].runTo(2), FadeInFrom(
                ti, DOWN), run_time=speed)
            for j in range(low, high):
                self.play(code1[-1].runTo(4), run_time=speed)
                if j == low:
                    self.play(FadeIn(tj), run_time=speed/2)
                else:
                    self.play(tj.next_to, a[j][1], DOWN, {
                              "buff": 0.1}, run_time=speed/2)
                self.play(FadeToColor(
                    a[j][1], YELLOW, rate_func=there_and_back_with_pause),  run_time=speed)
                if (a[j] < pivot):
                    a[i], a[j] = a[j], a[i]
                    self.play(code1[-1].runTo(5), run_time=speed)
                    if (a[i][1] != a[j][1]):
                        self.play(a[i][1].set_x, a[j][1].get_x(),
                                  a[j][1].set_x, a[i][1].get_x(),
                                  ti.next_to, a[i+1][1], DOWN, {"buff": 0.4}, run_time=speed)
                    else:
                        self.play(ti.next_to, a[i+1][1], DOWN, {"buff": 0.4},
                                  run_time=speed/2)
                    i += 1
            a[i], a[high] = a[high], a[i]
            self.play(code1[-1].runTo(8), run_time=speed)
            self.play(
                FadeOutAndShift(tj, DOWN), run_time=speed/2)
            self.play(a[i][1].set_color, GREEN,
                      a[i][1].set_x, a[high][1].get_x(),
                      a[high][1].set_x, a[i][1].get_x(), run_time=speed)
            self.play(code1[-1].runTo(9), run_time=speed)
            e = callStack.pop()
            self.play(FadeOutAndShift(e, UP*6),
                      code1[-1].runTo(-1), run_time=speed)
            self.play(
                FadeOutAndShift(ti, DOWN), code1[0].set_stroke, {
                    "opacity": 0}, code2[0][0].set_stroke, {"opacity": 0.5}, run_time=speed)
            return i

        def quickSort(low, high):
            nonlocal code2
            e = callStack.push("quickSort(a, {}, {})".format(low, high))
            g = Group(*[x[1] for x in a[low:high+1]])
            tt = [g.shift, UP/3]
            if not (low == 0 and high == len(a)-1):
                tt += [FadeInFrom(code2, UP)]
            self.play(*tt, FadeInFrom(e, UP*6), run_time=speed)
            self.play(code2[0][0].set_stroke, {
                      "opacity": 1, "width": 5, "color": GREEN}, run_time=speed)
            self.play(code2[-1].runTo(1), run_time=speed)
            if (low < high):
                self.play(code2[-1].runTo(2), run_time=speed)
                pi = partition(low, high)
                self.play(code2[0][0].set_stroke, {
                          "opacity": 0}, code2[-1].runTo(3), run_time=speed)
                temp = code2
                code2 = code2.deepcopy()
                code2[-1].runTo(-1)
                quickSort(low, pi - 1)
                self.play(temp[0][0].set_stroke, {
                          "opacity": 1}, run_time=speed)
                self.play(temp[-1].runTo(4), run_time=speed)
                self.play(temp[0][0].set_stroke, {
                          "opacity": 0}, run_time=speed)
                code2 = temp.deepcopy()
                code2[-1].runTo(-1)
                quickSort(pi + 1, high)
                self.play(temp[0][0].set_stroke, {
                    "opacity": 1}, run_time=speed)
                code2 = temp
            self.play(code2[-1].runTo(5), run_time=speed)
            self.play(
                g.shift, DOWN/3,
                g.set_color, GREEN, code2[0][0].set_stroke, {
                    "opacity": 0, }, code2[-1].runTo(-1), run_time=speed)
            e = callStack.pop()
            if not (low == 0 and high == len(a)-1):
                self.play(FadeOutAndShift(code2, UP),
                          FadeOutAndShift(e, UP*6), run_time=speed)
            else:
                self.play(FadeOutAndShift(e, UP*6), run_time=speed)

        quickSort(0, len(a)-1)
        self.wait(5)
