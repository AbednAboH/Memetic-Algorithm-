# Memetic Algorithm Optimization Project

## Overview

This project implements a **Memetic Algorithm (MA)** in Python, combining global search strategies of Genetic Algorithms (GAs) with local optimization techniques. This hybrid approach enhances both the convergence speed and the quality of solutions for complex optimization problems.

## Problem Domains Addressed

The Memetic Algorithm is applied to the following optimization challenges:

- **N-Queens Problem**: Placing N chess queens on an N×N chessboard so that no two queens threaten each other.

- **Bin Packing Problem**: Efficiently packing objects of varying sizes into a finite number of bins, each with a fixed capacity.

## Project Structure

The repository is organized as follows:

```
Memetic-Algorithm/
├── src/
│   ├── algorithms/
│   │   ├── genetic_algorithm.py    # Implementation of the Genetic Algorithm
│   │   ├── memetic_algorithm.py    # Implementation of the Memetic Algorithm
│   │   └── local_search.py         # Local search strategies for solution refinement
│   ├── problems/
│   │   ├── n_queens.py             # N-Queens problem definition
│   │   └── bin_packing.py          # Bin Packing problem definition
│   ├── utils/
│   │   ├── fitness_functions.py    # Fitness evaluation methods
│   │   ├── selection_methods.py    # Selection strategies for GA
│   │   ├── crossover_methods.py    # Crossover operators for GA
│   │   └── mutation_methods.py     # Mutation techniques for GA
│   ├── main.py                     # Entry point to execute the algorithm
│   └── config.py                   # Configuration settings for experiments
├── README.md                       # Project documentation (this file)
├── requirements.txt                # List of required Python packages
└── setup.py                        # Installation setup script
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Required Python packages listed in `requirements.txt`

### Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/AbednAboH/Memetic-Algorithm-.git
   cd Memetic-Algorithm
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing, manually install the necessary packages, such as NumPy:

   ```bash
   pip install numpy
   ```

## Usage Guide

### Configuring the Algorithm

Before running the algorithm, adjust the settings in `config.py` to specify:

- The problem to solve (`n_queens` or `bin_packing`).
- Hyperparameters such as population size, mutation rate, crossover rate, local search frequency, and the number of generations.

### Running the Algorithm

After configuration, execute the main script:

```bash
python src/main.py
```

This command initiates the Memetic Algorithm with the chosen settings and problem.

### Example: Solving the N-Queens Problem

With `config.py` set for the N-Queens problem, run:

```bash
python src/main.py
```

The algorithm will process and display the optimal arrangement of queens on the board.

## Detailed Module Descriptions

### 1. `algorithms/`

- **`genetic_algorithm.py`**: Implements the standard Genetic Algorithm, featuring selection, crossover, and mutation operations to explore the solution space.

- **`memetic_algorithm.py`**: Extends the Genetic Algorithm by integrating local search methods, enhancing individual solutions through refinement processes.

- **`local_search.py`**: Contains local optimization techniques, such as hill climbing and simulated annealing, applied to improve candidate solutions.

### 2. `problems/`

- **`n_queens.py`**: Defines the N-Queens problem, including the representation of the board and constraints to ensure no two queens threaten each other.

- **`bin_packing.py`**: Defines the Bin Packing problem, detailing item sizes and bin capacities, along with constraints to optimize space utilization.

### 3. `utils/`

- **`fitness_functions.py`**: Provides functions to evaluate the fitness of solutions for each problem domain, guiding the evolutionary process.

- **`selection_methods.py`**: Implements various parent selection strategies, such as tournament selection and roulette wheel selection, determining which individuals reproduce.

- **`crossover_methods.py`**: Contains crossover operators like one-point and uniform crossover, facilitating the combination of genetic information between parents.

- **`mutation_methods.py`**: Defines mutation techniques, including bit-flip and swap mutations, introducing genetic diversity into the population.

### 4. `main.py`

Serves as the entry point for the program. It parses configuration settings, initializes the chosen problem and algorithm, and manages the execution flow, including logging and result output.

### 5. `config.py`

Houses configuration parameters, allowing users to customize aspects such as:

- Problem selection (`n_queens` or `bin_packing`)
- Population size
- Number of generations
- Crossover and mutation rates
- Local search application frequency

## Extending the Project

### Adding a New Optimization Problem

1. **Define the Problem**: Create a new module in the `problems/` directory (e.g., `traveling_salesman.py`) that outlines the problem's structure and constraints.

2. **Develop a Fitness Function**: Implement an evaluation method in `utils/fitness_functions.py` to assess solution quality for the new problem.

3. **Update Configuration**: Modify `config.py` to include parameters and options pertinent to the new problem.

## Sample Output

### Memetic Algorithm Solving N-Queens

```
Generation 1: Best Fitness = 6
Applying local search...
Generation 2: Best Fitness = 3
...
Solution Found: [3, 1, 6, 2, 5, 7, 4, 0]
```

*Interpretation*: The array represents the column positions of queens in each row, indicating a solution where no two queens threaten each other.

## Potential Applications

- **Artificial Intelligence & Machine Learning**: Optimizing model parameters and architectures.

- **Operations Research**: Addressing complex scheduling, routing, and resource allocation problems.

- **Game Development**: Designing AI opponents with strategic planning capabilities.

- **Educational Tools**: Demonstrating advanced optimization algorithms in academic settings.

## Contributing

Contributions to enhance this project are welcome. To contribute:

1. Fork the repository.

2. Create a new branch for your feature (`feature-new-optimization`).

3. Commit your changes and push them to your fork.

4. Submit a pull request detailing your modifications.

## License

This project is licensed under the **MIT License**, permitting open-source use, modification, and distribution.

---

This `README.md` provides a detailed and accurate representation of the Memetic Algorithm project, reflecting its full scope and capabilities.
