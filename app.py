"""
Swarm Algorithm of Thoughts (Swarm-AoT)

A generalized framework for solving heuristic optimization problems using
swarm intelligence and the Algorithm of Thoughts approach.

MIT License
Copyright (c) 2024 [Richard Aragon]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import numpy as np
import random
from typing import Callable, List, Tuple, Any

class SwarmAoT:
    def __init__(self, num_agents: int, problem_space: Any, heuristic: Callable, update_fn: Callable):
        """
        Initialize the Swarm Algorithm of Thoughts.

        :param num_agents: Number of agents in the swarm.
        :param problem_space: The problem space (can be a range, list, or custom object).
        :param heuristic: A function to evaluate the quality of a solution.
        :param update_fn: A function to define how agents explore the problem space.
        """
        self.num_agents = num_agents
        self.problem_space = problem_space
        self.heuristic = heuristic
        self.update_fn = update_fn
        self.swarm = self._initialize_swarm()
        self.global_best = None
        self.global_best_score = float('inf')

    def _initialize_swarm(self) -> List[Any]:
        """Initialize the swarm with random positions in the problem space."""
        return [random.choice(self.problem_space) for _ in range(self.num_agents)]

    def optimize(self, iterations: int = 100) -> Tuple[Any, float]:
        """
        Perform optimization using the Swarm-AoT algorithm.

        :param iterations: Number of iterations to run the optimization.
        :return: The best solution found and its score.
        """
        for iteration in range(iterations):
            for agent_idx, position in enumerate(self.swarm):
                # Evaluate current position
                score = self.heuristic(position)
                
                # Update global best if a better solution is found
                if score < self.global_best_score:
                    self.global_best = position
                    self.global_best_score = score
                    print(f"Iteration {iteration}, Agent {agent_idx}: New global best found with score {score}")

                # Update agent's position using the update function
                self.swarm[agent_idx] = self.update_fn(position, self.problem_space)

        return self.global_best, self.global_best_score

# Example Usage
if __name__ == "__main__":
    # Define the problem space: a range of numbers to search
    problem_space = range(2, 100)

    # Define a heuristic function: checking if a number is prime
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def heuristic(n: int) -> float:
        """Heuristic function to minimize: smaller is better (negative primes are better)."""
        return -1 if is_prime(n) else n

    # Define an update function: random walk within the problem space
    def update_fn(position: int, space: range) -> int:
        step = random.randint(-5, 5)
        new_position = position + step
        return max(min(new_position, max(space)), min(space))

    # Initialize and run the optimizer
    swarm_aot = SwarmAoT(num_agents=10, problem_space=problem_space, heuristic=heuristic, update_fn=update_fn)
    best_solution, best_score = swarm_aot.optimize(iterations=50)

    print("\nOptimization Complete!")
    print(f"Best Solution: {best_solution}, Score: {best_score}")
