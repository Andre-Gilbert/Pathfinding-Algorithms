"""Pathfinder implements the pathfinding algorithms.

Given a grid, the start and destination vertex
the shortest path can be found using one of two algorithms:
Dijkstra's shortest path
    - O(E*log(V)) time complexity
    - O(V) space complexity

A* search algorithm
    - Manhatten distance heuristic
    - h = |x_start - x_destination| + |y_start - y_destination|
"""
from queue import PriorityQueue
from random import randrange

import pygame

from vertex import Vertex


class Pathfinder:
    """Class which implements the pathfinding algorithms.

    Attributes:
        __grid: A 2D array containing vertices.
        __start: The start vertex.
        __destination: The destination vertex.
    """
    def __init__(self, grid: list[list[Vertex]], start: Vertex, destination: Vertex) -> None:
        """Initializes the pathfinder."""
        self.__grid = grid
        self.__start = start
        self.__destination = destination

    def dijkstra(self, gui: object) -> bool:
        """Visualizes Dijkstra's shortest path algorithm.

        Args:
            gui: The graphical user interface.

        Returns:
            True if the shortest path is found, False otherwise.
        """
        count = 0
        queue = PriorityQueue()
        queue.put((0, count, self.__start))
        visited = {self.__start}
        came_from = {}

        distance = {vertex: float("inf") for row in self.__grid for vertex in row}
        distance[self.__start] = 0

        while not queue.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = queue.get()[2]
            visited.remove(current)

            # Reconstruct path
            if current == self.__destination:
                self.__reconstruct_path(gui, came_from, self.__destination)
                self.__start.make_start()
                return True

            # Check all neighbors
            for neighbor in current.neighbors:
                temp_distance = distance[current] + 1

                if temp_distance < distance[neighbor]:
                    came_from[neighbor] = current
                    distance[neighbor] = temp_distance

                    if neighbor not in visited:
                        count += 1
                        queue.put((distance[neighbor], count, neighbor))
                        visited.add(neighbor)

                        # Mark as visiting
                        if neighbor != self.__destination:
                            neighbor.make_visiting()

            # Redraw the gui
            gui.draw(self.__grid)

            # Mark as visited
            if current != self.__start:
                current.make_visited()

        return False

    def a_star_search(self, gui: object) -> bool:
        """Visualizes the A* search algorithm.

        Args:
            gui: The graphical user interface.

        Returns:
            True if the shortest path is found, False otherwise.
        """
        count = 0
        queue = PriorityQueue()
        queue.put((0, count, self.__start))

        g_score = {node: float("inf") for row in self.__grid for node in row}
        g_score[self.__start] = 0
        f_score = {node: float("inf") for row in self.__grid for node in row}
        f_score[self.__start] = self.__manhatten_distance(self.__start.get_position(),
                                                          self.__destination.get_position())

        open_set = {self.__start}
        came_from = {}

        while not queue.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = queue.get()[2]
            open_set.remove(current)

            # Reconstruct path
            if current == self.__destination:
                self.__reconstruct_path(gui, came_from, self.__destination)
                self.__start.make_start()
                return True

            # Check all neighbors
            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self.__manhatten_distance(neighbor.get_position(),
                                                                                 self.__destination.get_position())

                    if neighbor not in open_set:
                        count += 1
                        queue.put((f_score[neighbor], count, neighbor))
                        open_set.add(neighbor)

                        # Mark as visiting
                        if neighbor != self.__destination:
                            neighbor.make_visiting()

            # Redraw the grid
            gui.draw(self.__grid)

            # Mark as visited
            if current != self.__start:
                current.make_visited()

        return False

    def generate_maze(self) -> None:
        """Generates a random maze."""
        n = round(len(self.__grid) * len(self.__grid) * 0.3)

        for i in range(n + 1):
            row = randrange(len(self.__grid))
            col = randrange(len(self.__grid))

            if self.__grid[row][col] != self.__start and self.__grid[row][col] != self.__destination:
                self.__grid[row][col].make_wall()

    def __manhatten_distance(self, current: Vertex, destination: Vertex) -> int:
        """Computes the manhatten distance to the destination.

        Args:
            current: The current vertex we're considering.
            destination: The destination vertex.

        Returns:
            The absolute distance of the x, y coordinates
            of the current vertex to the destination.
        """
        x1, y1 = current
        x2, y2 = destination
        return abs(x1 - x2) + abs(y1 - y2)

    def __reconstruct_path(self, gui: object, came_from: dict[Vertex, Vertex], current: Vertex) -> None:
        """Reconstructs the shortest path.

        Args:
            gui: The graphical user interface.
            came_from: A dictionary containing the path to the destination.
            current: The current vertex we're considering.
        """
        while current in came_from:
            current = came_from[current]
            current.make_path()
            gui.draw(self.__grid)
