import unittest
from test_bfs_template import TestBFS


class TestBFSSimple(TestBFS):
    def setUp(self) -> None:
        size = 4
        edges = [
            [0, 1], [1, 2], [2, 3]
        ]
        super().init(edges, size)

    def test_1(self):
        initials = [0]
        expected = [0, 0, 0, 0]
        super().template_test(initials, expected)

    def test_2(self):
        initials = [1, 2]
        expected = [None, 1, 2, 2]
        super().template_test(initials, expected)


class TestBFSConvergence(TestBFS):
    def setUp(self) -> None:
        size = 5
        edges = [
            [0, 1], [1, 2],
            [4, 3], [3, 2]
        ]
        super().init(edges, size)

    def test_1(self):
        initials = [0, 4]
        expected = [0, 0, 0, 4, 4]
        super().template_test(initials, expected)

    def test_2(self):
        initials = [1, 3]
        expected = [None, 1, 1, 3, None]
        super().template_test(initials, expected)

    def test_3(self):
        initials = [2]
        expected = [None, None, 2, None, None]
        super().template_test(initials, expected)


class TestBFSCycle(TestBFS):
    def setUp(self) -> None:
        size = 5
        edges = [
            [0, 1], [1, 2], [2, 3], [3, 4], [4, 0]
        ]
        super().init(edges, size)

    def test_1(self):
        initials = [0]
        expected = [0, 0, 0, 0, 0]
        super().template_test(initials, expected)

    def test_2(self):
        initials = [0, 3]
        expected = [0, 0, 0, 3, 3]
        super().template_test(initials, expected)

    def test_3(self):
        initials = [0, 2, 4]
        expected = [0, 0, 2, 2, 4]
        super().template_test(initials, expected)


class TestBFSBackEdge(TestBFS):
    def setUp(self) -> None:
        size = 5
        edges = [
            [0, 1], [1, 0], [2, 3], [3, 2], [3, 4], [2, 4]
        ]
        super().init(edges, size)

    def test_1(self):
        initials = [0]
        expected = [0, 0, None, None, None]
        super().template_test(initials, expected)

    def test_2(self):
        initials = [1, 4]
        expected = [1, 1, None, None, 4]
        super().template_test(initials, expected)

    def test_3(self):
        initials = [2, 3]
        expected = [None, None, 2, 3, 2]
        super().template_test(initials, expected)


if __name__ == '__main__':
    unittest.main()
