from manim import *
import networkx as nx
import numpy as np
import random


class GraphExample(Scene):
    def construct(self):
        n = 15
        G = nx.fast_gnp_random_graph(n, 0.161, 29489)
        scale = np.array([6.5, 3.5])
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
            # leng = round(np.linalg.norm(positions[u] - positions[v]), 2)
            # a = edge.get_angle()+PI
            # t = DecimalNumber(leng, background_stroke_width=0, color=YELLOW).scale(0.5).move_to(
            #     edge)
            # if (positions[u][0] >= positions[v][0]):
            #     t.rotate(a)
            # else:
            #     t.rotate(a+PI)
            # edge.add(t)
            edges.add(edge)
        graph.add(edges, nodes)
        for u, v in G.edges():
            G[u][v]['weight'] = np.linalg.norm(positions[u] - positions[v])
        # mData = nx.to_numpy_matrix(G)
        # mData = np.round(mData, 2)
        # m = DecimalMatrix(mData).scale(
        #     0.5).to_corner(DR)
        self.play(Write(edges), Write(
            nodes),  run_time=2)
        self.wait(3)
