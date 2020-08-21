from manim import *
import networkx as nx
import numpy as np
import random


class GraphExample(Scene):
    def construct(self):
        G = nx.watts_strogatz_graph(n=100, k=4, p=0.6)
        scale = np.array([3, 3])
        positions = {k: v * scale for k,
                     v in nx.circular_layout(G).items()}
        graph = VGroup()
        nodes = VGroup()
        for k, v in positions.items():
            dot = Dot([*v, 0], radius=0.04, color=BLUE)
            nodes.add(dot)
        edges = VGroup()
        for u, v in G.edges():
            edge = Line([*positions[u], 0], [*positions[v], 0],
                        color=WHITE).set_stroke(WHITE, 0.5)
            edges.add(edge)
        graph.add(edges, nodes)
        for u, v in G.edges():
            G[u][v]['weight'] = np.linalg.norm(positions[u] - positions[v])
        self.play(Write(edges), Write(
            nodes),  run_time=3)
        self.play(Write(edges), Write(
            nodes),  run_time=3, rate_func=lambda t: smooth(1 - t), remover=True)
        self.wait(0.5)
