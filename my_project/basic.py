#!/usr/bin/env python

from manim import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

# output = output_start + ((output_end - output_start) / (input_end - input_start)) * (input - input_start)


class Test(Scene):
    def construct(self):
        t = Triangle(stroke_width=1).scale(4)
        n = 8
        self.tris = [[] for _ in range(n)]
        self.draw(t.get_bottom(), t.get_width(), 2, n)
        self.add(t)
        for x in self.tris[::-1]:
            self.play(*[Write(t) for t in x])
        self.wait(3)

    def draw(self, xb, length, scale, depth):
        if depth == 0:
            return
        self.tris[depth-1] += [Triangle(stroke_width=1).scale(scale).flip(
            RIGHT).move_to(xb).align_to(xb, DOWN)]
        self.draw(xb+[-length/4, 0, 0], length/2, scale/2, depth-1)
        self.draw(xb+[length/4, 0, 0], length/2, scale/2, depth-1)
        self.draw(xb+[0, ((length*length-length*length/4)**0.5)/2, 0],
                  length/2, scale/2, depth-1)


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty " "\\frac{1}{n^2} = \\frac{\\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title), FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\" "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([np.sin(p[1]), np.sin(p[0]), 0, ]),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square2 = Square()
        square.flip(LEFT)
        square2.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)
        square2.set_fill(YELLOW, opacity=0.3)
        self.play(ShowCreation(square))
        self.play(ReplacementTransform(square, circle))
        self.play(ReplacementTransform(circle, square2))
        self.play(FadeOut(square2))


class WarpSquare(Scene):
    def construct(self):
        square = Text("test", font="arial")
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(
                    np.exp(R3_to_complex(point))), square
            )
        )
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text", tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(config["frame_width"] - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0, show_ellipsis=True, num_decimal_places=3, include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN, rate_func=there_and_back, run_time=5,
        )
        self.wait()


class VDictTest(Scene):
    def construct(self):
        square = Square().set_color(RED)
        circle = Circle().set_color(YELLOW).next_to(square, UP)

        # create dict from list of tuples each having key-mobject pair
        pairs = [("s", square), ("c", circle)]
        my_dict = VDict(*pairs, show_keys=True)

        # display it just like a VGroup
        self.play(ShowCreation(my_dict))
        self.wait()

        text = TextMobject("Some text").set_color(GREEN).next_to(square, DOWN)

        # add like a VGroup
        my_dict.add(("t", text))
        self.wait()

        rect = Rectangle().next_to(text, DOWN)
        # can also do key assignment like a python dict
        my_dict["r"] = rect

        # access submobjects like a python dict
        my_dict["t"].set_color(PURPLE)
        self.play(my_dict["t"].scale, 3)
        self.wait()

        # also supports python dict styled reassignment
        my_dict["t"] = TextMobject("Some other text").set_color(BLUE)
        self.wait()

        # remove submojects by key
        my_dict.remove("t")
        self.wait()

        self.play(Uncreate(my_dict["s"]))
        self.wait()

        self.play(FadeOut(my_dict["c"]))
        self.wait()

        self.play(FadeOutAndShift(my_dict["r"], DOWN))
        self.wait()

        # iterate through all submobjects currently associated with my_dict
        for submob in my_dict.get_all_submobjects():
            self.play(ShowCreation(submob))
            self.wait()


# See old_projects folder for many, many more
