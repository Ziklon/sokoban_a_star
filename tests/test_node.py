# test_math_utils.py
import unittest
from app.node import Node
from app.math_utils import add

class TestNode(unittest.TestCase):

    def test_node_order(self):
        node1 = Node((0,0), [], [], 5)
        node2 = Node((0,0), [], [], 10)
        self.assertTrue(node1 < node2)