from pygraphblas import Matrix, Vector


def reachable_from(adjacency: Matrix, initials: Vector) -> Vector:
    """
    :param adjacency: Adjacency matrix of graph
    :param initials: Vector of bool if vertex is initial
    :return: Vector of integers.
    If empty, then vertex in unreachable
    Otherwise, the value is the number of one of the nearest initials (1-based)
    """
    return __reachable_from(adjacency, initials.nonzero().emult(Vector.from_1_to_n(initials.size)))


def __reachable_from(adjacency: Matrix, reachable: Vector) -> Vector:
    """
    Takes a vector of labels at the starting vertices and pushes them using an adjacency matrix using the bfs algorithm

    :param reachable: Reachable at start of bfs
    Empty is unreachable
    not Empty is reachable where value is marker which will be pushed to the reachable within the current vertex
    :return: Vector of labels.
    If label is empty, then the vertex is unreachable.
    Otherwise it is the label from one of the nearest initials.
    """
    reachable_next = __reachable_from_next(adjacency, reachable)
    while not reachable_next.iseq(reachable):
        reachable = reachable_next
        reachable_next = __reachable_from_next(adjacency, reachable)
    return reachable


def __reachable_from_next(adjacency: Matrix, reachable: Vector) -> Vector:
    """
    :return: Reachable vector within the next bfs iteration
    """
    reachable_next = reachable.vxm(adjacency, semiring=reachable.type.min_times)
    return reachable.eadd(reachable_next, add_op=reachable.type.first)
