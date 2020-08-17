from manim import *
import networkx as nx
import numpy as np
import random


class GraphExample(Scene):
    def construct(self):
        G = nx.fast_gnp_random_graph(10, 0.4, random.Random())
        G = nx.eulerize(G)
        scale = np.array([5.5, 2.5])
        positions = {k: v * scale for k, v in nx.spring_layout(G).items()}
        nodes = {}
        groupD = Group()
        for node, pos in positions.items():
            d = Dot([*pos, 0], radius=0.4)
            text = Text(str(node), font="arial",
                        color=BLACK).next_to(d, ORIGIN)
            d.add(text)
            nodes[node] = d
            groupD.add(d)
        groupL = Group()
        for (u, v, _) in G.edges:
            a = [*positions[u], 0]
            b = [*positions[v], 0]
            groupL.add(Line(a, b))
        self.play(*[ShowCreation(e.set_z_index(10)) for e in groupL],
                  *[GrowFromCenter(e.set_z_index(100)) for e in groupD], run_time=3)
        self.wait(2)
        ll = list(nx.eulerian_circuit(G, 0))
        self.play(Indicate(nodes[ll[0][0]]))
        for (u, v) in ll:
            l = Line([*positions[u], 0], [*positions[v], 0],
                     color=YELLOW, z_index=11)
            self.play(
                AnimationGroup(
                    ShowCreation(
                        l, color=YELLOW),
                    Indicate(nodes[v]),
                    lag_ratio=1),
            )
            self.play(l.set_color, GRAY, run_time=0.4)
        self.wait(4)
