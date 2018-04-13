#!/usr/bin/env python
from nose.tools import *
import networkx


class TestRandomClusteredGraph:

    def test_valid(self):
        node = [1, 1, 1, 2, 1, 2, 0, 0]
        tri = [0, 0, 0, 0, 0, 1, 1, 1]
        joint_degree_sequence = zip(node, tri)
        G = networkx.random_clustered_graph(joint_degree_sequence)
        assert_equal(G.number_of_nodes(), 8)
        assert_equal(G.number_of_edges(), 7)

    def test_valid2(self):
        G = networkx.random_clustered_graph(
            [(1, 2), (2, 1), (1, 1), (1, 1), (1, 1), (2, 0)])
        assert_equal(G.number_of_nodes(), 6)
        assert_equal(G.number_of_edges(), 10)

    def test_invalid1(self):
        assert_raises((TypeError, networkx.NetworkXError),
                      networkx.random_clustered_graph, [[1, 1], [2, 1], [0, 1]])

    def test_invalid2(self):
        assert_raises((TypeError, networkx.NetworkXError),
                      networkx.random_clustered_graph, [[1, 1], [1, 2], [0, 1]])