from manim import *
import networkx as nx
import numpy as np
import random


class GraphExample(Scene):
    def construct(self):
        G = nx.fast_gnp_random_graph(5, 0.5, 12)
        scale = np.array([5, 3])
        positions = {k: v * scale for k,
                     v in nx.kamada_kawai_layout(G).items()}

        graph = VGroup()
        nodes = VGroup()
        for k, v in positions.items():
            dot = Dot([*v, 0], radius=0.2)
            text = Text(str(k), font="hack", size=0.5,
                        color=BLACK).move_to(dot)
            dot.add(text)
            nodes.add(dot)
        edges = VGroup()
        for u, v in G.edges():
            edge = Line([*positions[u], 0], [*positions[v], 0], color=GRAY)
            v = round(np.linalg.norm(positions[u] - positions[v]), 2)
            a = edge.get_angle()
            a = a+PI*2 if a > PI/2 else a
            t = Text(str(v), font="hack", size=0.4).move_to(
                edge).rotate(a)
            edges.add(edge, t)
        graph.add(edges, nodes)
        graph.to_corner(UL)
        self.play(Write(edges), Write(
            nodes), run_time=4)
        for u, v in G.edges():
            G[u][v]['weight'] = np.linalg.norm(positions[u] - positions[v])
        mData = nx.to_numpy_matrix(G)
        mData = np.round(mData, 2)
        m = Matrix(mData).scale(0.5).to_corner(DR)
        self.add(m)
        self.wait(3)
