import unittest
from pygraphblas import Matrix, Vector, BOOL
from bfs import reachable_from


def transpose(edges: list) -> list:
    return list(map(list, zip(*edges)))


def make_adjacency(edges: list, size: int) -> Matrix:
    lists = transpose(edges)
    return Matrix.from_lists(lists[0], lists[1], [True] * len(lists[0]), size, size, BOOL)


def make_initials(initials: list, size: int) -> Vector:
    return Vector.from_lists(initials, [True] * len(initials), size, BOOL)


def expected_to_vec(lst: list) -> Vector:
    indices = [i for i in range(len(lst)) if lst[i] is not None]
    values = [lst[i] + 1 for i in indices]
    return Vector.from_lists(indices, values, len(lst))


class TestBFS(unittest.TestCase):
    def init(self, edges: list, size: int) -> None:
        self.size = size
        self.adjacency = make_adjacency(edges, size)

    def template_test(self, initials: list, expected: list):
        initials_vec = make_initials(initials, self.size)
        actual = reachable_from(self.adjacency, initials_vec)
        self.assertTrue(expected_to_vec(expected).iseq(actual))
