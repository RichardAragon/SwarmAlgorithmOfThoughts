# Swarm Algorithm of Thoughts (Swarm-AoT)

Swarm Algorithm of Thoughts (Swarm-AoT) is a generalized framework for solving heuristic optimization problems using **swarm intelligence**. Inspired by the concept of the **Algorithm of Thoughts**, this framework leverages multiple agents exploring a problem space collaboratively to find optimal solutions. It is lightweight, modular, and designed to adapt to various problem domains.

---

## Features

- **Generalized Design**: Supports any heuristic optimization problem with customizable problem spaces, evaluation functions, and update mechanisms.
- **Swarm Intelligence**: Utilizes multiple agents working in parallel to explore and exploit solutions.
- **Real-Time Feedback**: Outputs live updates when new optimal solutions are found.
- **Lightweight and Flexible**: Minimal dependencies, making it easy to integrate into existing projects.
- **Scalable**: Works for small-scale problems and large, complex environments.

---

## Use Cases

Swarm-AoT can be applied to a variety of problem domains, including but not limited to:

1. **Numerical Optimization**: Find the minimum or maximum of mathematical functions.
2. **Resource Allocation**: Optimize task assignments, inventory management, or scheduling.
3. **Pattern Recognition**: Discover anomalies or patterns in datasets.
4. **Prime Number Finder**: Dynamically find prime numbers in a given range.
5. **Combinatorial Problems**: Solve problems like the Traveling Salesman or Knapsack problem with heuristic-based solutions.

---

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/RichardAragon/swarm-algorithm-of-thoughts.git
cd swarm-algorithm-of-thoughts
```

No additional dependencies are required other than Python 3.x and NumPy:

```bash
pip install numpy
```

---

## Usage

### Quick Start

Here's how you can use the framework to solve a heuristic optimization problem.

1. **Define the Problem Space**: Specify the range, dataset, or structure of your problem.
2. **Create a Heuristic Function**: Write a function to evaluate the quality of a solution.
3. **Define an Update Function**: Write a function to control how agents explore the problem space.
4. **Run the Optimizer**: Use the `SwarmAoT` class to run the optimization.

### Example: Prime Number Finder

The following example demonstrates how to find prime numbers within a range using Swarm-AoT:

```python
from swarm_aot import SwarmAoT

# Problem Space: Numbers between 2 and 100
problem_space = range(2, 100)

# Heuristic Function: Prioritize prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def heuristic(n):
    return -1 if is_prime(n) else n  # Primes have higher priority (lower score)

# Update Function: Random walk
def update_fn(position, space):
    step = random.randint(-5, 5)
    new_position = position + step
    return max(min(new_position, max(space)), min(space))

# Initialize and run the optimizer
swarm_aot = SwarmAoT(num_agents=10, problem_space=problem_space, heuristic=heuristic, update_fn=update_fn)
best_solution, best_score = swarm_aot.optimize(iterations=50)

print(f"Best Solution: {best_solution}, Score: {best_score}")
```

---

## Class Documentation

### `SwarmAoT`

The main class for implementing Swarm-AoT.

#### Constructor

```python
SwarmAoT(num_agents: int, problem_space: Any, heuristic: Callable, update_fn: Callable)
```

- **`num_agents`**: Number of agents in the swarm.
- **`problem_space`**: The range, dataset, or structure representing the problem space.
- **`heuristic`**: Function that evaluates the quality of a solution.
- **`update_fn`**: Function defining how agents explore the problem space.

#### Methods

1. **`optimize(iterations: int = 100) -> Tuple[Any, float]`**
   - Runs the optimization process for a specified number of iterations.
   - Returns the best solution and its score.

---

## Contributing

Contributions are welcome! Here are some ways you can help:

1. **Enhance Functionality**:
   - Add support for advanced update strategies (e.g., inspired by Particle Swarm Optimization or Genetic Algorithms).
   - Include multi-objective optimization capabilities.

2. **Add Examples**:
   - Create new problem demonstrations using Swarm-AoT.
   - Share visualizations of agent behavior.

3. **Improve Documentation**:
   - Write detailed tutorials or expand on existing documentation.

### How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature-name"`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. 
